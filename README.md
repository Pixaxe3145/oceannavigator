# oceannavigator

Hello. this is my new project, OceanNavigator.

Used libraries: os, selenium, numpy, pandas, pillow, time

Please change the path inside os.chdir()

This project is mainly made out of 6 seperate codes.

1. type in latlong.py\
  This code makes you available to type in destination and deperture latitude/longtitude.\
  It saves 4 data as string, in "latlong.txt" file.

2. image_capture+merge.py\
  This code automatically reades latlong.txt and captures the map in many pices.\
  Then it merges the map into one image, "final.png".\
  *IMPORTANT!* Please respect etiquettes and manners when crawling from web.\
  *IMPORTANT!* As tested, it seems like google blocks the IP when the captured image number is over than 330.

3. image_analize.py\
  This code analizes the image and saves "final_map.xlsx".\
  The excel file indicates where the ship can go, where it can't go by 0 and 1.
  
4. seleniumcrawling.py\
  This code gets current data from a site called nullschoolearth.\
  It returns a webdriverobject. We can get text data from aa.text.\
  Then it finally saves the data to a list named C.\
  Finally it saves the data into "final_current.xlsx".\
  *IMPORTANT!* Please respect etiquettes and manners when crawling from web.\
5. data_mod.py\
  This code reads "final_map.xlsx" and "final_current.xlsx".\
  It modifies map data and rewrites current data as current-x component and current-y component.
  
6. image_cropping.py\
  This code makes the image "crimage.png".\
  It is made out of image("final.png") and it is needed for visualizing the route. 
  
7. shortest_route.py\
  making!
