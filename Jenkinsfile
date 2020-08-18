pipeline {
    agent none
	options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build Environment') {
            agent {label 'CI-W10-Slave'}
            environment {
                CONDA_DLL_SEARCH_MODIFICATION_ENABLE=1
            }
            bat 'conda env create'  // Build environment based on environment.yml
            bat 'conda activate GIS-Helper'
        }
        stage('Test') {
            agent {label 'CI-W10-Slave'}
            steps {
                bat 'c:\\Users\\Ross\\anaconda3\\envs\\GIS-Helper\\Scripts\\pytest --junitxml results.xml'
            }
            post {
                failure {
                    bat 'conda env remove -y --name GIS-Helper'
                    bat 'rmdir /Q /S c:\\Users\\Ross\\anaconda3\\envs\\GIS-Helper'  // Make sure environment is fully gone
                    cleanWs()
                }
            }
        }

	    stage('Deliver') {
            agent {label 'CI-W10-Slave'}
            steps {
                bat 'c:\\Users\\Ross\\anaconda3\\envs\\GIS-Helper\\Scripts\\pyinstaller --onefile gh-debug.spec'
            }
            post {
                success {
                    archiveArtifacts 'dist/gh/**/**'
                }
                cleanup {
                    bat 'conda env remove -y --name GIS-Helper'
                    bat 'rmdir /Q /S c:\\Users\\Ross\\anaconda3\\envs\\GIS-Helper'  // Make sure environment is fully gone
                    cleanWs()
                }
            }
        }
    }
}