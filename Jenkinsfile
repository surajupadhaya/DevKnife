pipeline {
    agent { label 'suru' }

    parameters {
        string(name: 'IMAGE_NAME', defaultValue: 'devknife', description: 'Name of the Docker image')
        string(name: 'CONT_NAME', defaultValue: 'devknife_container', description: 'Name of the Docker container')
    }

    stages {
        stage('check existing container'){
            steps{
                script{
                    sh "python3 main.py 4 ${IMAGE_NAME} ${CONT_NAME}"
                }
            }

        }
        stage('Check Existing Images') {
            steps {
                script {
                    sh "python3 main.py 0 ${IMAGE_NAME}"
                }
            }
        }

        stage('Build Image') {
            steps {
                script {
                    sh "python3 main.py 1 ${IMAGE_NAME}"
                }
            }
        }

        stage('Launch Container') {
            steps {
                script {
                    sh "python3 main.py 3 ${IMAGE_NAME} ${CONT_NAME}"
                }
            }
        }
    }
}