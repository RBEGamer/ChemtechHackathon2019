# ChemTechHackathon 2019 - XERON CHALLANGE




# ABOUT THE CHALLANGE



# THE TEAM
*
*
*
*





# TECH-STACK

* python2.7, python3.6
* numpy
* skilearn
* numplot
* paho-mqtt

* NodeJS
* MQTT Broker



* Amazon Web Services (EC2 instance)
* Alexa Skill Kit
* Amazon Lambda Functions (Python)


# FURTHER PROBLEM DESCRIPTION



# EXPLANATION CLASSIFIER


# EXPLANATION BACKEND



# RUN THE WEBINTERFACE
The Webinterface is running on an AWS EC2 Instance `t2 medium`

* install NodeJS `sudo apt-get install nodejs npm -y`
* install MQTT `sudo apt-get install mosquitto mosquitto-clients`
* copy the `./src/data_visulizer/` folder to the EC2 using an  SFTP client `eg. Cyberduck,MobaXTerm`
* in the `data_visulizer` run `npm install` to install all packets
* to run the server run `node server.js` the server is listening on port `3014`

# MQTT TOPICS
All components are communicates via the IOT Protocol MQTT, its based on a publish/subscriber modell.
The topics used in this Project are:

* `chemtechhack1234alexa` - Triggers the ALEXA Skill
* `chemtechhack1234light` - Triggers the lights the payload is `1` for a red light and. `0` for the blue light
* `chemtechhack1234hammer` - Starts the hammer simulation
* `chemtechhack1234unwucht` - Starts the unwicht simulation
* `chemtechhack1234` - Reports the result by the classifier
* `chemteckhack1234clear` - Clears the error


The result from the classifier contains the type of error, time and the location on the machine:
`Topic:chemtechhack1234
Payload:{'error':[2,3,4],'location':'right','time':'14:39'}
`



# RUN THE CLASSIFIER


* install python
* ...
* ...




# IMAGES

## RESULT
## WEBINTERFACE
## ...

