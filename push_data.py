import requests
import json
import csv
import re
import os
import nltk
nltk_data_dir = os.getcwd()
nltk.data.path.append(nltk_data_dir)

# nltk_data_dir = "C:/nltk_data"

nltk.download('stopwords', download_dir=nltk_data_dir, quiet=True)
nltk.download('punkt_tab', download_dir=nltk_data_dir, quiet=True)

import pickle

log_dir = r"output.log"
failure_list = []

summary = {"category": "", "count": 0, "testname": ""}
error_list = ['RuntimeError', 'APIException', 'ScriptIssue', 'TimeoutError', 'OtherIssue', 'SetupIssue', 'ModemIssue', 'NetworkIssue']



# Function to preprocess the log lines (tokenization, stop word removal)
def preprocess_log(logs):
    stop_words = set(nltk.corpus.stopwords.words('english'))
    cleaned_logs = []
    for log in logs:
        tokens = nltk.word_tokenize(log)
        tokens = [word.lower() for word in tokens if word.isalnum()]  # Remove punctuation
        filtered_tokens = [word for word in tokens if word not in stop_words]  # Remove stop words
        cleaned_logs.append(" ".join(filtered_tokens))
    return cleaned_logs


def predict_category(err_summary):
    # Load saved components
    with open("rf_model.pkl", "rb") as model_file:
        rf_model = pickle.load(model_file)
    with open("vectorizer.pkl", "rb") as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)
    with open("label_encoder.pkl", "rb") as label_encoder_file:
        label_encoder = pickle.load(label_encoder_file)
   
    processed_log = preprocess_log(err_summary)
    log_vector = vectorizer.transform(processed_log).toarray()
    
    # Predict and decode the label
    prediction = rf_model.predict(log_vector)
    predicted_label = label_encoder.inverse_transform(prediction)
    return predicted_label[0]

# Function to parse log files
def parse_log_files(log_dir, error_keywords=["error", "exception", "failed"]):
    with open(log_dir, "r") as f:
        content = f.readlines()
    for line in content:
        if "FAILED" in line and "Exception:" in line:
            for item in error_list:
                if item in line:
                    err_log = line
                    break
    return err_log


parsed_log = parse_log_files(log_dir)
test_name = re.findall(r"::(test.*)\s-", parsed_log)[0]
err_summary = re.findall(r"Exception:(.*)", parsed_log)[0]
failure_list.append(err_summary)
category = predict_category(failure_list)

summary["category"] = category
summary["testname"] = test_name
summary["count"] += 1

# Define the API URL
url = "http://127.0.0.1:5000/api/update_failures"

# Define the request headers
headers = {"Content-Type": "application/json"}


# Define the request payload (JSON data)
payload = {
    "failure_data": {
        "failures": []
    }
}

payload["failure_data"]["failures"].append(summary)

print(payload)

# Convert dictionary to JSON string
json_payload = json.dumps(payload)

# Send the POST request
response = requests.post(url, headers=headers, data=json_payload)

# # Print response details
print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")
