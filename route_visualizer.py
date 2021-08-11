import os
import pandas as pd
import numpy as np
from PIL import Image

os.chdir("F:\project\오션_2021\captures")

image=Image.open("crimage.png")
pix = np.array(image)
red=np.array([255,0,0], dtype='uint8')

route_final=Image.fromarray(pix)
route_final.save("route_final.png")