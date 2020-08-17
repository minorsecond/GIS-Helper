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
                bat 'conda env remove -y --name GIS-Helper'
                bat 'conda env create' // Build environment based on environment.yml
                bat 'conda activate GIS-Helper'
                bat 'conda install -y --file requirements.txt'
                bat 'pyinstaller --onefile gh-debug.spec'
            }
            post {
                success {
                    sh 'ls dist/gh'
                    archiveArtifacts 'dist/gh'
                }
                always {
                    cleanWs()
                }
            }
        }
    }
}