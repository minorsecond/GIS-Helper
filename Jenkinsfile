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
            //agent {
            //    docker {
            //        image 'cdrx/pyinstaller-windows'
            //    }
            //}
            agent {label 'master'}
            steps {
                sh 'ls $(pwd)'
                sh 'docker run -v "$(pwd):/src/" cdrx/pyinstaller-windows:latest "ls -alh"'
            }
            post {
                success {
                    archiveArtifacts 'dist/gh'
                }
            }
        }
    }
}