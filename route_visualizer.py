import os
import pandas as pd
import numpy as np
from PIL import Image

os.chdir("F:\project\오션_2021")
route=pd.read_excel("route.xlsx")
route=pd.DataFrame(route).to_numpy()

os.chdir("F:\project\오션_2021\captures")

image=Image.open("imcolorchanged.png")
pix = np.array(image)
red=np.array([255,0,0], dtype='uint8')
white=np.array([255,255,255], dtype='uint8')
blue=np.array([156,192,249], dtype='uint8')

routef=[]

for i in range(len(route)):
    x=route[i][1]*74
    y=route[i][0]*71
    routef.append([x,y])

routef=np.array(routef)
mappoint=[]

for i in range(len(routef)-1):
    alpha1,beta1=routef[i][0],routef[i][1]
    alpha2,beta2=routef[i+1][0],routef[i+1][1]
    a=(beta1-beta2)/(alpha1-alpha2)
    b=(beta1*alpha2-beta2*alpha1)/(alpha2-alpha1)
    for j in range(alpha1,alpha2):
        x=j
        y=a*x+b
        y=round(y)
        mappoint.append([x,y])

for i in range(1,len(mappoint)):
    pix[mappoint[i][1]][mappoint[i][0]]=red

for i in range(2,len(mappoint)):
    pix[mappoint[i][1]-1][mappoint[i][0]-1]=red
    
for i in range(1,len(mappoint)-1):
    pix[mappoint[i][1]+1][mappoint[i][0]+1]=red

route_final=Image.fromarray(pix)
route_final.save("route_final.png")
