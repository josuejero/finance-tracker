pipeline {
    agent any
    environment {
        GOOGLE_PROJECT_ID = credentials('google-project-id')
        OAUTH_CLIENT_ID = credentials('oauth-client-id')
        OAUTH_CLIENT_SECRET = credentials('oauth-client-secret')
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t gcr.io/$GOOGLE_PROJECT_ID/finance-tracker:$BUILD_TAG .'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest tests/'
            }
        }
        stage('Deploy') {
            steps {
                sh 'kubectl apply -f k8s/deployment-prod.yaml'
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: '**/target/*.jar', allowEmptyArchive: true
            junit '**/target/test-reports/*.xml'
        }
    }
}
