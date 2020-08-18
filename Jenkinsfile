pipeline {
    agent none
	options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Test') {
            agent {label 'CI-W10-Slave'}
            bat 'pytest'
        }

	    stage('Deliver') {
            agent {label 'CI-W10-Slave'}
            environment {
                CONDA_DLL_SEARCH_MODIFICATION_ENABLE=1
            }
            steps {
                bat 'conda env create' // Build environment based on environment.yml
                bat 'conda activate GIS-Helper'
                bat 'c:\\Users\\Ross\\anaconda3\\envs\\GIS-Helper\\Scripts\\pyinstaller --onefile gh-debug.spec'
                //bat 'move matplotlibrc dist\\gh\\'
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