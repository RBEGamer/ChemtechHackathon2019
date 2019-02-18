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


'''

def on_connect(client, userdata, flags, rc):
   print("Connected with result code " + str(rc))    
   client.subscribe("chemtechhack1234hammer")
   
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    client.publish("chemtechhack1234","{'error':[2,3,4],'location':'right','time':'14:39'}")
    client.publish("chemtechhack1234alexa","0")
    client.publish("chemtechhack1234light","0")
'''


def my_maxes(maxlism_in, feature_in):
    np_in = np.asarray(feature_in)
    np_out = np_in[sorted(np.argsort(np_in)[-1*maxlism_in:])]
    return np_out.tolist()


def my_predic(data_in):
    svm_model_linear = pickle.load(open('Hammer_svm__model_multiclass.sav', 'rb'))
    svm_prediction = svm_model_linear.predict(data_in)
    return svm_prediction



for i in range(len(sys.argv)-1):
    csvFile = open(sys.argv[i+1], "rb")
    reader = csv.reader(csvFile)
    count = 0
    single_feature = []
    label = 0
    sensor = "S0"
    count2 = 0
    for row in reader:
        if count!=1 and float(row[0]) >= 50:
            count2 = count2 + 1
        if count == 0:
            label = int(row[0])
            if label != 3:
                label = 0
        elif count == 1:
            sensor = row
        elif (count-1) % step_size != 0:
            single_feature.append(float(row[0]))
        elif (count-1) % step_size == 0:
            single_feature.append(float(row[0]))
            features = []
            features.append(my_maxes(maxlism, single_feature))
            result = my_predic(features)
            #true
            if result > 0:
                print "case: "+str(result)+" detected!"
                print "client on"
                #client = mqtt.Client()
                #client.on_connect = on_connect
                #client.on_message = on_message
                #client.connect("test.mosquitto.org", 1883, 60)
            if result == 0:
                print "case: no detection"
        count = count + 1


#client.loop_forever()
