import numpy as np
import csv
import math
import matplotlib.pyplot as plt
from scipy import interpolate

counter = 0
data = []
aux = []
with open('dataset_ATD_PL7.csv', 'rb') as csvfile:
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

#media da serie total
media = np.mean(values)
print("media: %s" % (media))

#desvio padrao da serie total
dpadrao = np.std(values)
print("desvio padrao: %s" % (dpadrao))

# media e desvio padrao mensal
array_medias = []
array_desviop = []
n=0
for i in range (12):
    if i%2 == 0:
        array_medias.append(np.mean(values[n:n+29]))
        array_desviop.append(np.std(values[n:n+29]))

        n+=29
    elif i == 1:
        array_medias.append(np.mean(values[n:n+27]))
        array_desviop.append(np.std(values[n:n+27]))

        n+=27
    else:
        array_medias.append(np.mean(values[n:n+30]))
        array_desviop.append(np.std(values[n:n+30]))

        n+=30


#media trimestral
mt = []
mt.append(np.mean(values[0:89]))
mt.append(np.mean(values[90:180]))
mt.append(np.mean(values[181:272]))
mt.append(np.mean(values[273:364]))

aux_mt = np.array(mt)
#print(aux_mt)
mt_value = np.mean(aux_mt)
print("media trimestral: %s" % (mt_value))

#dp trimestral
dpt = []
dpt.append(np.std(values[0:89]))
dpt.append(np.std(values[90:180]))
dpt.append(np.std(values[181:272]))
dpt.append(np.std(values[273:364]))

aux_dpt = np.array(dpt)
#print(aux_dpt)
dpt_value = np.mean(aux_dpt)
print("desvio padrao trimestral: %s" % (dpt_value))

# media semestral
ms = []
ms.append(np.mean(values[0:180]))
ms.append(np.mean(values[181:364]))
aux_ms = np.array(ms)
#print(aux_ms)
ms_value = np.mean(aux_ms)
print("media semestral: %s" % (ms_value))

#dp semestral
dps = []
dps.append(np.std(values[0:180]))
dps.append(np.std(values[181:364]))
aux_dps = np.array(dps)
#print(aux_ms)
dps_value = np.mean(aux_dps)
print("desvio padrao semestral: %s" % (dps_value))

#outliers
values_outliers = np.copy(values)
print("vo: ",values_outliers)

for i in range(len(array_medias)):
    for j in range(len(values_outliers)):
        if (abs(values_outliers[j]-array_medias[i])>3*array_desviop[i]):
            values_outliers[j] = array_medias[i]+ 2.5*array_desviop[i]
        else:
            values_outliers[j] = array_medias[i]- 2.5*array_desviop[i]






'''


#mostra grafico sem outliers
plt.figure('DataSet Graph\n')
plt.title('DataSet Graph sem Outliers\n')
lines = plt.plot(values)
plt.setp(lines, 'color', 'r', 'linewidth', 1.0)
xmarks=[i for i in range(0,364+1,15)]
plt.xticks(xmarks)
plt.axis([0, 370, 0, 40])
plt.ylabel('Samples\n')
plt.xlabel('\nNumber of Samples')
plt.show()
'''
'''
#mostra grafico com outliers
plt.figure('DataSet Graph\n')
plt.title('DataSet Graph com Outliers\n')
lines = plt.plot(values_outliers)
plt.setp(lines, 'color', 'r', 'linewidth', 1.0)
xmarks=[i for i in range(0,364+1,15)]
plt.xticks(xmarks)
plt.axis([0, 370, 0, 40])
plt.ylabel('Samples\n')
plt.xlabel('\nNumber of Samples')
plt.show()
'''



