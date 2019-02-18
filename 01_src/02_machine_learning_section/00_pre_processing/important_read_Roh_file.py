import sys
import csv
import numpy as np
from sklearn import datasets 
from sklearn.metrics import confusion_matrix 
from sklearn.model_selection import train_test_split 
import pickle


step_size = 248993
maxlism = 850

features = []
labels = []

def my_maxes(maxlism_in, feature_in):
    np_in = np.asarray(feature_in)
    np_out = np_in[sorted(np.argsort(np_in)[-1*maxlism_in:])]
    return np_out.tolist()


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
            single_feature = my_maxes(maxlism, single_feature)
            features.append(single_feature)
            labels.append(label)
            single_feature = []
        count = count + 1
print labels

X = features
y = labels 
  
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0) 
  
from sklearn.svm import SVC 
svm_model_linear = SVC(kernel = 'linear', C = 1).fit(X_train, y_train) 
filename = 'Hammer_svm__model.sav'
pickle.dump(svm_model_linear, open(filename, 'wb'))

svm_predictions = svm_model_linear.predict(X_test) 
loaded_model = pickle.load(open('Hammer_svm__model.sav', 'rb'))
result = loaded_model.score(X_test, y_test)
print "result"
print result


# model accuracy for X_test   
accuracy = svm_model_linear.score(X_test, y_test) 
print accuracy
 
# creating a confusion matrix 
cm = confusion_matrix(y_test, svm_predictions) 
print cm
