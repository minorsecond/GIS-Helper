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
                sh 'python -m py_compile client/python-client/modelportfolio/ModelPortfolioMain.py client/python-client/modelportfolio/restfulAPI.py client/python-client/modelportfolio/Utils.py'
            }
        }
	stage('Deliver') {
            agent {
                docker {
                    image 'cdrx/pyinstaller-windows:latest'
                }
            }
            steps {
                sh 'pyinstaller --onefile client/python-client/modelportfolio/ModelPortfolioMain.py'
            }
            post {
                success {
                    archiveArtifacts 'dist/ModelPortfolioMain'
                }
            }
        }
    }
}