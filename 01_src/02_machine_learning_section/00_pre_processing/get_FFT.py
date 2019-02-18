import sys
import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft,ifft

csvFile = open(sys.argv[1], "rb")
reader = csv.reader(csvFile, delimiter=';')
fft_size = 248993


count = 0
value_of_row = []
value_of_time = []
for row in reader:
    count = count + 1
    row_c = 0
    if count == 3:
        for i in row:
            row_c = row_c +1
    print row_c
        #value_of_row.append(int(row[8].replace(",", "")))
        #value_of_time.append(int(row[5].replace(",", "")))

#print value_of_row

time_np = np.asarray(value_of_time[0:fft_size])
row_np = np.asarray(value_of_row[0:fft_size])

time_np_1 = time_np
row_np_1 = row_np
result = np.fft.rfft(row_np_1)

#print len(result)

#plt.plot(result, color='C0')
#plt.xlabel("Time")
#plt.ylabel("Amplitude")
#plt.show()



#print count
