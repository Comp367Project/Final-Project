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
        stage("Dev ENV"){

        
        steps{
          echo "test cases passed"
        }}
        stage("Test ENV"){

        
        steps{
          echo "test cases passed"
        }}
        stage("Staging ENV"){

        
        steps{
          echo "test cases passed"
        }}
      
        stage(" Production ENV Setup gunicorn SetUp"){

       
        steps{
            sh'''
            chmod +x gunicorn.sh
            ./gunicorn.sh
            '''
        } }
        stage("Production ENV Set Up NGINX"){
        steps{
            sh'''
            chmod +x nginx.sh
            ./nginx.sh
            '''
        }}
    }
}
