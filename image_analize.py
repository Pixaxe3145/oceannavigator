from PIL import Image
import numpy as np
import pandas as pd
import os

os.chdir("F:\project\오션_2021\captures")

img_name = ('final.png')
im = Image.open(img_name)
pix = np.array(im)

b1=np.array([241,233,215], dtype='uint8')
b2=np.array([187,226,198], dtype='uint8')
b3=np.array([232,234,237], dtype='uint8')

w, h=im.size[0], im.size[1]
ws=w//70
hs=h//70

A=np.ones((hs,ws))

for i in range(ws):
    for j in range(hs):
        for wc in range(i*70,(i+1)*70-1):
            for hc in range(j*70,(j+1)*70-1):
                if np.array_equal(pix[hc][wc],b1)==True:
                    A[j][i]=0
                elif np.array_equal(pix[hc][wc],b2)==True:
                    A[j][i]=0
                elif np.array_equal(pix[hc][wc],b3)==True:
                    A[j][i]=0
                else:
                    pass

final_map=pd.DataFrame(A)

os.chdir("F:\project\오션_2021")
final_map.to_excel('final_map.xlsx', index=False)