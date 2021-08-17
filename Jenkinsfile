pipeline {
    agent any
	
    stages {
        stage('build') {
            steps {
                sh 'docker-compose up -d'
            }
        }
	stage('test') {
	    steps {
		echo 'testing application'	
	    }
	}
    }
}
