pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'
    }

    stages {
        stage("Checkout Code") {
            steps {
                checkout scm
            }
        }
    }

    stages {
        stage("Extract data.py") {
            bat "${env.PYTHON} extract_data.py"
        }
    }
}