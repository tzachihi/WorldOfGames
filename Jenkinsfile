pipeline {
    agent any
    stages {
        stage('Git Checkout') {
            steps {
                git 'https://github.com/tzachihi/WorldOfGames.git'
            }
        }
        stage('Build image') {
             /* This builds the actual image; synonymous to
              * docker build on the command line */
            steps {
             sh 'docker build -t tzachihi/maingame:0.1 .'
            }
        }
        stage('Run image') {
            steps {
             sh 'docker run -d --name game -p 5000:5000 tzachihi/maingame:0.1'
            }
        }
         stage('Test MainGame') {
            steps {
             sh 'docker exec -d game python e2e.py'
            }
        }

    }
}
