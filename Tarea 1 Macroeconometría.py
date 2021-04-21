# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 07:52:01 2021

@author: David Gerardo Mora Salazar
"""
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import normalize
import requests
import io
#1.a
# Download data from web page
url="https://vincentarelbundock.github.io/Rdatasets/csv/datasets/airquality.csv"
s=requests.get(url).content
a=pd.read_csv(io.StringIO(s.decode('utf-8')))
#1.b
# Rename the columns of a: a.1
#b = a.rename(columns = {0: 'Time'}, inplace = False)
pd.options.display.max_rows = 20
print(a)
#1.c
a.plot(subplots=True, figsize=(6, 6)); plt.legend(loc='best')
#1.c.alternativa1
fig, axes = plt.subplots(nrows=2, ncols=2)
a['Ozone'].plot(ax=axes[0,0]); axes[0,0].set_title('Ozone')
a['Temp'].plot(ax=axes[0,1]); axes[0,1].set_title('Temp')
a['Solar.R'].plot(ax=axes[1,0]); axes[1,0].set_title('Solar.R')
a['Wind'].plot(ax=axes[1,1]); axes[1,1].set_title('Wind')
#1.c.alternativa2
sns.set_theme(style="ticks")

# Load the example dataset for Anscombe's quartet
df = sns.load_dataset("anscombe")

# Show the results of a linear regression within each dataset
sns.lmplot(x="Day", y="Ozone", col="Ozone", hue="Ozone", data=a,
           col_wrap=2, ci=None, palette="muted", height=4,
           scatter_kws={"s": 50, "alpha": 1})
# sns.set_theme(style="darkgrid")

# # Load an example dataset with long-form data
# fmri = sns.load_dataset("a")

# # Plot the responses for different events and regions
# sns.lineplot(x="Day", y="Ozone",
#              hue="region", style="event",
#              data=a)
