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
                sh 'c/Users/Ross/miniconda3/condabin/conda.bat env remove --name GIS-Helper'
                sh 'c/Users/Ross/miniconda3/condabin/conda.bat GIS-Helper python=3.8'
                sh 'c/Users/Ross/miniconda3/condabin/conda.bat activate GIS-Helper'
                sh 'c/Users/Ross/miniconda3/condabin/conda.bat install --file requirements.txt'
            }
            post {
                success {
                    archiveArtifacts 'dist/gh'
                }
            }
        }
    }
}