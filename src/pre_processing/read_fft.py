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
    if count != 1:
        value_of_row.append(float(row[8].replace(",",".")))
        value_of_time.append(float(row[5].replace(",",".")))

time_np = np.asarray(value_of_time[0:fft_size])
row_np = np.asarray(value_of_row[0:fft_size])

time_np_1 = time_np
row_np_1 = row_np
result = np.fft.rfft(row_np_1)

print len(result)

#plt.plot(result, color='C0')
#plt.xlabel("Time")
#plt.ylabel("Amplitude")
#plt.show()



#print count
