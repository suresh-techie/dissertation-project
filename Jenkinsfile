pipeline {
    agent { label 'my-local-agent' }  // Assign the job to a specific local agent

    environment {
        PYTHON_PATH = 'C:\\Users\\Suresh\\AppData\\Local\\Programs\\Python\\Python311\\python.exe'
        DIR_PATH = 'C:\\Users\\Suresh\\Documents\\BITS_WILP\\BITS_AIML_Course_documents\\Semester_4\\failure_analysis_tool\\testcases'
    }

    stages {
        stage('Build') {
            steps {
                script {
                    echo "Running on my-local-agent"
                    echo "Current Build ID: ${env.BUILD_ID}"
                    echo "Current Build Number: ${env.BUILD_NUMBER}"
					bat 'C:\\Users\\Suresh\\AppData\\Local\\Programs\\Python\\Python311\\python.exe --version' 
					bat 'C:\\Users\\Suresh\\AppData\\Local\\Programs\\Python\\Python311\\python.exe ./sample_test.py'
                    echo "${PYTHON_PATH} ${DIR_PATH}\\test1.py"
                    // bat "${PYTHON_PATH} ./test1.py"
                    bat "${PYTHON_PATH} ./test1.py > output.log 2>&1"
                    bat "curl -X POST http://127.0.0.1:5000/api/update_failures -H \"Content-Type: application/json\" -d \"{\\\"failure_data\\\": {\\\"failures\\\": [{\\\"category\\\": \\\"Build Failure\\\", \\\"count\\\": 10, \\\"testname\\\": \\\"Test A\\\"}, {\\\"category\\\": \\\"Test Error\\\", \\\"count\\\": 5, \\\"testname\\\": \\\"Test B\\\"}, {\\\"category\\\": \\\"Warning\\\", \\\"count\\\": 3, \\\"testname\\\": \\\"Test C\\\"}, {\\\"category\\\": \\\"Dependency Issue\\\", \\\"count\\\": 9}]}}\""
                }
            }
        }
    }
}