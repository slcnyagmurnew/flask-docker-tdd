pipeline {
    agent any
    environment {
        // result = sh(script: 'docker inspect -f {{.State.Running}} tdd-web')
	result = sh(script: 'nc -vz 127.0.0.1 5000')
    }
    stages {
        stage('build') {
            steps {
		echo result
		sh 'type result'
		script {
		    if(result == true) {
			echo 'selam'
		    }
		    else {
			sh 'docker-compose up -d'
		    }
		}
	    }
        }
	stage('preparation-test') {
	    steps {
		sh 'docker exec tdd-web pip3 install pytest'
	    }
	}
	stage('test') {
	    steps {
		sh 'sleep 60'
		echo 'Wait Completed !'
		sh 'docker exec tdd-web python3 -m pytest tests'
		echo 'Test Passed !'
	    }
	}
    }
}
