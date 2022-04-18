import pandas as pd
import requests #For Http Requests
from bs4 import BeautifulSoup #Web Scraping

r = requests.get('https://www.game.tv/')
soup = BeautifulSoup(r.content, 'html.parser')
game = soup.find_all ('li',attrs={'class',"games-item"})
gamelist = []
for j in game:
   game_detail = {}
   url = j.find('a')
   newurl = 'https://www.game.tv/' + url['href']
   r2=requests.get(newurl)
   #print(j.text ,newurl,r2.status_code) 
   game_detail['Gamename']=str(j.text).strip()
   game_detail['Url']=newurl
   game_detail['Status Code']=r2.status_code
   gamelist.append(game_detail)
#print (gamelist)
dataFrame = pd.DataFrame.from_dict(gamelist)   
print (dataFrame.head(20))
dataFrame.to_csv('gamelist.csv', index=False)