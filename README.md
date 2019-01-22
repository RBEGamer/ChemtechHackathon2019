# ChemTechHackathon 2019 - XERON CHALLANGE




# ABOUT THE CHALLANGE



# THE TEAM
*
*
*
*





# USED SOFTWARE

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

# USED HARDWARE

* RPI 3 (sd, powersupply, ethernet)
* Arduino Nano
* ESP32 DevKit V1
* WS2813 12 LED Ring
* 3.5mm Audio Cable
* Alexa Echo Dot V2



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


You can also run all scripts using the container service `docker`, you have to clone the folloing images:
* `docker pull node` - nodejs
* `docker pull eclipse-mosquitto` - mqtt broker
* `docker pull python` - python environment

You have to modify the `dockerfile` to install the python packages


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
`Topic:chemtechhack1234 Payload:{'error':[2,3,4],'location':'right','time':'14:39'}`



# RUN THE CLASSIFIER


* `install python`
* `pip instal paho-mqtt`
* `pip install -U scikit-learn`





# BUILD THE HARDWARE

## BUILDING THE NOTIICATION LIGHT
* flash the `./src/esp32_mqtt_client_for_light` to the ESP32 DevKit by using the Arduino IDE
* flash the `./src/notification_light` to the Arduino Nano by using the Arduino IDE
* connect  the `ESP32 gpio 2`to the `Arduino Nano Pin D3`
* connect  the `ESP32 gnd`to the `Arduino Nano gnd`
* connect  the `ESP32 5V`to the `Arduino Nano 5V`
* connect  the `Arduino Nano gnd`to the `WS2813 gnd`
* connect  the `Arduino Nano 5v`to the `WS2813 5v`
* connect  the `Arduino Nano D2`to the `WS2813 din`

## BUILD THE SELF SPEAKING ALEXA

# IMAGES

## RESULT
## WEBINTERFACE
## ...

