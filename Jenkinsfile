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
		        sh 'docker exec tdd-web pip3 install pytest && docker exec tdd-db python3 -m pytest tests'
	        }
	    }
    }
}
