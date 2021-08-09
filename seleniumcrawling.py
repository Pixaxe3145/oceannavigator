import os
from selenium import webdriver
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

slat=round(slat,2)
elat=round(elat,2)
slon=round(slon,2)
elon=round(elon,2)


latdiff=(elat-slat)//1.25
londiff=(elon-slon)//1.25

llat=[]
llon=[]

for i in range(0,int(londiff)):
    llon.append(slon+1.25*i)
    
for i in range(0,int(latdiff)):
    llat.append(slat+1.25*i)

a=len(llat)
b=len(llon)

url='https://earth.nullschool.net/ko/#current/wind/surface/level/orthographic/loc=168.294,38.156'

wd = webdriver.Chrome(r'F:\project\오션_2021\chromedriver.exe')

wd.get(url)

aa=wd.find_element_by_xpath("//div[@data-name='spotlight-a']/div")

time.sleep(3)

print(aa.text)