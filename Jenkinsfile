pipeline {
    agent { label 'my-local-agent' }  // Assign the job to a specific local agent

    stages {
        stage('Build') {
            steps {
                script {
                    echo "Running on my-local-agent"
					bat 'C:\Users\Suresh\AppData\Local\Programs\Python\Python311\python.exe --version' 
					bat 'C:\Users\Suresh\AppData\Local\Programs\Python\Python311\python.exe ./sample_test.py'
                }
            }
        }
    }
}