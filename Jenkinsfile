pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git "https://github.com/talvinisky/WorldOfGames"
            }
        }
        stage("Build") {
            steps {
                sh 'docker-compose build'
                // Tag the built image
                sh 'docker tag wog_flask_app:latest talvinisky1208/world_of_games:latest'
            }
        }
        stage("Run") {
            steps {
                sh 'docker-compose up -d'
                // Ensure services are up
                script {
                    sleep 15 // Adjust the sleep time as necessary
                }
            }
        }
        stage("Test") {
            steps {
                script {
                    try {
                        sh 'docker-compose exec -T flask_app python /app/tests/e2e.py'
                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'
                        throw e
                    }
                }
            }
        }
        stage("Finalize") {
            when {
                expression {
                    currentBuild.result == null || currentBuild.result == 'SUCCESS'
                }
            }
            steps {
                withCredentials([usernamePassword(credentialsId: 'DockerHub', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_ID')]) {
                    sh 'echo $DOCKER_PASSWORD | docker login -u $DOCKER_ID --password-stdin'
                    sh 'docker push talvinisky1208/world_of_games:latest'
                }
                sh 'docker-compose down; docker rmi $(docker images -q)'
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}
