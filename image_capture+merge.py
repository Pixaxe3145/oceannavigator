from selenium import webdriver
import time
from PIL import Image
import os

os.chdir("F:\project\오션_2021")

wd = webdriver.Chrome(r'F:\project\오션_2021\chromedriver.exe')

A=list(map(float,input().split()))

slat, slon=A[0],A[1]

B=list(map(float,input().split()))

elat, elon=B[0],B[1]

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

for i in range(a):
    for j in range(b):
        lat=str(llat[i])
        lon=str(llon[j])
        os.chdir("F:\project\오션_2021")
        url = 'https://www.google.com/maps/@'+lat+','+lon+',10z?hl=ko'
        wd.get(url)
        time.sleep(0.01)
        os.chdir("F:\project\오션_2021\captures")
        wd.save_screenshot(str(i)+str(j)+'.png')
        
wd.quit()

os.chdir("F:\project\오션_2021\captures")

merged = Image.new('RGB', (929*a,888*b))

for i in range(a):
    for j in range(b):
        im = Image.open(str(i)+str(j)+'.png')
        merged.paste(im, (929*j, 888*(b-1-i)))

merged.save('final.png')