import requests
from bs4 import BeautifulSoup
import urllib
import time
import os 

base = "http://archillect.com/"

BEGINNING_POST_NUM = 207202
END_POST_NUM = 150000

current_post = BEGINNING_POST_NUM

folder_size = 0

while(current_post > END_POST_NUM):
    print(current_post)
    r = requests.get(base + str(current_post)).text
    soup = BeautifulSoup(r, features="html.parser")
    img_url = ''
    try:
	img_url = soup.find(id="ii")['src']
    except:
	current_post -= 1 
	continue
    path =  "./images/" + str(current_post) + ".png"
    urllib.urlretrieve(img_url, path )
    current_post -= 1
    #time.sleep(.25)

    file_size = os.path.getsize(path)
    folder_size += file_size
    if folder_size > 50000000000:
	print('too many images downloaded, upload to google photos')
	print('last image added : ' + current_post)
	sys.exit
