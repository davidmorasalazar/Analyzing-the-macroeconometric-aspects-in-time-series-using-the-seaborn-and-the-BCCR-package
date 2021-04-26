# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 07:52:01 2021
@author: David Gerardo Mora Salazar
"""
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import io
import xlrd
from bccr import SW
from scipy import stats
# xlrd.xlsx.ensure_elementtree_imported(False, None)
# xlrd.xlsx.Element_has_iter = True
#pip install bccr
#!pip install xlrd==1.2.0
#1.a
# Download data from web page
urla="https://vincentarelbundock.github.io/Rdatasets/csv/datasets/airquality.csv"
s1=requests.get(urla).content
a=pd.read_csv(io.StringIO(s1.decode('utf-8')))
#1.b
#Create variable Date:
a['dateInt']= "1973" + a['Month'].astype(str).str.zfill(2)+ a['Day'].astype(str).str.zfill(2)
a['Date'] = pd.to_datetime(a['dateInt'], format='%Y%m%d')
#1.c
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(25, 15))
fig.suptitle('Ozono, radiación solar, velocidad media del viento y temperatura máxima')
a.plot(ax=axes[0,0], x = "Date", y = "Ozone", color="k"); axes[0,0].set_title('Ozone')
a.plot(ax=axes[0,1],  x = "Date", y = "Temp", color="green"); axes[0,1].set_title('Temp')
a.plot(ax=axes[1,0], x = "Date", y = "Solar.R", color="blue"); axes[1,0].set_title('Solar.R')
a.plot(ax=axes[1,1], x = "Date", y = "Wind", color="orange"); axes[1,1].set_title('Wind')
#1.d
#2.a
urlb="https://vincentarelbundock.github.io/Rdatasets/csv/datasets/AirPassengers.csv"
s2=requests.get(urlb).content
b=pd.read_csv(io.StringIO(s2.decode('utf-8')))
#2.b
ax = sns.lineplot(data=b, x="Unnamed: 0", y="value")
ax.set(title="Información mensual de enero 1949 a diciembre 1960 del número de pasajeros aéreos internacionales", xlabel='Número del mes', ylabel='Número de pasajeros')
#2.c
b['Natural logarithm of value'] = np.log(b['value'])
ax = sns.lineplot(data=b, x="Unnamed: 0", y="Natural logarithm of value")
ax.set(title="Información mensual de enero 1949 a diciembre 1960 del número de pasajeros aéreos internacionales", xlabel='Número del mes', ylabel='Logaritmo natural del número de pasajeros')
#3.a
wb = xlrd.open_workbook('C:/Users/David Mora Salazar/Documents/ECONOMÍA UNIVERSIDAD DE COSTA RICA/Macroeconometría/Tarea 1/IPC Julio 2006 = 100.xlsx')
sh1 = wb.sheet_by_name(u'ipccompu')
x = sh1.col_values(0)  # column 0
y = sh1.col_values(1)  # column 1
plt.plot(x[7:252], y[7:252])
plt.xticks(x[7:252][::12], rotation='vertical', fontsize=10)
plt.title("Serie en nivel del IPC, Base Julio 2006=100")    
plt.xlabel("Fecha")
plt.ylabel("IPC")
plt.subplots_adjust(bottom=0.35)
plt.show()
#3.a.alternativa
IPC = SW({979:'IPC Julio 2006 = 100'}, FechaInicio=1995)  # pasando un diccionario para renombrar las series
IPC.plot();
plt.title("Serie en nivel del IPC, Base Julio 2006=100")
plt.xlabel("Fecha de 1995 a 2015")
plt.ylabel("IPC")
#3.a.alternativa2
def figura(datos, titulo, y):
    fig, ax = plt.subplots(figsize=(12,5))
    ax = datos.plot(ax=ax, legend=None)
    ax.set(title=titulo, xlabel="Fecha de 1995 a 2015", ylabel=y)
    return fig
figura(IPC,"Serie en nivel del IPC, Base Julio 2006=100", "IPC")
#3.b
figura(100*IPC.diff(1),
       'Cambio mensual en el IPC de Costa Rica, Base Julio 2006 = 100',
       'IPC');
#3.c
# transIPC1 = 100*IPC.pct_change(1)
# translogIPC2 = 100*np.log(IPC).diff(1)
# IPCrespaldo = IPC.copy()
# IPCrespaldo['Tasa de crecimiento mensual del IPC'] =transIPC1
# IPCrespaldo['Primera diferencia del logaritmo del IPC'] =translogIPC2
# IPCrespaldo['Tasa de crecimiento mensual del IPC'].plot(color="green", legend="normal")
# IPCrespaldo['Primera diferencia del logaritmo del IPC'].plot(linestyle="dotted", color = "red", linewidth="3", legend="logaritmo")
# plt.rcParams["figure.figsize"] = (20,20)
# plt.legend(fontsize=30)
# plt.title("Tasa de crecimiento mensual del IPC y primera diferencia del logaritmo del IPC", fontsize=30)
# plt.xlabel(xlabel= "Fecha de 1995 a 2015",fontsize=30)
# plt.ylabel(ylabel= "IPC",fontsize=30)
# plt.show()        
def figura1(dato1, dato2, leyenda1, leyenda2, titulo, y):
    variable_de_apoyo1 = dato1
    variable_de_apoyo2 = dato2
    IPCrespaldo = IPC.copy()
    IPCrespaldo['variable_de_apoyo1'] =variable_de_apoyo1
    IPCrespaldo['variable_de_apoyo2'] =variable_de_apoyo2
    IPCrespaldo['variable_de_apoyo1'].plot(color="green", label=leyenda1)
    IPCrespaldo['variable_de_apoyo2'].plot(linestyle="dotted", color = "red", linewidth="3", label=leyenda2)
    plt.rcParams["figure.figsize"] = (20,20)
    plt.legend(fontsize=30)
    plt.title(titulo, fontsize=30)
    plt.xlabel(xlabel= "Fecha de 1995 a 2015",fontsize=30)
    plt.ylabel(ylabel= y,fontsize=30)
    plt.show()        
    return
figura1(100*IPC.pct_change(1), 100*np.log(IPC).diff(1), "Tasa de crecimiento mensual del IPC", "Primera diferencia del logaritmo del IPC","Tasa de crecimiento mensual del IPC y primera diferencia del logaritmo del IPC", "IPC")   
#3.d
figura1(IPC.diff(4), 100*np.log(IPC).diff(4), "Tasa de crecimiento interanual del IPC", "Diferencia estacional del logaritmo del IPC","Tasa de crecimiento interanual y la diferencia estacional del logaritmo del IPC", "IPC")   
#3.d.alternativa
figura(IPC.diff(4),
       'Tasa de crecimiento interanual del IPC',
       '"IPC');
figura(100*np.log(IPC).diff(4),
       'Diferencia estacional del logaritmo de la serie',
       'por ciento');
#3.e
IPCsuavizadotrimestral = pd.concat([IPC, IPC.rolling(4).mean()], axis=1)
IPCsuavizadotrimestral.columns = ['Serie original', 'Serie suavizada']

figura(IPCsuavizadotrimestral,
    'IPC de Costa Rica tomando el promedio para cada trimestre',
    'Por ciento');
#3.f
IPCsuavizadoanual = pd.concat([IPC, IPC.rolling(13).mean()], axis=1)
IPCsuavizadoanual.columns = ['Serie original', 'Serie suavizada']

figura(IPCsuavizadoanual,
    'IPC de Costa Rica tomando el promedio de los 12 meses de cada año',
    'por ciento');

#4.a
euroframe = pd.read_csv('C:/Users/David Mora Salazar/Documents/ECONOMÍA UNIVERSIDAD DE COSTA RICA/Macroeconometría/Tarea 1/euro.csv')  
def figura3 (datos, indice_inicial, indice_final, titulo, y):
    fig3, ax = plt.subplots(figsize=(20,5))
    ax = sns.lineplot(data=datos, x =datos.fecha[indice_inicial:indice_final], y = 100*np.log(datos.euro[indice_inicial:indice_final]).diff(1) )
    ax.set(title=titulo, xlabel=" ", ylabel=y)    
    plt.xticks(rotation=90)
    plt.xticks(datos.fecha[indice_inicial:indice_final][::2])  
    return fig3

figura3(euroframe, 5300, 5475, "Tasa de depreciación diaria del euro con respecto al dólar como la primera diferencia del logaritmo natural del tipo de cambio", "Variación")
#4.b
depreciación = 100*np.log(euroframe.euro[0:5476]).diff(1)
media = np.mean(depreciación)
desviacion = np.std(depreciación)
np.random.seed(987654321)
x = np.random.normal(media, desviacion, 100000)
#Histograma de la muestra
count, bins, ignored = plt.hist(x, 30, density=True)
plt.plot(bins, 1/(desviacion * np.sqrt(2 * np.pi)) *
               np.exp( - (bins - media)**2 / (2 * desviacion**2) ),
         linewidth=2, color='r')
plt.show()
#Prueba de jarque_bera
jarque_bera_test = stats.jarque_bera(x)
jarque_bera_test
#No se rechaza la hipótesis nula de distribución normal.
#4.c
