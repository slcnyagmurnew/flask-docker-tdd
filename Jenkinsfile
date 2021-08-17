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
		sh 'docker exec 8ac7 pip3 install pytest && python3 -m pytest tests'
	    }
	}
    }
}
