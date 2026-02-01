pipeline {
    agent none 
    
    stages {
        stage('Test Matrix') {
            matrix {
                axes {
                    axis {
                        name 'PYTHON_VERSION'
                        values '3.9', '3.10' 
                    }
                }
                stages {
                    stage('Setup and Test') {
                        agent {
                            docker { image "python:${PYTHON_VERSION}" }
                        }
                        steps {
                            sh 'python -m pip install --upgrade pip'
                            sh 'pip install pytest'
                            sh 'if [ -f requirements.txt ]; then pip install -r requirements.txt; fi'
                            
                            sh 'pytest'
                        }
                    }
                    
                    stage('Build Docker Image') {
                        when {
                            expression { env.PYTHON_VERSION == '3.10' }
                        }
                        steps {
                            echo "Building Docker image for Python 3.10..."
                            sh 'echo "docker build -t moja-app:v1 ."'
                        }
                    }
                }
            }
        }
    }
    post {
        always {
            echo 'Proces zakonczony.'
        }
    }
}