import numpy as np
import csv
import math
import matplotlib.pyplot as plt
from scipy import interpolate
from scipy import signal
import numpy.matlib


counter = 0
data = []
aux = []
times = []

with open('dataset_ATD_PL5.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in spamreader:
        if counter != 0:
            times.append(counter)
            data.append([row[0],float(row[1])])
            aux.append(float(row[1]))
        counter = counter+1 

values = np.array(aux)
times = np.array(times)
#cria uma matriz que poe a True se nao for nan, e a False se for
ok = ~np.isnan(values)
#cria uma matriz com numeros de 0 a 364
xp = ok.ravel().nonzero()[0]
fp = values[~np.isnan(values)]
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

values_outliers = np.copy(values)
#outliers mes a mes
for i in range(len(values_outliers)):
    if i < 31:
        if(abs(values[i]-array_medias[0]) > 3*array_desviop[0]):
            if(values[i] > array_medias[j]):
                values_outliers[i] = array_medias[0]+ 2.5*array_desviop[0]
                print (values_outliers[i] ,"-" ,i) 
            else:
                values_outliers[i] = array_medias[0]- 2.5*array_desviop[0]
                print (values_outliers[i] , "-" ,i) 

    elif i >30 and i<59:
        if(abs(values[i]-array_medias[1]) > 3*array_desviop[1]):
            if(values[i] > array_medias[1]):
                values_outliers[i] = array_medias[1]+ 2.5*array_desviop[1]
                print (values_outliers[i] , "-" ,i) 
            else:
                values_outliers[i] = array_medias[1]- 2.5*array_desviop[1]
                print (values_outliers[i] , "-" ,i) 
    elif i >58 and i<90:
        if(abs(values[i]-array_medias[2]) > 3*array_desviop[2]):
            if(values[i] > array_medias[2]):
                values_outliers[i] = array_medias[2]+ 2.5*array_desviop[2]
                print (values_outliers[i] , "-" ,i) 
            else:
                values_outliers[i] = array_medias[2]- 2.5*array_desviop[2]
                print (values_outliers[i] , "-" ,i) 
    elif i>89 and i<120:
        if(abs(values[i]-array_medias[3]) > 3*array_desviop[3]):
            if(values[i] > array_medias[3]):
                values_outliers[i] = array_medias[3]+ 2.5*array_desviop[3]
                print (values_outliers[i] , "-" ,i) 
            else:
                values_outliers[i] = array_medias[3]- 2.5*array_desviop[3]
                print (values_outliers[i] , "-" ,i) 

    elif i>119 and i<151:
        if(abs(values[i]-array_medias[4]) > 3*array_desviop[4]):
            if(values[i] > array_medias[4]):
                values_outliers[i] = array_medias[4]+ 2.5*array_desviop[4]
                print (values_outliers[i] , "-" ,i) 
            else:
                values_outliers[i] = array_medias[4]- 2.5*array_desviop[4]
                print (values_outliers[i] , "-" ,i) 

    elif i>150 and i<181:
        if(abs(values[i]-array_medias[5]) > 3*array_desviop[5]):
            if(values[i] > array_medias[5]):
                values_outliers[i] = array_medias[5]+ 2.5*array_desviop[5]
                print (values_outliers[i] , "-" ,i) 
            else:
                values_outliers[i] = array_medias[5]- 2.5*array_desviop[5]
                print (values_outliers[i] , "-" ,i) 
    elif i>180 and i<212:
        if(abs(values[i]-array_medias[6]) > 3*array_desviop[6]):
            if(values[i] > array_medias[6]):
                values_outliers[i] = array_medias[6]+ 2.5*array_desviop[6]
                print (values_outliers[i] , "-" ,i) 
            else:
                values_outliers[i] = array_medias[6]- 2.5*array_desviop[6]
                print (values_outliers[i] , "-" ,i) 
    elif i>211 and i<243:
        if(abs(values[i]-array_medias[7]) > 3*array_desviop[7]):
            if(values[i] > array_medias[7]):
                values_outliers[i] = array_medias[7]+ 2.5*array_desviop[7]
                print (values_outliers[i] , "-" ,i) 
            else:
                values_outliers[i] = array_medias[7]- 2.5*array_desviop[7]
                print (values_outliers[i] , "-" ,i) 
    elif i>242 and i<273:
        if(abs(values[i]-array_medias[8]) > 3*array_desviop[8]):
            if(values[i] > array_medias[j]):
                values_outliers[i] = array_medias[8]+ 2.5*array_desviop[8]
                print (values_outliers[i] , "-" ,i) 
            else:
                values_outliers[i] = array_medias[8]- 2.5*array_desviop[8]
                print (values_outliers[i] , "-" ,i) 
    elif i>272 and i<304:
        if(abs(values[i]-array_medias[9]) > 3*array_desviop[9]):
            if(values[i] > array_medias[9]):
                values_outliers[i] = array_medias[9]+ 2.5*array_desviop[9]
                print (values_outliers[i] , "-" ,i) 
            else:
                values_outliers[i] = array_medias[9]- 2.5*array_desviop[9]
                print (values_outliers[i] , "-" ,i) 

    elif i>303 and i<334:
        if(abs(values[i]-array_medias[10]) > 3*array_desviop[10]):
            if(values[i] > array_medias[10]):
                values_outliers[i] = array_medias[10]+ 2.5*array_desviop[10]
                print (values_outliers[i] , "-" ,i) 
            else:
                values_outliers[i] = array_medias[10]- 2.5*array_desviop[10]
                print (values_outliers[i] , "-" ,i) 

    elif i>333 and i<366:
        if(abs(values[i]-array_medias[11]) > 3*array_desviop[11]):
            if(values[i] > array_medias[11]):
                values_outliers[i] = array_medias[11]+ 2.5*array_desviop[11]
                print (values_outliers[i] , "-" ,i) 
            else:
                values_outliers[i] = array_medias[11]- 2.5*array_desviop[11]
                print (values_outliers[i] , "-" ,i) 

#outliers por ano

#detrend linear - serie sem tendencia e grau 1 
values_detrend_linear = np.copy(values)
values_detrend_linear = signal.detrend(values_detrend_linear,-1,type='linear', bp=0)

#detrend constant
#values_detrend_constant = np.copy(values)
values_detrend_constant = signal.detrend(values)
print(values_detrend_constant)
#values_detrend_constant = signal.detrend(values_detrend_constant,-1,type='constant', bp=0)

#polyfit
p1 = np.polyfit(times, values, 2)
p2 = np.polyval(p1,times)
values_ro_t2 = values - p2

#2.7 e 2.8 trimestral sazonalidade
trim = np.arange(0,91,1)

for i in range(91):
    trim[i] =  (values_ro_t2[i] + values_ro_t2[i+91] + values_ro_t2[i+91*2] + values_ro_t2[i+91*3]) /4 

trim = np.matlib.repmat(trim, 1, 4)
trim2 = []
for i in range(len(trim)):
    for j in range(len(trim[i])):
        trim2.append(trim[i][j])
trim2= np.array(trim2)

#Sem sazonalidade
#fazendo batota (o trim so tem 364 valores e os nosso values têm 365)
values_ro_t2_s = []
for i in range(364):
    values_ro_t2_s.append(values_ro_t2[i])

values_ro_t2_s = np.array(values_ro_t2_s)
values_sem_sazonalidade = values_ro_t2_s - trim2

#sem as componentes irregulares
#fazendo batota again
values_ro_t2_364 = []
for i in range(364):
    values_ro_t2_364.append(values_ro_t2[i])

values_ro_t2_364 = np.array(values_ro_t2_364)
values_sem_irregulares = values_ro_t2_364 - values_ro_t2_s - trim2

#mostra grafico sem outliers
plt.figure('DataSet Graph\n')
plt.title('DataSet Graph Values\n')
lines = plt.plot(values)
plt.setp(lines, 'color', 'r', 'linewidth', 1.0)
xmarks=[i for i in range(0,364+1,15)]
plt.xticks(xmarks)
plt.axis([0, 370, -20, 40])
plt.ylabel('Samples\n')
plt.xlabel('\nNumber of Samples')
plt.show()


#mostra grafico com outliers
plt.figure('DataSet Graph\n')
plt.title('DataSet Graph sem Outliers\n')
lines = plt.plot(values_outliers)
plt.setp(lines, 'color', 'r', 'linewidth', 1.0)

lines2 = plt.plot(values_outliers)
plt.setp(lines2, 'color', 'b', 'linewidth', 1.0)

xmarks=[i for i in range(0,364+1,15)]
plt.xticks(xmarks)
plt.axis([0, 370, -20, 40])
plt.ylabel('Samples\n')
plt.xlabel('\nNumber of Samples')
plt.show()


#mostra grafico polyfit
plt.figure('DataSet Graph\n')
plt.title('DataSet Graph com Polyfit\n')
lines2 = plt.plot(values_ro_t2)
plt.setp(lines2, 'color', 'r', 'linewidth', 1.0)
xmarks=[i for i in range(0,364+1,15)]
plt.xticks(xmarks)
plt.axis([0, 370, -20, 40])
plt.ylabel('Samples\n')
plt.xlabel('\nNumber of Samples')
plt.show()

#mostra grafico detrend linear
plt.figure('DataSet Graph\n')
plt.title('DataSet Graph com Detrend Linear\n')
lines2 = plt.plot(values_detrend_linear)
plt.setp(lines2, 'color', 'r', 'linewidth', 1.0)
xmarks=[i for i in range(0,364+1,15)]
plt.xticks(xmarks)
plt.axis([0, 370, -20, 40])
plt.ylabel('Samples\n')
plt.xlabel('\nNumber of Samples')
plt.show()

#mostra grafico detrend constante
plt.figure('DataSet Graph\n')
plt.title('DataSet Graph com Detrend Constante\n')
lines2 = plt.plot(values_detrend_constant)
plt.setp(lines2, 'color', 'r', 'linewidth', 1.0)
xmarks=[i for i in range(0,364+1,15)]
plt.xticks(xmarks)
plt.axis([0, 370, -20, 40])
plt.ylabel('Samples\n')
plt.xlabel('\nNumber of Samples')
plt.show()

#Sem sazonalidade (se calhar é preciso mudar)
plt.figure('DataSet Graph\n')
plt.title('DataSet Graph sem Sazonalidade\n')
lines2 = plt.plot(values_sem_sazonalidade)
plt.setp(lines2, 'color', 'r', 'linewidth', 1.0)
xmarks=[i for i in range(0,364+1,15)]
plt.xticks(xmarks)
plt.axis([0, 370, -20, 40])
plt.ylabel('Samples\n')
plt.xlabel('\nNumber of Samples')
plt.show()

#Componente da Sazonalidade
plt.figure('DataSet Graph\n')
plt.title('DataSet Graph Sazonalidade\n')
lines2 = plt.plot(trim2)
plt.setp(lines2, 'color', 'r', 'linewidth', 1.0)
xmarks=[i for i in range(0,364+1,15)]
plt.xticks(xmarks)
plt.axis([0, 370, -20, 40])
plt.ylabel('Samples\n')
plt.xlabel('\nNumber of Samples')
plt.show()


#Sem irregulares (se calhar é preciso mudar)
plt.figure('DataSet Graph\n')
plt.title('DataSet Graph sem irregularidades\n')
lines2 = plt.plot(values_sem_irregulares)
plt.setp(lines2, 'color', 'r', 'linewidth', 1.0)
xmarks=[i for i in range(0,364+1,15)]
plt.xticks(xmarks)
plt.axis([0, 370, -20, 40])
plt.ylabel('Samples\n')
plt.xlabel('\nNumber of Samples')
plt.show()


