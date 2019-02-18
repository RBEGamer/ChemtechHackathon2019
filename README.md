## ChemTechHackathon 2019 - A XERVON CHALLANGE

<img src="/03_logo/00_logo_v1.png" data-canonical-src="/03_logo/00_logo_v1.png" width="150" height="150" />


## ABOUT THE CHALLANGE



## THE TEAM
* [Marcel Ochsendorf](https://github.com/RBEGamer)
* [Weiling Xi](https://github.com/notagenius)
* Vasil
* Paul

## USED SOFTWARE

### AI Service
* python2.7, python3.6
* numpy
* sklearn
* pytorch
* csv
* numplot
* paho-mqtt

### WebUI Service
* NodeJS
* socket.io
* ejs templating engine
* couchdb

### Hosting
* MQTT Broker
* Amazon Web Services (EC2 instance)

### Alexa Skill
* Alexa Skill Kit
* Amazon Lambda Functions (Python)

## Used Hardware

### Self-speaking alexa for voice notification
* RPI 3 (sd, powersupply, ethernet)
* Alexa Echo Dot V2
* 3.5mm Audio Cable
* optocoupler PF817

### Notification Light
* [Arduino Nano](https://www.conrad.de/de/arduino-board-nano-atmega328-1172623.html?WT.mc_id=google_pla&WT.srch=1&ef_id=Cj0KCQiAvqDiBRDAARIsADWh5TdkGpHTU44qwLFKKNTgm5uaTho83g3jRuzOcssIlJPiwOhgq3lqE5UaAtITEALw_wcB:G:s&gclid=Cj0KCQiAvqDiBRDAARIsADWh5TdkGpHTU44qwLFKKNTgm5uaTho83g3jRuzOcssIlJPiwOhgq3lqE5UaAtITEALw_wcB&hk=SEM&insert_kz=VQ&s_kwcid=AL!222!3!293649793181!!!g!!)
* [ESP32 DevKit V1](https://www.bastelgarage.ch/wifi-lora-32-v2-sx1276-868mhz-mit-oled)
* [WS2813 12 LED Ring](https://www.seeedstudio.com/WS2813-Digital-RGB-LED-Ring-p-2871.html)
* 10k resistor

### Tools
* [soldering iron ts100](https://www.banggood.com/de/MINI-TS80-Digital-OLED-USB-Type-C-Programable-Soldering-Iron-Station-Solder-Tool-Built-in-STM32-Chip-p-1330060.html?gmcCountry=DE&currency=EUR&cur_warehouse=CN&createTmp=1&ID=554956&utm_source=googleshopping&utm_medium=cpc_union&utm_content=2zou&utm_campaign=ssc-de-de-all&gclid=Cj0KCQiAvqDiBRDAARIsADWh5TfJrIg0-jV-CLCHcV-Yc0rjw4NkFCJe-BkxnWlLEZpVYmOtDFpJ4CIaAuWqEALw_wcB)
* hotglue
* cables, 2,54mm header
* 20x10cm@9mm wood
* solder bp-free


## Pitch Slides 
[(online) Hackathon Version](https://slides.com/beinggracie/deck-6#/) 

[(pdf) Hackathon Version](/02_pitch/00_ECC_hackathon_slides.pdf)

[(online) Presentation Version](https://slides.com/beinggracie/deck-6-7#/) 

[(pdf) on site Presentaion Version](/02_pitch/01_ECC_on_site_slides.pdf)


## Futher Problem Description



## Explaination Classifier

### SVM - SupportVectorMachine


### RNN - RecurrentNeuralNetwork


## Explanation Backend

### Communitcation Between [Software-] Components


### MQTT Topics
All components are communicates via the IOT Protocol MQTT, its based on a publish/subscriber modell.
The topics used in this Project are:

* `chemtechhack1234alexa` - Triggers the ALEXA Skill `[payload can be empty]`
* `chemtechhack1234light` - Triggers the lights the payload is `1` for a red light and. `0` for the blue light
* `chemtechhack1234hammer` - Starts the hammer simulation `[payload can be empty]`
* `chemtechhack1234unwucht` - Starts the unwicht simulation `[payload can be empty]`
* `chemtechhack1234` - Reports the result by the classifier
* `chemteckhack1234clear` - Clears the error, if the user mark error as unread `[payload can be empty]`


The result from the classifier contains the type of error, time and the location on the machine:
`Topic:chemtechhack1234 Payload:{'error':[2,3,4],'location':'right','time':'14:39'}



## Software Setup

### Run the Webinterface
The Webinterface is running on an AWS EC2 Instance `t2 nano`

* install NodeJS `sudo apt-get install nodejs npm -y`
* install MQTT `sudo apt-get install mosquitto mosquitto-clients`
* copy the `./01_src/01_notification_system/data_visulizer_webinterface/
` folder to the EC2 using an  SFTP client `eg. Cyberduck,MobaXTerm`
* in the `data_visulizer` run `npm install` to install all packets
* to run the server run `node server.js` the server is listening on port `3014`

You can also run all scripts using the container service `docker`, you have to clone the folloing images:
* [`docker pull node`](https://hub.docker.com/_/node/) - nodejs `[expose port 3014]`
* [`docker pull eclipse-mosquitto`](https://hub.docker.com/_/eclipse-mosquitto) - mqtt broker `[expose port 1883]`
* [`docker pull python`](https://hub.docker.com/r/fastgenomics/sklearn/) - python environment
You have to modify the `dockerfile` to install the python packages


### Run The Classifier

* `install python`
* `pip instal paho-mqtt`
* `pip install -U scikit-learn`


## Build the Hardware

### Building the Notification Light
* flash the `./src/esp32_mqtt_client_for_light` to the ESP32 DevKit by using the Arduino IDE
* flash the `./src/notification_light` to the Arduino Nano by using the Arduino IDE
* connect  the `ESP32 gpio 2`to the `Arduino Nano Pin D3`
* connect  the `ESP32 gnd`to the `Arduino Nano gnd`
* connect  the `ESP32 5V`to the `Arduino Nano 5V`
* connect  the `Arduino Nano gnd`to the `WS2813 gnd`
* connect  the `Arduino Nano 5v`to the `WS2813 5v`
* connect  the `Arduino Nano D2`to the `WS2813 din`

### Build the Self Speaking Alexa
* download the RPI Image [`Raspbian Stretch Lite`](https://www.raspberrypi.org/downloads/raspbian/) and write it to an `sd card` using [etcher](https://www.balena.io/etcher/)
* create an file called `ssh` in the `/boot partionion` on the sd card, to enable ssh
* connect the rpi to power and ethernet
* login to ssh with `pi@<PI_IP>` and the password `raspberry`
* type `sudo raspi-config` and select `advanced option->audio->force 3.5mm output`
* cut the 3.5mm audio-cable in half and strip of the isolation
*


## Build a realworld-thing? 
What we need to build a scalable product

### Hardware for realtime measurements
Using a fast dac to read out the [vibration sensors](https://german.alibaba.com/product-detail/cz9300-oil-water-piezo-sensor-with-armoured-cable-60685810280.html)
[using red pitaya for sensor collection](https://hackaday.io/project/163069-using-red-pitaya-for-long-time-data-logging)
using the [`pyrpl`](https://pyrpl.readthedocs.io/en/latest/) python package its possible to collect data `up to 50msamples/s`

maybe something to accelerate the AI
[movidius compute stick](https://www.movidius.com)
but i think its not nessessary if the measurement interval is only every minute, and samples 5seconds 

### Data, more Data

### Software


## Images

### Result
### Webinterface

#### Landing Pages
![Gopher image](/00_doc_support/00_error_dashboard.png)

#### START A SIMULATION
![Gopher image](/00_doc_support/00_landing_page.png)

#### ERROR REPORT PAGE
![Gopher image](/00_doc_support/00_simulation_dashboard.png)

### TEST STAND
![Gopher image](/00_doc_support/01_diy_schaft.jpg)


## ...

