pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Clona el repositorio desde GitHub
                checkout scm
            }
        }

        stage('Build') {
            steps {
                // Construye y levanta los contenedores con Docker Compose
                script {
                    sh 'docker-compose down'
                    sh 'docker-compose up -d --build'
                }
            }
        }

        stage('Test') {
            steps {
                // Aquí puedes añadir comandos para ejecutar pruebas (opcional)
                echo 'Running tests...'
            }
        }

        stage('Post-deploy') {
            steps {
                // Puedes añadir tareas adicionales como limpieza o notificaciones
                echo 'Application successfully deployed!'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished!'
        }
        success {
            echo 'Build succeeded!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}
