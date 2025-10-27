pipeline {
  agent any
  stages {
    stage('Checkout') { steps { checkout scm } }
    stage('Install') { steps { sh 'pip install -r requirements.txt' } }
    stage('Test') { steps { sh 'pytest --alluredir=allure-results' } }
    stage('Publish') { steps { echo 'Publish reports (configure Allure/Jenkins plugin)' } }
  }
}
