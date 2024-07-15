pipeline {

  environment {
    DOCKER_IMAGE = 'devraj112/to-dolist'
    registryCredential = 'dockerhub'
    KUBECONFIG_CREDENTIALS_ID = 'kubernetes'
  }

  agent any

  stages {

    stage('Checkout Source') {
      steps {
        checkout([$class: 'GitSCM', branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/whoisdevraj/Flask-TO-DOList.git']]])
      }
    }

    stage('Build & Push image') {
      steps {
        script {
          docker.withRegistry('https://hub.docker.com/repositories/devraj112', registryCredential) {
            def app = docker.build(DOCKER_IMAGE)
            app.push()
          }
        }
      }
    }

    stage('Deploying App to Kubernetes') {
      steps {
        script {
          withKubeConfig([credentialsId: KUBECONFIG_CREDENTIALS_ID]) {
            sh 'kubectl apply -f deploymentservice.yml'
          }
        }
      }
    }

  }

  post {
    always {
      cleanWs()
    }
  }
}
