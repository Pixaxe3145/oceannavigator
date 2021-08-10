import os
from PIL import Image

os.chdir("F:\project\오션_2021")

f=open(".\imcrop.txt",'r')

A=[]
for i in range(2):
    line=f.readline()
    A.append(line)
f.close()

w=int(A[0])
h=int(A[1])

ww=w*74
hh=h*71

os.chdir("F:\project\오션_2021\captures")

image=Image.open("final.png")

hhh=int(image.size[1])

crimage=image.crop((464,hhh-444-hh,ww+464,hhh-444))
crimage.save("crimage.png")
