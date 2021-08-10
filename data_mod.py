import pandas as pd
import numpy as np
import os
import math

os.chdir("F:\project\오션_2021")

fmap=pd.read_excel("final_map.xlsx")
fcur=pd.read_excel("final_current.xlsx")

fmap=pd.DataFrame(fmap).to_numpy()
fcur=pd.DataFrame(fcur).to_numpy()

w=len(fcur[0])
h=len(fcur)

f=open(".\imcrop.txt",'w')

f.write(str(w))
f.write("\n")
f.write(str(h))
f.close()

fmap=fmap[0:len(fmap)-6]
hh=len(fmap)-h
fmap=fmap[hh:]

ffmap=[]

for i in range(len(fmap)):
    temp=np.array([])
    ftemp=np.array([])
    temp=fmap[i][6:len(fmap[i])]
    ftemp=temp[0:w]
    ftemp=ftemp.tolist()
    ffmap.append(ftemp)

ffmap=np.array(ffmap)
fmapp=[]

for i in range(h):
    ttemp=[]
    for j in range(w):
        if ffmap[i][j]==1:
            temp=[]
            temp=fcur[i][j].split(',')
            deg=int(temp[0][:-1])
            spd=int(temp[1])
            spdx=(-1)*math.sin(math.pi*(deg/180))
            spdy=(-1)*math.cos(math.pi*(deg/180))
            spdf=str(spdx)+','+str(spdy)
            ttemp.append(spdf)
        else:
            ttemp.append(0)
    fmapp.append(ttemp)

fmapp=np.array(fmapp)
