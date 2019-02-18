import sys
import csv
import numpy as np
from sklearn import datasets 
from sklearn.metrics import confusion_matrix 
from sklearn.model_selection import train_test_split 
import pickle
import paho.mqtt.client as mqtt
step_size = 248993
maxlism = 850

features = []
labels = []

def on_connect(client, userdata, flags, rc):
   print("Connected with result code " + str(rc))    
   client.subscribe("chemtechhack1234hammer")
   
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    client.publish("chemtechhack1234","{'error':[2,3,4],'location':'right','time':'14:39'}")
    client.publish("chemtechhack1234alexa","0")
    client.publish("chemtechhack1234light","0")
    
    


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("test.mosquitto.org", 1883, 60)

def my_maxes(maxlism_in, feature_in):
    np_in = np.asarray(feature_in)
    np_out = np_in[sorted(np.argsort(np_in)[-1*maxlism_in:])]
    return np_out.tolist()


def my_predic(data_in):
    loaded_model = pickle.load(open('Hammer_svm__model.sav', 'rb'))
    data_in = my_maxes(maxlism, data_in)
    svm_predictions = svm_model_linear.predict(data_in)
    print svm_preditions


client.loop_forever()
