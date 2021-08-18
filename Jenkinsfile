pipeline {
    agent any
	
    stages {
        stage('build') {
            steps {
		sh 'docker-compose up -d'
		// echo 'kekeke'
            }
        }
	stage('preparation-test') {
	    steps {
		sh 'docker exec tdd-web pip3 install pytest'
	    }
	}
	stage('test-1') {
	    steps {
		sh 'sleep 60'
		echo 'Wait Completed !'
		sh 'docker exec tdd-web python3 -m pytest tests'
		echo 'Test Failed !'
	    }
	}
	stage('test-2') {
	     steps {
		sh 'docker exec tdd-web python3 -m pytest tests'
	        echo 'Test Passed !'
	    }
	}
    }
}
