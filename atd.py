import numpy as np
import csv
import math
import matplotlib.pyplot as plt
from scipy import interpolate


counter = 0
data = []
aux = []
with open('dataset_ATD_PL5.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in spamreader:
        if counter != 0:
            data.append([row[0],float(row[1])])
            aux.append(float(row[1]))
        counter = counter+1 

values = np.array(aux)

#cria uma matriz que poe a True se nao for nan, e a False se for
ok = -np.isnan(values)
#cria uma matriz com numeros de 0 a 364
xp = ok.ravel().nonzero()[0]
fp = values[-np.isnan(values)]
x  = np.isnan(values).ravel().nonzero()[0]
#interpolacao
values[np.isnan(values)] = np.interp(x, xp, fp)


#mostra grafico
plt.figure('DataSet Graph\n')
plt.title('DataSet Graph\n')
lines = plt.plot(values)
plt.setp(lines, 'color', 'r', 'linewidth', 1.0)
xmarks=[i for i in range(0,364+1,15)]
plt.xticks(xmarks)
plt.axis([0, 370, 0, 40])
plt.ylabel('Samples\n')
plt.xlabel('\nNumber of Samples')
plt.show()


