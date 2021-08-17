pipeline {
    agent any
	
    stages {
        stage('build') {
            steps {
                sh 'docker -v'
            }
        }
	stage('test') {
	    steps {
		echo 'testing application'	
	    }
	}
    }
}
