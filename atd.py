import statsmodels as sm
import numpy as np
import csv
import math
import matplotlib.pyplot as plt
from scipy import interpolate
from scipy import signal
from scipy import stats, linalg
import numpy.matlib
from statsmodels.tsa.stattools import adfuller
import statsmodels.tsa as sm


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

#detrend linear - serie sem tendencia e grau 1 
values_detrend_linear = np.copy(values_outliers)
values_detrend_linear = signal.detrend(values_outliers,-1,type='linear', bp=0)

#detrend constant
values_detrend_constant = np.copy(values_outliers)
values_detrend_constant =signal.detrend(values_outliers,-1,type='constant', bp=0)

#polyfit
p1 = np.polyfit(times, values_outliers, 2)
p2 = np.polyval(p1,times)

#serie sem a tendencia
values_ro_t2 = values_outliers - p2

#2.7 e 2.8  sazonalidade trimestral
trim = np.arange(0,91,1)

for i in range(91):
    trim[i] =  (values_ro_t2[i] + values_ro_t2[i+91] + values_ro_t2[i+91*2] + values_ro_t2[i+91*3]) /4

auxiliar = []
ho = np.matlib.repmat(trim, 1, 4)
for i in range(len(ho)):
    for j in range(len(ho[i])):
        auxiliar.append(ho[i][j])

auxiliar.append(0)
auxiliar = np.array(auxiliar)

#sem sazonalidade
values_sem_sazonalidade = np.subtract(values_outliers, auxiliar)

#componente sazonal
saz = np.subtract(values_outliers,values_sem_sazonalidade)


#sem as componentes irregulares
values_sem_irregulares = np.subtract(values_outliers, values_sem_sazonalidade)

#componente irregular
irregularidade = np.subtract(values_outliers,values_sem_irregulares)

#3.1
N = len(values_outliers)
t = np.arange(0,91,1) #escala temporal
tt = np.arange(0,4*91,1) #escala temporal para previsao

#teste de estacionaridade da serie regularizada
result = adfuller(values_outliers,1)
print('ADF Statistic: %f' % result[0])
print('p-value: %f' % result[1])
print('Critical Values:')
for key, value in result[4].items():
	print('\t%s: %.3f' % (key, value))
print result

#3.3 
#auto correlation
y = saz - np.mean(saz)
norm = np.sum(y ** 2)
correlated = np.correlate(y, y, mode='full')/norm
#falta par corr

#3.5
NA1_ar =6
#modelo AR 
#model1_AR = sm.ar_model.AR(values_outliers, dates=None, freq=None, missing='none')

#3.6 - siimulacao modelo AR

'''
#----------------------------------------- graficos ---------------------------------------------------
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

#mostra grafico detrend linear
plt.figure('DataSet Graph\n')
plt.title('Serie sem tendencia - grau 1 - linear\n')
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
plt.title('Serie sem tendencia - grau 1 - constante\n')
lines2 = plt.plot(values_detrend_constant)
plt.setp(lines2, 'color', 'r', 'linewidth', 1.0)
xmarks=[i for i in range(0,364+1,15)]
plt.xticks(xmarks)
plt.axis([0, 370, -20, 40])
plt.ylabel('Samples\n')
plt.xlabel('\nNumber of Samples')
plt.show()

#mostra grafico polyfit
plt.figure('DataSet Graph\n')
plt.title('Serie com a componente da tendencia de grau 2\n')
lines2 = plt.plot(p2)
plt.setp(lines2, 'color', 'r', 'linewidth', 1.0)
xmarks=[i for i in range(0,364+1,15)]
plt.xticks(xmarks)
plt.axis([0, 370, -20, 40])
plt.ylabel('Samples\n')
plt.xlabel('\nNumber of Samples')
plt.show()

#mostra grafico sem componente da tendencia
plt.figure('DataSet Graph\n')
plt.title('Serie sem a componente da tendencia de grau 2\n')
lines2 = plt.plot(values_ro_t2)
plt.setp(lines2, 'color', 'r', 'linewidth', 1.0)
xmarks=[i for i in range(0,364+1,15)]
plt.xticks(xmarks)
plt.axis([0, 370, -20, 40])
plt.ylabel('Samples\n')
plt.xlabel('\nNumber of Samples')
plt.show()

#mostra grafico componente sazonalidade
plt.figure('DataSet Graph\n')
plt.title('Componente sazonalidade\n')
lines2 = plt.plot(auxiliar)
plt.setp(lines2, 'color', 'r', 'linewidth', 1.0)
xmarks=[i for i in range(0,364+1,15)]
plt.xticks(xmarks)
plt.axis([0, 370, -20, 40])
plt.ylabel('Samples\n')
plt.xlabel('\nNumber of Samples')
plt.show()

#Sem sazonalidade
plt.figure('DataSet Graph\n')
plt.title('Serie sem Sazonalidade\n')
lines2 = plt.plot(values_sem_sazonalidade)
plt.setp(lines2, 'color', 'r', 'linewidth', 1.0)
xmarks=[i for i in range(0,364+1,15)]
plt.xticks(xmarks)
plt.axis([0, 370, -20, 40])
plt.ylabel('Samples\n')
plt.xlabel('\nNumber of Samples')
plt.show()


#Sem irregulares
plt.figure('DataSet Graph\n')
plt.title('Serie sem irregularidades\n')
lines2 = plt.plot(values_sem_irregulares)
plt.setp(lines2, 'color', 'r', 'linewidth', 1.0)
xmarks=[i for i in range(0,364+1,15)]
plt.xticks(xmarks)
plt.axis([0, 370, -20, 40])
plt.ylabel('Samples\n')
plt.xlabel('\nNumber of Samples')
plt.show()

#Componente irregular
plt.figure('DataSet Graph\n')
plt.title('Componente irregular\n')
lines2 = plt.plot(irregularidade)
plt.setp(lines2, 'color', 'r', 'linewidth', 1.0)
xmarks=[i for i in range(0,364+1,15)]
plt.xticks(xmarks)
plt.axis([0, 370, -20, 40])
plt.ylabel('Samples\n')
plt.xlabel('\nNumber of Samples')
plt.show()
'''
plt.figure('DataSet Graph\n')
plt.title('FAC\n')
lines2 = plt.plot(correlated)
plt.setp(lines2, 'color', 'r', 'linewidth', 1.0)
xmarks=[i for i in range(0,364+1,15)]
plt.xticks(xmarks)
plt.axis([0, 370, -20, 40])
plt.ylabel('Samples\n')
plt.xlabel('\nNumber of Samples')
plt.show()

