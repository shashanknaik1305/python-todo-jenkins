pipeline {
    agent any

    tools {
        sonarQubeScanner 'SonarQubeScanner' 
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
                SONARQUBE = credentials('sonar-token')
            }
            steps {
                withSonarQubeEnv('MySonarQubeServer') {
                    // No need for additional parameters - sonar-project.properties will be used automatically
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
