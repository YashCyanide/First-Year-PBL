from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
url = "https://www.flipkart.com/search?q=samsung%20phones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
req = requests.get(url)
content = BeautifulSoup(req.content,'html.parser')

# MAIN WEBPAGE BOX CLASS

data=content.find_all('div',{'class':'_2kHMtA'})
links=[] 
title=[]
prices=[]
ratings = []
start_link="https://www.flipkart.com"
for items in data:
  rest_link=items.find('a')['href']

  #PRICES

  price = items.find('div', attrs={'class':'_30jeq3 _1_WHN1'})

  #RATINGS

  rating = items.find('div', attrs={'_3LWZlK'})

  #TITLE

  name=items.find('div', attrs={'class':'_4rR01T'}) 

  title.append(name.text) 
  links.append(start_link+rest_link)
  prices.append(price.text)
  ratings.append(rating.text)
dataframe = {'Title':title, 'Links':links , 'Prices':prices , 'Ratings' : ratings}
Final_dataframe=pd.DataFrame(dataframe) 
print(Final_dataframe)

# ALL DATA TO EXCEL SHEET >>>>

Final_dataframe.to_csv('samsung.csv')