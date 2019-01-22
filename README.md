# ChemTechHackathon 2019 - A XERVON CHALLANGE

![Gopher image](/documentation/logo_v1.png)


# ABOUT THE CHALLANGE



# THE TEAM
Our mind-blowing `extra cute crocodiles` - team

* Marcel
* Weiling
* Vasil
* Paul





# USED SOFTWARE

## AI Service
* python2.7, python3.6
* numpy
* skilearn
* numplot
* paho-mqtt

## WebUI Service
* NodeJS
* socket.io
* ejs templating engine
* couchdb
## HOSTING
* MQTT Broker
* Amazon Web Services (EC2 instance)

## ALEXA SKILL
* Alexa Skill Kit
* Amazon Lambda Functions (Python)



# USED HARDWARE

## Self-speaking alexa for voice notification
* RPI 3 (sd, powersupply, ethernet)
* Alexa Echo Dot V2
* 3.5mm Audio Cable

## Notification Light
* Arduino Nano
* ESP32 DevKit V1
* WS2813 12 LED Ring
* 10k resistor

## TOOLS
* soldering iron ts100
* hotglue
* cables, 2,54mm header
* 20x10cm@9mm wood
* solder bp-free



# SLIDES ? 
https://slides.com/beinggracie/deck-6#/



# FURTHER PROBLEM DESCRIPTION



# EXPLANATION CLASSIFIER

## SVM - SupportVectorMachine


## RNN - RecurrentNeuralNetwork




# EXPLANATION BACKEND

## COMMUNICATION BETWEEN [SOFTWARE-]COMPONENTS


# RUN THE WEBINTERFACE
The Webinterface is running on an AWS EC2 Instance `t2 nano`

* install NodeJS `sudo apt-get install nodejs npm -y`
* install MQTT `sudo apt-get install mosquitto mosquitto-clients`
* copy the `./src/data_visulizer/` folder to the EC2 using an  SFTP client `eg. Cyberduck,MobaXTerm`
* in the `data_visulizer` run `npm install` to install all packets
* to run the server run `node server.js` the server is listening on port `3014`


You can also run all scripts using the container service `docker`, you have to clone the folloing images:
* `docker pull node` - nodejs `[expose port 3014]`
* `docker pull eclipse-mosquitto` - mqtt broker `[expose port 1883]`
* `docker pull python` - python environment
You have to modify the `dockerfile` to install the python packages


# MQTT TOPICS
All components are communicates via the IOT Protocol MQTT, its based on a publish/subscriber modell.
The topics used in this Project are:

* `chemtechhack1234alexa` - Triggers the ALEXA Skill `[payload can be empty]`
* `chemtechhack1234light` - Triggers the lights the payload is `1` for a red light and. `0` for the blue light
* `chemtechhack1234hammer` - Starts the hammer simulation `[payload can be empty]`
* `chemtechhack1234unwucht` - Starts the unwicht simulation `[payload can be empty]`
* `chemtechhack1234` - Reports the result by the classifier
* `chemteckhack1234clear` - Clears the error, if the user mark error as unread `[payload can be empty]`


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
* download the RPI Image `Raspbian Stretch Lite` and write it to an `sd card` using `etcher - https://www.balena.io/etcher/`
* create an file called `ssh` in the `/boot partionion` on the sd card, to enable ssh
* connect the rpi to power and ethernet
* login to ssh with `pi@<PI_IP>` and the password `raspberry`
* type `sudo raspi-config` and select `advanced option->audio->force 3.5mm output`
* cut the 3.5mm audio-cable in half and strip of the isolation
*







# BUILD A REALWORLD-THING ? 
What we need to build a scalable product

## Hardware for realtime measurements
Using a fast dac to read out the vibration sensors:
https://hackaday.io/project/163069-using-red-pitaya-for-long-time-data-logging

https://www.ebay.de/itm/SX1276-868MHz-915MHz-ESP32-LoRa-Bluetooth-WIFI-Kit-IOT-Entwicklung-Tafel-AIP/142639274892?hash=item2135f69b8c:g:BUcAAOSwMQBaHDgZ:rk:1:pf:1

and for the communication some lora stuff to send only the error_messages:
https://www.antratek.de/lora-iot-kit?gclid=Cj0KCQiAm5viBRD4ARIsADGUT2554OXE1H2TQW_V9g6Gik1cN9DIoEMsH83lfYLLp12YNLRFspnj6AgaAveUEALw_wcB

maybe something to accelerate the AI
https://www.movidius.com

but i think its not nessessary if the measurement interval is only every minute, and samples 5seconds 

## Data, more Data

## Software







# IMAGES

## RESULT
## WEBINTERFACE
## ...

