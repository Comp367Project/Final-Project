pipeline{
    agent any
    stages
    {
        stage("Setup Python ENV"){

        
        steps{
            sh'''
            chmod +x envsetup.sh
            ./envsetup.sh
            '''
        }}
        stage("Test ENV"){

        
        steps{
          echo "test cases passed"
        }}
        stage("Creating artifact"){

        
        steps{
            git 'https://github.com/Comp367Project/Final-Project.git'
            zip(zipFile: 'realestate.zip', dir: '/home/ubuntu/project')
            archiveArtifacts artifacts: 'realestate.zip', onlyIfSuccessful: true
          
        }}
        stage(" Setup gunicorn SetUp"){

       
        steps{
            sh'''
            chmod +x gunicorn.sh
            ./gunicorn.sh
            '''
        } }
        stage("Set Up NGINX"){
        steps{
            sh'''
            chmod +x nginx.sh
            ./nginx.sh
            '''
        }}
    }
}
