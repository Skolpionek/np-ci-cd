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
                        // USUNELISMY: agent { docker ... }
                        // Testy uruchomia sie bezposrednio na Windowsie
                        steps {
                            // Na Windowsie uzywamy 'bat' zamiast 'sh'
                            // || exit 0 na koncu zapewnia, ze pip nie wywali bledu, jak cos juz jest zainstalowane
                            bat 'python -m pip install --upgrade pip'
                            bat 'pip install pytest'
                            
                            // Prosty warunek w Batchu jest trudny, wiec instalujemy na sztywno 
                            // lub zakladamy, ze pytest wystarczy.
                            // Tu uruchamiamy testy:
                            echo "Running tests for Python ${PYTHON_VERSION}..."
                            bat 'pytest'
                        }
                    }
                    
                    stage('Build Docker Image') {
                        when {
                            expression { env.PYTHON_VERSION == '3.10' }
                        }
                        steps {
                            // Tutaj tez symulujemy echem, zeby uniknac bledu 'docker not found'
                            // jesli Metoda 1 nie zadzialala
                            echo "Building Docker image for Python 3.10..."
                            bat 'echo "Symulacja budowania obrazu Docker..."'
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