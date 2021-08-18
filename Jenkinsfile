pipeline {
    agent any
	
    environment {
        RESULT = sh(script: 'docker inspect -f {{.State.Running}} tdd-web')
    }
	
    stages {
        stage('build') {
            steps {
		    script {
		    	try {
		        	sh 'nc -vz 127.0.0.1 5000'
		        	echo 'Docker already up !'
	            	}
	            	catch (err) {
	 	        	echo 'Building started !'
		        	sh 'docker-compose up -d'
	            	}
		    }
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
		script {
		    	try {
		        	sh 'nc -vz 127.0.0.1 32000'
		        	echo 'NO NEED FOR SLEEP !'
	            	}
	            	catch (err) {
	 	        	echo 'SLEEP REQUIRED !'
		        	sh 'sleep 60'
				echo 'Wait Completed !'
	            	}
		}
		sh 'docker exec tdd-web python3 -m pytest tests'
		echo 'Test Completed !'
	    }
	}
    }
}
