import requests
import pandas as pd
import regex as re
from bs4 import BeautifulSoup
url = "https://indianexpress.com/l"
r = requests.get(url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent, 'html.parser')





anchors = soup.find_all('a')
all_links = set()
# Get all the links on the page:
for link in anchors:
    if(link.get('href') != '#'): 
        linkText = "" +link.get('href')
        all_links.add(link)
        print(linkText)




def get_video_links():
  #create response object
  r = requests.get("https://indianexpress.com/l")
  #create beautiful-soup object
  soup = BeautifulSoup(r.content,'html5lib')
  #find all links on web-page
  links = soup.findAll('a')
  #filter the link ending with .mp4
  video_links = ["https://indianexpress.com/l" + link['href'] for link in links if link['href'].endswith('mp4')]
  #return(video_links)
  print(video_links)

get_video_links()

#this will give the address or source of the image you can use ctrl+click to reach image again this can be used for personal use



images = soup.find_all('img')
  
for item in images:
   print(item['src'])

#all the videos present on the website can be accessed through this without going on website you can also use this to embed videos in your own websites or personal use


'''videos = soup.find_all('mp3')
 
for item in videos:
    print(item['src'])'''

#this line of code will get you the header of website if there is no header it will return null set

header = soup.find('header')
print(header)


