from selenium import webdriver
import time
import webbrowser
import os

os.chdir("F:\project\오션_2021")

lat=float(input('위도:'))
lon=float(input('경도:'))

lat=round(lat,7)
lon=round(lon,7)

lat=str(lat)
lon=str(lon)

wd = webdriver.Chrome(r'F:\project\오션_2021\chromedriver.exe')
url = 'https://www.google.com/maps/@'+lat+','+lon+',10z?hl=ko'
wd.get(url)
time.sleep(1)
#text = wd.page_source
#print(text)

wd.save_screenshot('screenshot.png')
webbrowser.open('screenshot.png')

wd.quit()
