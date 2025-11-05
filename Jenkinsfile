pipeline {
    agent any

    tools {
        sonarScanner 'SonarScanner' // same name as configured in Jenkins Tools
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/shashanknaik1305/python-todo-jenkins.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('SonarQube Analysis') {
            environment {
                SONARQUBE = credentials('sonarqube-token') // Jenkins credential ID you created
            }
            steps {
                withSonarQubeEnv('MySonarQubeServer') {
                    sh 'sonar-scanner -Dsonar.login=$SONARQUBE'
                }
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 1, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }
}
