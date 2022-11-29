import numpy as np
import matplotlib.pyplot as plt
import datetime 

daten=np.genfromtxt('bremen_klima_tag_18900101_20211231.csv',delimiter=";",skip_header=1)


temp=daten[:,13]
messDatum=daten[:,1]


datum=[]
intdates=[]

for date in messDatum:
    intdate=int(date)
    strdate=str(intdate)
    intdates.append(intdate)  
    dtdate=(datetime.datetime.strptime(strdate,'%Y%m%d')).date()
    datum.append(dtdate)
    
intdatArray=np.asarray(intdates)    

#%%2021 Daten

datum21=[]
for date in datum:
    if (date.year==2021):
        datum21.append(date)



index21=np.argwhere((intdatArray>=20210101) & (intdatArray<=20211231))


temp21=temp[index21]


#%% Aufgabe 1 Das Jahr 2021 Platten


plt.figure(figsize=(9, 6))
plt.plot(datum21, temp21, label='2021')
plt.xlabel('Datum')
plt.ylabel('Temperatur')
plt.title("2021 Temperatur Liniendieagramm")
plt.legend();



#%% Aufgabe 2 Statistik über das Jahr 2021

maxInd= np.argwhere(temp21==temp21.max())
minInd=np.argwhere(temp21==temp21.min())

maxDatum=datum21[maxInd[0,0]]
minDatum=datum21[minInd[0,0]]

print("Durchschnitts-Temperatur für das Jahr 2021 =>  ", "{:.2f}".format(temp21.mean()))
print("Max-Temperatur für das Jahr 2021 =>  ", "{:.2f}".format(temp21.max()), "an diesen Tag=> " , maxDatum)
print("Min-Temperatur für das Jahr 2021 =>  ", "{:.2f}".format(temp21.min()), "an diesen Tag=> ", minDatum)




#%% Aufgabe 3 Die Monate in 2021

monat21Mean=[]
for x in range(0,12):
    indices = np.argwhere((intdatArray>=(20210101+(x*100))) & (intdatArray<(20210201+(x*100))))
    y=temp[indices]
    monat21Mean.append(y.mean())
    print("Durchschnitts-Temperatur für monat ",x+1, " ist ", "{:.2f}".format(monat21Mean[x]))
    

plt.bar(range(1,13), monat21Mean)
plt.xlabel("Monaten")
plt.ylabel("Durchschnitt Temp")
plt.title("2021 Durchschnitt Temperatur Balken")
plt.show()
    

    

#%% Aufgabe 4 Monatstat von 2000-2021
datum22Jahre=[]

for date in datum:
    if (date.year>=2000):
        datum22Jahre.append(date)


def monatcalc(year):
    monatMean=[]
    for x in range(0,12):
        indices = np.argwhere((intdatArray>=((year*10000)+101+(x*100))) & (intdatArray<((year*10000)+201)+(x*100)))
        y=temp[indices]
        monatMean.append(y.mean())
    return monatMean

jahre22meanmonatlich=[]

for y in range(2000,2022): 
    print(monatcalc(y))
    

#%% Aufgabe 5 Klimawandel
jahresMean1=[]
for x in range(0,55):
    indices = np.argwhere((intdatArray>=(18900101+(x*10000))) & (intdatArray<(18910101+(x*10000))))
    y2=temp[indices]
    jahresMean1.append(y2.mean())
    print("Durchschnitts-Temperatur für das Jahr ",x+1890, " ist ", "{:.2f}".format(jahresMean1[x]))

jahresMean2=[]
for x in range(0,75):
    indices = np.argwhere((intdatArray>=(19470101+(x*10000))) & (intdatArray<(20210101+(x*10000))))
    y3=temp[indices]
    jahresMean2.append(y3.mean())
    print("Durchschnitts-Temperatur für das Jahr ",x+1947, " ist ", "{:.2f}".format(jahresMean2[x]))
    
jahresMean=np.concatenate((jahresMean1,jahresMean2))
x1=range(1890,1945)
x2=range(1947,2022)
xJahr=np.concatenate((x1,x2))
plt.figure(figsize=(9, 6))
plt.plot(xJahr, jahresMean, label='Durchschnitt Temperatur')
plt.xlabel('Jahr')
plt.ylabel('Jahresdurchschnittstemperatur')
plt.title("1890-2021 (ausser 1945,46) Jahresdurchschnittstemperatur Liniendieagramm")
plt.legend(); 


#%%Aufgabe 5 Lineare Regression

linmod = np.polyfit(xJahr, jahresMean, 1)
plt.scatter(xJahr, jahresMean,label="scatter")
plt.plot(xJahr,np.polyval(linmod,xJahr),color="red",label="regression line")   
plt.xlabel('Jahr')
plt.ylabel('Jahresdurchschnittstemperatur')
plt.title("1890-2021 (ausser 1945,46) Jahresdurchschnittstemperatur Lineare Regression")
plt.legend(loc='lower right'); 

#%%control
indexcontrol=np.argwhere((intdatArray>=18910101) & (intdatArray<=18911231))


tempcontrol=temp[indexcontrol]
tempcontrol.mean()



#%%
temp=daten[:,13]
datum=[]
for date in daten[:,1]:
    strdate=str(int(date))
    dtdate=(datetime.datetime.strptime(strdate,'%Y%m%d')).date()
    datum.append(dtdate)
temp21=[]
datum21=[]
datum21=[]
for date in datum:
    if (date.year==2021):
        datum21.append(date)