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
                    echo "Build Number: ${env.BUILD_NUMBER}"
                    bat 'pip list'
                    bat "${PYTHON_PATH} -m pytest ./test1.py > output.log 2>&1 || exit 0"
                    bat "${PYTHON_PATH} push_data.py"
                }
            }
        }
    }
}