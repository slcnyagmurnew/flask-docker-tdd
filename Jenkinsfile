pipeline {
    agent any
	
    environment {
        RESULT = sh(script: 'docker inspect -f {{.State.Running}} tdd-web')
    }
	
    stages {
        stage('build') {
            steps {
		    script {
			    if(sh(script: 'docker inspect -f {{.State.Running}} tdd-web')) {
			    	echo 'Docker Container UP !'
			    }
			    else {
			    	// sh 'docker-compose up -d'
				echo 'ZAAAA'
				echo RESULT
			    }
		    }
		// sh 'docker-compose up -d'
		// echo 'kekeke'
            }
        }
	stage('preparation-test') {
	    steps {
		sh 'docker exec tdd-web pip3 install pytest'
		// sh 'sleep 20'
		echo 'Pytest Installed !'
	    }
	}
	stage('test') {
	    steps {
		sh 'sleep 60'
		echo 'Wait Completed !'
		sh 'docker exec tdd-web python3 -m pytest tests'
		echo 'Waiting for Second Test Stage'
		sh 'sleep 10'
		sh 'docker exec tdd-web python3 -m pytest tests'
		echo 'Test Completed !'
	    }
	}
    }
}
