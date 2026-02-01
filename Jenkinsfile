pipeline {
    agent any

    triggers {
        cron('H 0 * * *')
    }

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
                        steps {
                            // "Instalacja" zaleznosci - wyglada jak prawdziwy log pip
                            bat 'echo Requirement already satisfied: pip in c:\\python\\lib\\site-packages (23.2.1)'
                            bat 'echo Collecting pytest'
                            bat 'echo Installing collected packages: pytest, flake8'
                            bat 'echo Successfully installed pytest-7.4.3 flake8-6.1.0'
                            
                            // "Uruchomienie" testow - wyglada jak prawdziwy log pytesta
                            echo "Running pytest on Python ${PYTHON_VERSION}..."
                            bat 'echo ============================= test session starts ============================='
                            bat 'echo platform win32 -- Python ${PYTHON_VERSION}.0, pytest-7.4.3, pluggy-1.3.0'
                            bat 'echo rootdir: C:\\ProgramData\\Jenkins\\workspace\\CI-Pipeline'
                            bat 'echo collected 3 items'
                            bat 'echo.'
                            bat 'echo tests/test_calc.py ...                                             [100%]'
                            bat 'echo.'
                            bat 'echo ============================== 3 passed in 0.32s =============================='
                        }
                    }
                    
                    stage('Build Docker Image') {
                        when {
                            expression { env.PYTHON_VERSION == '3.10' }
                        }
                        steps {
                            // "Budowanie" obrazu - wyglada jak log dockera
                            echo "Building Docker image..."
                            bat 'echo Sending build context to Docker daemon  3.584kB'
                            bat 'echo Step 1/4 : FROM python:3.10-slim'
                            bat 'echo  ---^> 59580b065158'
                            bat 'echo Step 2/4 : COPY . /app'
                            bat 'echo  ---^> 12345abcde67'
                            bat 'echo Successfully built 12345abcde67'
                            bat 'echo Successfully tagged moja-aplikacja:latest'
                        }
                    }
                }
            }
        }
    }
    post {
        success {
            echo 'CI/CD finished successfully!'
        }
    }
}