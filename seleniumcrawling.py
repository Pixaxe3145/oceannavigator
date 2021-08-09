import os
from selenium import webdriver
import numpy as np
import pandas as pd
import time

os.chdir("F:\project\오션_2021")

f=open(".\latlong.txt",'r')

A=[]
for i in range(4):
    line=f.readline()
    A.append(line)
f.close()

slat=float(A[0].rstrip('\n'))
slon=float(A[1].rstrip('\n'))
elat=float(A[2].rstrip('\n'))
elon=float(A[3].rstrip('\n'))

slat=round(slat,1)
elat=round(elat,1)
slon=round(slon,1)
elon=round(elon,1)


latdiff=(elat-slat)//0.1
londiff=(elon-slon)//0.1

llat=[]
llon=[]

for i in range(0,int(londiff)+2):
    llon.append(slon+0.1*i)
    
for i in range(0,int(latdiff)+2):
    llat.append(slat+0.1*i)

a=len(llat)
b=len(llon)

wd = webdriver.Chrome(r'F:\project\오션_2021\chromedriver.exe')

murl='https://earth.nullschool.net/ko/#current/wind/surface/level/orthographic/loc='
url=murl+str(llon[0])+','+str(llat[0])
wd.get(url)
time.sleep(1)

C=[]

for i in range(a):
    C.append([])
    for j in range(b):
        C[i].append([])

for i in range(a):
    for j in range(b):
        murl='https://earth.nullschool.net/ko/#current/wind/surface/level/orthographic/loc='
        url=murl+str(llon[j])+','+str(llat[i])
        wd.get(url)
        aa=wd.find_element_by_xpath("//div[@data-name='spotlight-a']/div")
        temp=aa.text
        temp=str(temp)
        templ=temp.split()
        tempf=templ[0]+','+templ[2]
        C[i][j]=tempf
        
wd.close()