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
		        sh 'docker exec pipeline-1_web pip3 install pytest && docker exec pipeline-1_web python3 -m pytest tests'
	        }
	    }
    }
}
