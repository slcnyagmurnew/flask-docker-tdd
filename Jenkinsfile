pipeline {
    agent any
	
    stages {
        stage('build') {
            steps {
                sh 'docker-compose -v'
            }
        }
	stage('test') {
	    steps {
		echo 'testing application'	
	    }
	}
    }
}
