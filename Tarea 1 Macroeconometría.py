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
#pip install bccr
#1.a
# Download data from web page
urla="https://vincentarelbundock.github.io/Rdatasets/csv/datasets/airquality.csv"
s1=requests.get(urla).content
a=pd.read_csv(io.StringIO(s1.decode('utf-8')))
#1.b
#Rename the columns of a: a.1
b = a.rename(columns = {0: 'Time'}, inplace = False)
pd.options.display.max_rows = 20
#1.c
a.plot(subplots=True, figsize=(10, 10)); plt.legend(loc='best')
#1.c.alternativa1
fig, axes = plt.subplots(nrows=2, ncols=2)
a['Ozone'].plot(ax=axes[0,0]); axes[0,0].set_title('Ozone')
a['Temp'].plot(ax=axes[0,1]); axes[0,1].set_title('Temp')
a['Solar.R'].plot(ax=axes[1,0]); axes[1,0].set_title('Solar.R')
a['Wind'].plot(ax=axes[1,1]); axes[1,1].set_title('Wind')
#1.c.alternativa2
# y = ["Ozone"]
# x = ["Day"]
# g = sns.FacetGrid(a, row='Ozone', col='Day')
# g.map(sns.lmplot, "age")
# plt.show()
#1.d

# #2.a
urlb="https://vincentarelbundock.github.io/Rdatasets/csv/datasets/AirPassengers.csv"
s2=requests.get(urlb).content
b=pd.read_csv(io.StringIO(s2.decode('utf-8')))
#2.b
sns.lineplot(data=b, x="Unnamed: 0", y="value")
#2.c
b['Natural logarithm of value'] = np.log(b['value'])
sns.lineplot(data=b, x="Unnamed: 0", y="Natural logarithm of value")
#3.a
wb = xlrd.open_workbook('C:/Users/MiBebe/Downloads/IPC.xlsx')
sh1 = wb.sheet_by_name(u'Hoja1')
x = sh1.col_values(0)  # column 0
y = sh1.col_values(1)  # column 1
plt.plot(x[290:318], y[290:318])
plt.xticks(x[290:318], rotation='vertical', fontsize=5)
plt.subplots_adjust(bottom=0.35)
plt.show()
#3.a.alternativa
IPC = SW({979:'IPC Julio 2006 = 100'}, FechaInicio=2000)  # pasando un diccionario para renombrar las series
IPC.plot();
#3.a.alternativa2
def figura(datos, titulo, y):
    fig, ax = plt.subplots(figsize=(12,5))
    ax = datos.plot(ax=ax, legend=None)
    ax.set(title=titulo, xlabel=" ", ylabel=y)
    return fig
figura(IPC,"IPC", "Julio 2006 = 100")
#3.b
figura(IPC.diff(1),
       'Cambio trimestral en el IPC de Costa Rica',
       'Base J2006 = 100');
#3.b.alternativa
IPC1 = SW({1043:'IPC (J2006=100) variación mensual'}, FechaInicio=2000)  # pasando un diccionario para renombrar las series
IPC1.plot(figsize = (12,5));

#3.c.1
def figura1(datos, datos1, titulo, y):
    fig1, ax = plt.subplots(figsize=(12,10))
    fig2, ax1 = plt.subplots(figsize=(12,10))
    # concatenar = pd.concat([datos, datos1])    
    # ax = sns.lineplot(data=concatenar)
    ax = datos.plot(ax=ax, legend=None)
    ax1 = datos1.plot(ax1=ax1, legend=None)  
    ax.set(title=titulo, xlabel=" ", ylabel=y)    
    ax1.set(title=titulo, xlabel=" ", ylabel=y)

    return
figura1(100*IPC.pct_change(1), 100*np.log(IPC).diff(1)," Tasa de crecimiento y la primera diferencia del logaritmo del IPC", "Julio 2006 = 100")

transIPC1 = 100*IPC.pct_change(1)
translogIPC2 = 100*np.log(IPC).diff(1)
transIPC1.plot(figsize = (12,5));
translogIPC2.plot(figsize = (12,5));
#3.d

#3.e

#3.f

#4.a
