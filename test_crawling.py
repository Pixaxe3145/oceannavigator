from urllib.request import urlopen 
from urllib.request import Request
from bs4 import BeautifulSoup

hdr={'User-Agent':'Mozilla/5.0'} 
url="https://earth.nullschool.net/ko/#current/wind/surface/level/orthographic/loc=141.898,35.943"

req=Request(url,headers=hdr)
html=urlopen(req).read()
soup = BeautifulSoup(html, 'html.parser')

aa=soup.find_all(class_="vert-unchanged row")

print(aa)
#for j in aa:
#    print(aa.attrs['aria-label'])