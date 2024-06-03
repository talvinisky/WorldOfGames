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
                sh 'docker tag wog_flask_app:latest talvinisky1208/world_of_games:latest'
            }
        }
        stage("Run") {
            steps {
                sh 'docker-compose up -d'

                script {
                    sleep 15
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
        stage("Push to DockerHub") {
            when {
                expression {
                    currentBuild.result == null || currentBuild.result == 'SUCCESS'
                }
            }
            steps {
                withCredentials([usernamePassword(credentialsId: 'DockerHub', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_ID')]) {
                    sh 'docker login -u $DOCKER_ID -p $DOCKER_PASSWORD'
                    sh 'docker push talvinisky1208/world_of_games:latest'
                }
            }
        }
    }
    post {
        always {
            script {
                sh 'docker-compose down'

                sh 'docker container prune -f'

                sh 'docker rmi $(docker images -q) --force || true'
            }
            cleanWs()
        }
    }
}
