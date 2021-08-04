from PIL import Image
import os

os.chdir("F:\project\오션_2021\captures")

# 1. 병합할 이미지 만들기
merged = Image.new('L', (929*2,888*2))

for i in range(2):
    for j in range(2):
        # 2. 이미지 불러오기
        im = Image.open(str(i)+str(j)+'.png')

        # 3. 이미지 붙여넣기
        merged.paste(im, (929*j, 888*(1-i)))

# 4. 병합한 이미지 저장하기
merged.save('final.png')