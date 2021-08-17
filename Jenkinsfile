pipeline {
    agent any
	
    stages {
        stage('build') {
            steps {
                sh 'docker ps -v $(which docker):/usr/bin/docker --privileged'
            }
        }
	stage('test') {
	    steps {
		echo 'testing application'	
	    }
	}
    }
}
