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
        stage("Push to DockerHub") {
            when {
                expression {
                    currentBuild.result == null || currentBuild.result == 'SUCCESS'
                }
            }
            steps {
                withCredentials([usernamePassword(credentialsId: 'DockerHub', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_ID')]) {
                    sh 'docker login -u $DOCKER_ID -p $DOCKER_PASSWORD'
                    sh 'docker tag wog_flask_app:latest talvinisky1208/world_of_games:latest'
                    sh 'docker push talvinisky1208/world_of_games:latest'
                }
            }
        }
    }
    post {
        always {
            script {
                // Stop and remove containers
                sh 'docker-compose down'
                // Remove all containers
                sh 'docker container prune -f'
                // Remove images safely
                def images = sh(script: 'docker images -q', returnStdout: true).trim()
                if (images) {
                    def imageList = images.split("\n")
                    imageList.each { image ->
                        sh "docker rmi --force ${image} || true"
                    }
                }
            }
            cleanWs()
        }
    }
}
