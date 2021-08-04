import os

A=list(map(float,input("departure latitude, longtitude:").split()))
slat, slon=A[0],A[1]
B=list(map(float,input("destination latitude, longtitude:").split()))
elat, elon=B[0],B[1]
data=[slat,slon,elat,elon]

os.chdir("F:\project\오션_2021")

f=open(".\latlong.txt",'w')

for i in range(len(data)):
    f.write(str(data[i]))
    f.write("\n")
f.close()