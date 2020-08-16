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
            agent {
                docker {
                    image 'cdrx/pyinstaller-windows:latest'
                }
            }
            steps {
                sh 'pyinstaller --onefile gh-debug.spec'
            }
            post {
                success {
                    archiveArtifacts 'dist/gh'
                }
            }
        }
    }
}