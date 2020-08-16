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
                sh '/c/Users/Ross/miniconda3/condabin/conda.bat env remove --name GIS-Helper'
                sh '/c/Users/Ross/miniconda3/condabin/conda.bat create -y --name GIS-Helper python=3.8'
                sh '/c/Users/Ross/miniconda3/condabin/conda.bat activate GIS-Helper'
                sh '/c/Users/Ross/miniconda3/condabin/conda.bat install -y --file requirements.txt'
                sh '/c/Users/Ross/miniconda3/Scripts/pyinstaller gh-debug.spec'
            }
            post {
                success {
                    sh 'ls'
                    archiveArtifacts 'dist/gh'
                }
            }
        }
    }
}