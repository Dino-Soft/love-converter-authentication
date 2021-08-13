# Authentication microservice for Love Converter

### **DEPLOYING THE API WITH DOCKER**
1. Install docker
2. In `/love-converter-authentication` directory, run: 
`docker build -t auth_flask:v0.1 .`
3. In `/love-converter-authentication/docker` define .env variables specified in the sample `.env.example`
4. In the same docker directory, run `docker-compose up`


### **DEPLOYING THE API LOCALLY**
1. Install MySQL database development files:

    `sudo apt install libmysqlclient-dev`


2. Check if it is successfully installed:  `mysql_config --version`
3. Create a virtual environment: `python3 -m venv .`
4. Install the venv requirements with pip3: `pip3 install -r requirements.txt`
5. Define the environment using a `.env` file from the sample file `~/env.local`
6. Connect to the sample MySQL database:
   - MySQL DB Name: `sql10430672`
   - MySQL User Name: `sql10430672`
   - MySQL Password: `apJbbscxAm`
   - MySQL Host Name: `sql10.freemysqlhosting.net`
   - Online view: [PHPMyAdmin](https://www.phpmyadmin.co/)