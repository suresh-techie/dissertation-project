import requests
import json

# Define the API URL
url = "http://127.0.0.1:5000/api/update_failures"

# Define the request headers
headers = {"Content-Type": "application/json"}

# Define the request payload (JSON data)
payload = {
    "failure_data": {
        "failures": [
            {"category": "Build Failure", "count": 10, "testname": "Test A"},
            {"category": "Test Error", "count": 5, "testname": "Test B"},
            {"category": "Warning", "count": 3, "testname": "Test C"},
            {"category": "Dependency Issue", "count": 9}
        ]
    }
}

# Convert dictionary to JSON string
json_payload = json.dumps(payload)

# Send the POST request
response = requests.post(url, headers=headers, data=json_payload)

# Print response details
print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")
