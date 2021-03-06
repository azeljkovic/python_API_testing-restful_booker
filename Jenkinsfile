#!/usr/bin/env groovy
pipeline {

    // Run everything on an existing agent configured with a label 'docker-agent'.

    agent {
        node {
            label 'docker-agent'
        }
    }

    stages {
        stage('Bild restful-booker') {
            steps {
                // Install pip
                sh 'curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py'
                sh 'python get-pip.py'
                // Install docker-compose
                sh 'pip install docker-compose'
                // Clone restful-booker repo
                sh 'git clone https://github.com/mwinteringham/restful-booker.git'
                // Start resrful-booker container
                sh 'cd restful-booker && docker-compose build'
                sh 'cd restful-booker && docker-compose up -d'
            }
        }

        stage('Test') {
            steps {
                // Run the tests container
                sh 'docker-compose build'
                sh 'docker-compose up'
                // Copy allure results to Jenkins host so the report can be generated
                sh 'docker cp restful_booker_test_container:/home/python_API_testing/allure-results "${WORKSPACE}/allure-results"'
            }
        }

        stage('Report') {
            steps {
                script {
                    allure([
                        includeProperties: false,
                        jdk: '',
                        properties: [],
                        reportBuildPolicy: 'ALWAYS',
                        results: [[path: 'target/allure-results']]
                        ])
                    }
                }
        }   
    }

}

