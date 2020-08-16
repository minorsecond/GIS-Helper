pipeline {
    agent none
	options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
	    agent {
                docker {
                    image 'python:2-alpine'
		}
	    }
            steps {
                sh 'python -m py_compile gh.py gui.py'
            }
        }
	stage('Deliver') {
            agent {label 'CI-W10-Slave'}
            steps {
                sh 'dir'
            }
            post {
                success {
                    archiveArtifacts 'dist/gh'
                }
            }
        }
    }
}