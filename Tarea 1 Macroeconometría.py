# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 07:52:01 2021

@author: David Gerardo Mora Salazar
"""
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
from unicodedata import normalize
import requests
import io
# Download data from web page
url="https://vincentarelbundock.github.io/Rdatasets/csv/datasets/airquality.csv"
s=requests.get(url).content
a=pd.read_csv(io.StringIO(s.decode('utf-8')))
print(a)