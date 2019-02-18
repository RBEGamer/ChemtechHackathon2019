import sys
import csv
import numpy as np
from sklearn import datasets 
from sklearn.metrics import confusion_matrix 
from sklearn.model_selection import train_test_split 
import pickle
import torch.utils.data as Data

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
            #if label != 3:
            #    label = 0
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


import torch
from torch import nn
import torchvision.datasets as dsets
import torchvision.transforms as transforms
import matplotlib.pyplot as plt


EPOCH = 10
BATCH_SIZE = 1
TIME_STEP = 1
INPUT_SIZE = 850
LR = 0.01

train_tensor = torch.FloatTensor(X_train)
train_label_tensor = torch.LongTensor(y_train)
test_x = torch.FloatTensor(X_test)
test_y = np.asarray(y_test)

torch_dataset = Data.TensorDataset(train_tensor, train_label_tensor)

train_loader = torch.utils.data.DataLoader(dataset=torch_dataset, batch_size=BATCH_SIZE, shuffle=True)


class RNN(nn.Module):
    def __init__(self):
        super(RNN, self).__init__()

        self.rnn = nn.LSTM(
            input_size=INPUT_SIZE,
            hidden_size=850,
            num_layers=1,
            batch_first=True,
        )

        self.out = nn.Linear(850, 850)

    def forward(self, x):
        r_out, (h_n, h_c) = self.rnn(x, None)
        out = self.out(r_out[:, -1, :])
        return out

rnn = RNN()
print(rnn)

optimizer = torch.optim.Adam(rnn.parameters(), lr=LR)
loss_func = nn.CrossEntropyLoss()

for epoch in range(EPOCH):
    for step, (b_x, b_y) in enumerate(train_loader):
        b_x = b_x.view(-1, TIME_STEP, INPUT_SIZE)

        output = rnn(b_x)
        loss = loss_func(output, b_y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if step % 50 == 0:
            test_x = test_x.view(-1, TIME_STEP, INPUT_SIZE)
            test_output = rnn(test_x)
            pred_y = torch.max(test_output, 1)[1].data.numpy()
            accuracy = float((pred_y == test_y).astype(int).sum()) / float(test_y.size)
            print('Epoch: ', epoch, '| train loss: %.4f' % loss.data.numpy(), '| test accuracy: %.2f' % accuracy)

test_output = rnn(test_x[:10].view(-1, TIME_STEP, INPUT_SIZE))
pred_y = torch.max(test_output, 1)[1].data.numpy()
print(pred_y, 'prediction number')
print(test_y, 'real number')

