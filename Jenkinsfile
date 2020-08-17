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
            environment {
                CONDA_DLL_SEARCH_MODIFICATION_ENABLE=1
            }
            steps {
                bat 'conda env remove -y --name GIS-Helper'
                bat 'conda env create' // Build environment based on environment.yml
                bat 'conda activate GIS-Helper'
                bat 'c:\\Users\\Ross\\anaconda3\\envs\\GIS-Helper\\Scripts\\pyinstaller --onefile gh-debug.spec'
            }
            post {
                success {
                    sh 'ls'
                    archiveArtifacts 'dist/gh/**/*.*'
                }
                cleanup {
                    cleanWs()
                }
            }
        }
    }
}