pipeline {
    agent any
	
    stages {
        stage('build') {
            steps {
		        sh 'docker-compose down --volumes'
            }
        }
	    stage('test') {
	        steps {
		        // sh 'docker exec pipeline-1_web pip3 install pytest && docker exec pipeline-1_web python3 -m pytest tests'
			echo 'hello'
	        }
	    }
    }
}
