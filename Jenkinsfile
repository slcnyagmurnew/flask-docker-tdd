pipeline {
    agent any
    stages {
        stage('build') {
	    try {
		sh 'nc -vz 127.0.0.1 5000'
		echo 'Docker already up !'
	    }
	    catch (err) {
	 	echo 'Building started !'
		sh 'docker-compose up -d'
		throw err
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
