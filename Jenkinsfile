pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('your-dockerhub-credentials-id')
        DOCKER_IMAGE = 'your-dockerhub-username/your-image-name'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                script {
                    // Build the Docker image using Docker Compose
                    sh 'docker-compose build'
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    // Run the Docker container using Docker Compose
                    sh 'docker-compose up -d'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run the e2e tests
                    try {
                        sh 'docker-compose exec flask_app python /app/tests/e2e.py'
                    } catch (Exception err) {
                        currentBuild.result = 'FAILURE'
                        error('Tests failed')
                    }
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    // Stop and remove the container using Docker Compose
                    sh 'docker-compose down'

                    // Push the new image to DockerHub
                    docker.withRegistry('https://index.docker.io/v1/', 'DOCKERHUB_CREDENTIALS') {
                        sh 'docker-compose push'
                    }
                }
            }
        }
    }

    post {
        always {
            script {
                // Cleanup dangling Docker images and containers
                sh 'docker system prune -f'
            }
        }
        failure {
            script {
                // Notify on failure
                echo 'Pipeline failed.'
            }
        }
    }
}
