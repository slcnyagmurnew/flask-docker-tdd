def AGENT_LABEL = null
node('master') {
    stage('scm') {
	//steps {
	//    properties([gitLabConnection('your-gitlab-connection-name')])
        //    node {
	//        checkout([$class: 'GitSCM', branches: [[name: '*/dev' ]],
	//        userRemoteConfigs: [[url: 'https://github.com/slcnyagmurnew/flask-docker-tdd.git']]])
	        // checkout scm // Jenkins will clone the appropriate git branch, no env vars needed
	//    }
	    
        //}
        checkout scm
	if (env.BRANCH_NAME == 'master') {
            AGENT_LABEL = "prod"3
	    echo 'masterdeyim'
        } else {
            AGENT_LABEL = "dev"
	    echo 'devdeyim'
	    echo AGENT_LABEL
        }
    }
}
pipeline {
    agent {
	label '${AGENT_LABEL}'
    }
    stages {
        stage('build') {
	    steps {
		echo "Running in ${AGENT_LABEL}"
		script {
		    try {
		        sh 'nc -vz 127.0.0.1 5000'
		        echo 'Docker already up !'
	            }
	            catch (err) {
	 	        echo 'Building started !'
		        sh 'docker-compose up -d'
		        // throw err
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
		script {
		    try {
		        sh 'nc -vz 127.0.0.1 32000'
			sh 'sleep 30'
	            }
	            catch (err) {
	 	        echo 'Sleep required, wait a moment..'
			sh 'sleep 60'
	            }
		    echo 'Wait Completed !'
		}
		sh 'docker exec tdd-web python3 -m pytest tests'
		echo 'Test Passed !'
	    }
	}
    }
}
