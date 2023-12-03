pipeline {
    agent any
    stages {
        stage('Execute Python Script') {
            steps {
                script {
                    def folderPath = "C:/Users/57310/Documents/TESIS/forms-script"
                    def pythonScript = "app.py"
                    
                    while (true) {
                        bat "cd ${folderPath} && C:/Users/57310/AppData/Local/Programs/Python/Python312/python.exe ${pythonScript}"
                        sleep time: 60, unit: 'SECONDS'
                    }
                }
            }
        }
    }
}
