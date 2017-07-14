from bs4 import BeautifulSoup
from urllib.request import urlopen
from db import *
import datetime

BASE_URL = "https://www.livelib.ru"
def get_all(section_url):
    html = urlopen(section_url).read()
    soup = BeautifulSoup(html, "html.parser")
    users = []
    
    for item in soup.find_all('div', class_='row'):
        user = {}
        nickname = item.find('span', class_='reader')
        nickname = nickname.find('a')
        profile_url = item.find('span', class_='reader')
        profile_url = profile_url.find('a')
        reviews_url = item.find('div', class_='actionbar bar-vertical mmarg')
        reviews_url = reviews_url.find('a', class_='action')
        user['nickname'] = nickname.get('title')
        user['profile_url'] = profile_url.get('href')
        user['last_process'] = datetime.datetime.now()
        user['reviews_url'] = 'https://www.livelib.ru' + reviews_url.get('href') + '/reviews'
        users.append(user) 
        new_user = User(**user)
        db_session.add(new_user)
    return users
   
results = get_all('https://www.livelib.ru/readers/~5')
db_session.commit()
print(results)


