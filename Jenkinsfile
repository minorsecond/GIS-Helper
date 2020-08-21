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
            steps {
                bat 'conda env create'  // Build environment based on environment.yml
                bat 'conda activate GIS-Helper'
                bat 'yes | c:\\Users\\Ross\\anaconda3\\envs\\GIS-Helper\\Scripts\\pip install -r requirements.txt'
            }
            post {
                failure {
                    bat 'conda env remove -y --name GIS-Helper'
                    bat 'rmdir /Q /S c:\\Users\\Ross\\anaconda3\\envs\\GIS-Helper'  // Make sure environment is fully gone
                    cleanWs()
                }
            }
        }
        stage('Test') {
            agent {label 'CI-W10-Slave'}
            environment {
                CONDA_DLL_SEARCH_MODIFICATION_ENABLE=1
            }
            steps {
                bat 'c:\\Users\\Ross\\anaconda3\\envs\\GIS-Helper\\Scripts\\pytest --cov=. --cov-report xml --junitxml results.xml'
            }
            //post {
            //    failure {
            //        bat 'conda env remove -y --name GIS-Helper'
            //        bat 'rmdir /Q /S c:\\Users\\Ross\\anaconda3\\envs\\GIS-Helper'  // Make sure environment is fully gone
            //        cleanWs()
            //    }
            }
        }

	    stage('Deliver') {
            agent {label 'CI-W10-Slave'}
            environment {
                CONDA_DLL_SEARCH_MODIFICATION_ENABLE=1
            }
            steps {
                bat 'c:\\Users\\Ross\\anaconda3\\envs\\GIS-Helper\\Scripts\\pyinstaller --onefile gh-debug.spec'
            }
            post {
                success {
                    archiveArtifacts 'dist/gh/**/**'
                }
                always {
                    junit 'results.xml'
                    cobertura coberturaReportFile: 'coverage.xml'
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