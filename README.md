# Python-jenkins-automation (Pipeline Script/Public Repo)

In this Project i want to create different Jenkins-Jobs and Trigger them on different ways.
For this subproject i have crated a simple Python program (Python_basic_list.py) to run it with jenkins Pipeline-Skript.

## GitHub
1. Create a GitHub-Repository with a basic Python program.<b><br>NOTE : </b>Private Repos need authentication from Jenkins side.
## Jenkins
2. Create a Jenkins-Job (Pipeline Job) <br>
2.1 Add a Pipeline-Script :<br>You can create a Pipeline-Script in Jenkins or you can choose Pipeline-Script from SCM ( in ths case a jenkins file need to be present in your Git-Repository)<br>
You can create the Pipline with Jenkins-Pipeline-Syntax.

Example
````

  pipeline {
  agent any
  
      stages {
          stage('Checkout') {
              steps {
                  checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/rerdm/Python-selenium-jenkins-automation.git']])
              }
          }
          stage('Build'){
              steps {
                  git 'https://github.com/rerdm/Python-selenium-jenkins-automation.git'
                  bat 'python Python_basic_list.py'
              }
          }
           stage('Test'){
                steps {
                    echo 'Test has been executed successfully'
                }
               
           }
      }
  }

````

## Run The Pipeline

3. Now you can build the Programm and see the output in the console log from jenkins

########################################################################################################################

# Python-jenkins-automation with Pytest Integration and generating HTML Report (Pipeline Script/Public Repo)

In this Project i want to create different Jenkins-Jobs and Trigger them on different ways.
For this subproject i have crated a simple Python program (test_calculate.py) to run it with jenkins Pipeline-Skript.

## GitHub
1. Create a GitHub-Repository with a basic Python program.<b><br>NOTE : </b>Private Repos need authentication from Jenkins side.
## Jenkins
2. Create a Jenkins-Job (Pipeline Job) <br>
   2.1 Add a Pipeline-Script :<br>You can create a Pipeline-Script in Jenkins or you can choose Pipeline-Script from SCM ( in ths case a jenkins file need to be present in your Git-Repository)<br>
   You can create the Pipline with Jenkins-Pipeline-Syntax.

Example
````

pipeline {
  agent any
  
      stages {
          stage('Checkout') {
              steps {
                  checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/rerdm/Python-selenium-jenkins-automation.git']])
              }
          }
          stage('Build'){
              steps {
                  git 'https://github.com/rerdm/Python-selenium-jenkins-automation.git'
                  bat 'pytest test_calculate.py --html=reports/report.html'
              }
          }
           stage('Test'){
                steps {
                    echo 'Test has been executed successfully'
                }
               
           }
      }
  }


````

## Run The Pipeline

3. Now you can build the Programm and see the output in the console log from jenkins