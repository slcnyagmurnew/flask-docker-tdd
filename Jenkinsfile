pipeline {
    agent any
	
    stages {
        stage('build') {
            steps {
                sh 'bash setup.sh'
		sh 'cd Project/flask-docker-tdd && docker-compose up -d'
            }
        }
	stage('test') {
	    steps {
		sh 'docker exec pipelinedeneme_web_1 pip3 install pytest && docker exec pipelinedeneme_web_1 python3 -m pytest tests'
		echo 'cartcurt'
	    }
	}
    }
}
