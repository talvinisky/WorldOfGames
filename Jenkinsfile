pipeline {
    agent any
    triggers {
        pollSCM '*/5 * * * *'
    }
    stages {
        stage('Checkout') {
            steps {
                git "https://github.com/talvinisky/WorldOfGames"
            }
        }
        stage("Build") {
            steps {
                sh 'docker-compose build'
            }
        }
        stage("Run") {
            steps {
                sh 'docker-compose up -d'
                // Ensure services are up
                script {
                    sleep 10 // Adjust the sleep time as necessary
                }
            }
        }
        stage("Test") {
            steps {
                sh 'docker-compose exec flask_app python /app/tests/e2e.py'
            }
        }
        stage("Finalize") {
            steps {
                withCredentials([usernamePassword(credentialsId: 'DockerHub', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_ID')]) {
                    sh 'docker login -u $DOCKER_ID -p $DOCKER_PASSWORD'
                    sh 'docker push khjomaa/world_of_games:latest'
                }
                sh 'docker-compose down; docker rmi $(docker images -q)'
            }
        }
    }
}
