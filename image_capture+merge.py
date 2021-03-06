import os
import time
from selenium import webdriver
from PIL import Image

os.chdir("F:\project\오션_2021")

wd = webdriver.Chrome(r'F:\project\오션_2021\chromedriver.exe')

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

for i in range(0,int(londiff)+2):
    llon.append(slon+1.25*i)
    
for i in range(0,int(latdiff)+2):
    llat.append(slat+1.25*i)

a=len(llat)
b=len(llon)

for i in range(a):
    for j in range(b):
        os.chdir("F:\project\오션_2021")
        url = 'https://www.google.com/maps/@'+str(llat[i])+','+str(llon[j])+',10z?hl=ko'
        wd.get(url)
        time.sleep(0.01)
        os.chdir("F:\project\오션_2021\captures")
        wd.save_screenshot(str(i)+str(j)+'.png')
wd.close()

merged = Image.new('RGB', (929*b,888*a))

for i in range(a):
    for j in range(b):
        im = Image.open(str(i)+str(j)+'.png')
        merged.paste(im, (929*j, 888*(a-1-i)))

merged.save('final.png')
