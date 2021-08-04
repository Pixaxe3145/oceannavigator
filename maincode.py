from urllib.request import urlopen 
from urllib.request import Request
from bs4 import BeautifulSoup
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

url="https://earth.nullschool.net/ko/#current/ocean/primary/waves/overlay=currents/orthographic=-174.93,20.69,639/loc="

A=list(map(float,input.split()))
slatitude, slongitude=A[0],A[1]

B=list(map(float,input.split()))
elatitude, elongitude=B[0],B[1]

lat=elatitude-slatitude
long=elongitude-slongitude

latdiff=lat/0.1
longdiff=long/0.1

lat=[]
long=[]

for i in range(0,int(longdiff)):
    long.append(slongitude+0.1*i)
    
for i in range(0,int(latdiff)):
    lat.append(slatitude+0.1*i)

murl=url+str(long)+','+str(lat)

html=urlopen