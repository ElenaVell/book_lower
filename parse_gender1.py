from bs4 import BeautifulSoup
from urllib.request import urlopen
from db import *
import datetime
from test import *
#from parse_users import *

BASE_URL = "https://www.livelib.ru"

def get_gender(section_url):
    html = urlopen(section_url).read()
    soup = BeautifulSoup(html, "html.parser")
    users = []
    for item in soup.find_all('div', class_='profile-info-column'):
        user = {}
        gender = item.select('span')[1]
        user['gender'] = gender.get_text()
        users.append(user)
        #new_user = User(**user)
        #db_session.add(new_user)
    #db_session.commit()
    return users
result_gender = get_gender('https://www.livelib.ru/reader/lustdevildoll')
print(result_gender)