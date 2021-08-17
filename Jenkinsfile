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
		sh 'docker exec -i 8ac7 /bin/bash'
		sh 'python3 -m pytest tests/'
		sh 'exit'
	    }
	}
    }
}
