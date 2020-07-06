#!/usr/bin/env groovy
pipeline {

    /*
     * Run everything on an existing agent configured with a label 'docker'.
     */
    agent {
        node {
            label 'docker-agent'
        }
    }

    stages {
        stage('Test') {
            steps {
                sh 'ls'
                sh 'curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py'
                sh 'python get-pip.py'
                sh 'pip install docker-compose'
                sh 'docker-compose --version'
                sh 'docker-compose build'
                sh 'docker-compose up'
                sh 'docker cp jnk_test:/home/python_API_testing/allure-results "/home/jenkins/workspace/jkfile_master/allure-results" '
            }
        }
    }

}

