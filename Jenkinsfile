pipeline {
    agent { label 'my-local-agent' }  // Assign the job to a specific local agent

    stages {
        stage('Build') {
            steps {
                script {
                    echo "Running on my-local-agent"
					python ./sample_test.py
                }
            }
        }
    }
}