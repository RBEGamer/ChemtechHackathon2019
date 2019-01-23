import sys
import csv
import matplotlib.pyplot as plt
import numpy as np

csvFile = open(sys.argv[1], "rb")
reader = csv.reader(csvFile, delimiter=';')

count = 0
value_of_row = []
value_of_time = []
for row in reader:
    count = count + 1
    if count != 1:
        value_of_row.append(row[8])
file_write = open("./result/"+"0" + sys.argv[2] + "_Raw_" + sys.argv[1][0:-4] + "_" + str(count-1) + "_.csv","w+")
file_write.write(sys.argv[2]+"\n")
file_write.write(sys.argv[3]+"\n")
for i in value_of_row:
    if i != '':
        i = float(i.replace(",","."))
        file_write.write(str(i) + "\n")
file_write.close()

print count

