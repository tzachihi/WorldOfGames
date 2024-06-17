pipeline {
    agent any

    stages {
        stage('ChcekOut') {
            steps {
               git url: 'https://github.com/tzachihi/WorldOfGames.git' , branch: 'master'
            }
        }
        stage('Build') {
            steps {
               sh 'docker build -t tzachihi/maingame:0.1 .'
            }
        }
        stage('run') {
            steps {
               sh 'docker run -d --name game -p 5000:5000 tzachihi/maingame:0.1 '
            }
        }
        stage('test') {
            steps {
               sh 'docker exec -d game python e2e.py '
            }
        }
    }
}
