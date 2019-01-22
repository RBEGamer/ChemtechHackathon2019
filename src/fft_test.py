#!bin/python


import csv


with open('~/Desktop/Hackathon/Messdaten_Hackaton/Test Case 1/S1_Roh_1.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader: