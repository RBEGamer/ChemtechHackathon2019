# ChemTechHackathon 2019 - A XERVON CHALLANGE

<img src="/documentation/logo_v1.png" data-canonical-src="/documentation/logo_v1.png" width="250" height="250" />


# ABOUT THE CHALLANGE



# THE TEAM
Our mind-blowing `extra cute crocodiles` - team

* [Marcel](https://github.com/RBEGamer)
* [Weiling Xi](https://github.com/notagenius)
* Vasil
* Paul




# USED SOFTWARE

## AI Service
* python2.7, python3.6
* numpy
* sklearn
* pytorch
* csv
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
* optocoupler PF817

## Notification Light
* [Arduino Nano](https://www.conrad.de/de/arduino-board-nano-atmega328-1172623.html?WT.mc_id=google_pla&WT.srch=1&ef_id=Cj0KCQiAvqDiBRDAARIsADWh5TdkGpHTU44qwLFKKNTgm5uaTho83g3jRuzOcssIlJPiwOhgq3lqE5UaAtITEALw_wcB:G:s&gclid=Cj0KCQiAvqDiBRDAARIsADWh5TdkGpHTU44qwLFKKNTgm5uaTho83g3jRuzOcssIlJPiwOhgq3lqE5UaAtITEALw_wcB&hk=SEM&insert_kz=VQ&s_kwcid=AL!222!3!293649793181!!!g!!)
* [ESP32 DevKit V1](https://www.bastelgarage.ch/wifi-lora-32-v2-sx1276-868mhz-mit-oled)
* [WS2813 12 LED Ring](https://www.seeedstudio.com/WS2813-Digital-RGB-LED-Ring-p-2871.html)
* 10k resistor

## TOOLS
* [soldering iron ts100](https://www.banggood.com/de/MINI-TS80-Digital-OLED-USB-Type-C-Programable-Soldering-Iron-Station-Solder-Tool-Built-in-STM32-Chip-p-1330060.html?gmcCountry=DE&currency=EUR&cur_warehouse=CN&createTmp=1&ID=554956&utm_source=googleshopping&utm_medium=cpc_union&utm_content=2zou&utm_campaign=ssc-de-de-all&gclid=Cj0KCQiAvqDiBRDAARIsADWh5TfJrIg0-jV-CLCHcV-Yc0rjw4NkFCJe-BkxnWlLEZpVYmOtDFpJ4CIaAuWqEALw_wcB)
* hotglue
* cables, 2,54mm header
* 20x10cm@9mm wood
* solder bp-free


# SLIDES ? 
[OH YES! HERE](https://slides.com/beinggracie/deck-6#/)


# FURTHER PROBLEM DESCRIPTION



# EXPLANATION CLASSIFIER

## SVM - SupportVectorMachine


## RNN - RecurrentNeuralNetwork


# EXPLANATION BACKEND

## COMMUNICATION BETWEEN [SOFTWARE-]COMPONENTS


## MQTT TOPICS
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







# SOFTWARE SETUP

## RUN THE WEBINTERFACE
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



## RUN THE CLASSIFIER


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
* download the RPI Image `Raspbian Stretch Lite` and write it to an `sd card` using [etcher](https://www.balena.io/etcher/)
* create an file called `ssh` in the `/boot partionion` on the sd card, to enable ssh
* connect the rpi to power and ethernet
* login to ssh with `pi@<PI_IP>` and the password `raspberry`
* type `sudo raspi-config` and select `advanced option->audio->force 3.5mm output`
* cut the 3.5mm audio-cable in half and strip of the isolation
*







# BUILD A REALWORLD-THING ? 
What we need to build a scalable product

## Hardware for realtime measurements
Using a fast dac to read out the [vibration sensors](https://german.alibaba.com/product-detail/cz9300-oil-water-piezo-sensor-with-armoured-cable-60685810280.html)
[using red pitaya for sensor collection](https://hackaday.io/project/163069-using-red-pitaya-for-long-time-data-logging)
using the [`pyrpl`](https://pyrpl.readthedocs.io/en/latest/) python package its possible to collect data `up to 50msamples/s`

maybe something to accelerate the AI
[movidius compute stick](https://www.movidius.com)
but i think its not nessessary if the measurement interval is only every minute, and samples 5seconds 

## Data, more Data

## Software







# IMAGES

## RESULT
## WEBINTERFACE

### LANDING PAGES
![Gopher image](/documentation/landing_page.png)

### START A SIMULATION
![Gopher image](/documentation/simulation_dashboard.png)

### ERROR REPORT PAGE
![Gopher image](/documentation/error_dashboard.png)



## ...

