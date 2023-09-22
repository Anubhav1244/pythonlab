import os
import requests
from bs4 import BeautifulSoup

url='https://xkcd.com/1/'
os.makedirs('xcd')
while(True):
    res=requests.get(url)
   
    soup=BeautifulSoup(res.text,"html.parser")
    
    comic=soup.select('#comic img')
    if comic==[]:
        print("no element in the comic")
    else:
        comic_url='https:'+comic[0].get('src')
        print(f'downloading {comic_url}...')
        res=requests.get(url)
        
        image_file = open(os.path.join('xcd', os.path.basename(comic_url)), 'wb')
        for chunk in res.iter_content(10000):
            image_file.write(chunk)
        image_file.close()
    perv_link=soup.select('a[rel="prev"]')[0]
    
    if not perv_link:
        break
    url='https://xkcd.com'+perv_link.get('href')

