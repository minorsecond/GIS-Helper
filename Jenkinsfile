pipeline {
    agent none
	options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build Environment') {
            agent {label 'CI-W10-Agent'}
            environment {
                CONDA_DLL_SEARCH_MODIFICATION_ENABLE=1
            }
            steps {
                bat """set PATH=%PATH%;C:\\Windows\\System32\\downlevel;'
                       call conda env create
                       call activate GIS-Helper
                       call conda info -a
                       call yes | pip install -r requirements.txt"""
            }
            post {
                failure {
                    bat 'conda env remove -y --name GIS-Helper'
                    bat 'rmdir /Q /S c:\\Users\\Ross\\miniconda3\\envs\\GIS-Helper'  // Make sure environment is fully gone
                    cleanWs()
                }
            }
        }
        stage('Test') {
            agent {label 'CI-W10-Agent'}
            environment {
                CONDA_DLL_SEARCH_MODIFICATION_ENABLE=1
            }
            steps {
                bat """call activate GIS-Helper
                       call conda env list
                       call pytest --cov=. --cov-report xml --junitxml results.xml"""
            }
            //post {
            //    failure {
            //        bat 'conda env remove -y --name GIS-Helper'
            //        bat 'rmdir /Q /S c:\\Users\\Ross\\miniconda3\\envs\\GIS-Helper'  // Make sure environment is fully gone
            //        cleanWs()
            //    }
            //}
        }

	    stage('Deliver') {
            agent {label 'CI-W10-Agent'}
            environment {
                CONDA_DLL_SEARCH_MODIFICATION_ENABLE=1
            }
            steps {
                bat """call activate GIS-Helper
                       call conda info --envs
                       call pyinstaller --onefile gh-release.spec"""
            }
            post {
                success {
                    archiveArtifacts 'dist/gh/**'
                }
                always {
                    junit 'results.xml'
                    cobertura coberturaReportFile: 'coverage.xml'
                }
                cleanup {
                    bat 'conda env remove -y --name GIS-Helper'
                    bat 'rmdir /Q /S c:\\Users\\Ross\\miniconda3\\envs\\GIS-Helper'  // Make sure environment is fully gone
                    cleanWs()
                }
            }
        }
    }
}