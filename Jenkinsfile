pipeline {
    agent { label 'Built-In Node' }  // Assign the job to a specific local agent

    stages {
        stage('Build') {
            steps {
                script {
                    echo "Running on my-local-agent"
                }
            }
        }
    }
}