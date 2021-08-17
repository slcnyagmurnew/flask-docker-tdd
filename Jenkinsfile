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
		sh 'docker exec 8ac7 pip3 install pytest && docker exec 8ac7 python3 -m pytest tests'
		// echo 'cartcurt'
	    }
	}
    }
}
