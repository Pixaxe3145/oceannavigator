import os
import pandas as pd
import numpy as np

os.chdir("F:\project\오션_2021")
fmap=pd.read_excel("current+map.xlsx")
fmap=pd.DataFrame(fmap).to_numpy()

curx=[]
cury=[]

for i in range(len(fmap)):
    tempx=[]
    tempy=[]
    for j in range(len(fmap[i])):
        temp=fmap[i][j].split(',')
        tempx.append(float(temp[0]))
        tempy.append(float(temp[1]))
    curx.append(tempx)
    cury.append(tempy)

curx=np.array(curx)
cury=np.array(cury)

point=[len(curx),0]
route=[point]
y=point[0]
x=point[1]

for i in range(len(curx[0])-1):
    x=x+1
    temp=[]
    if y<4:
        for j in range(3,-1,-1):
            temp.append(curx[y+j][x])
    elif y>len(curx)-4:
        for j in range(1,5):
            temp.append(curx[y-j][x])
    else:
        for j in range(3,1,-1):
            temp.append(curx[y+j][x])
        for j in range(1,3):
            temp.append(curx[y-j][x])
    m=max(temp)
    l=temp.index(m)
    if y<4:
        if l==0:
            y=y+4
        elif l==1:
            y=y+3
        elif l==2:
            y=y+2
        elif l==3:
            y=y+1
        else:
            y=y
    elif y>len(curx)-4:
        if l==0:
            y=y
        elif l==1:
            y=y-1
        elif l==2:
            y=y-2
        elif l==3:
            y=y-3
        else:
            y=y-4
    else:
        if l==0:
            y=y+2
        elif l==1:
            y=y+1
        elif l==2:
            y=y
        elif l==3:
            y=y-1
        else:
            y=y-2
    route.append([y,x])

route.append([0,len(curx[0])])
route=np.array(route)
