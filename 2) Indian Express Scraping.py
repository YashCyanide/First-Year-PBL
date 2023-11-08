# import module
import requests
import pandas as pd
from bs4 import BeautifulSoup

# link for extract html data  >>>

def getdata(url):
	r = requests.get(url)
	return r.text

#Entering The Website URL >>>

htmldata = getdata("https://indianexpress.com/article/explained/everyday-explainers/what-is-hermit-spyware-explained-7995895/")
soup = BeautifulSoup(htmldata, 'html.parser')
data = ''

#Initializing loop >>>

for data in soup.find_all("p"):
	print(data.get_text())
