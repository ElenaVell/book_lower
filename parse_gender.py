from bs4 import BeautifulSoup
from urllib.request import urlopen
from db import *
import datetime
from test import *
#from parse_users import *

BASE_URL = "https://www.livelib.ru"

def get_gender(section_url):
    resp = urlopen(section_url)
    html = resp.read()
    soup = BeautifulSoup(html, "html.parser")
    users = []
    profile_info = soup.find_all('div', class_='profile-info-column')
    if profile_info == []:
        print(html)
    for item in profile_info:
        user = {}
        gender = item.select('span')[1]
        user['gender'] = gender.get_text()
        users.append(user)
        #new_user = User(**user)
        #db_session.add(new_user)
    #db_session.commit()
    return users

if __name__ == "__main__":
    links = users_url()
    for u in links:
        result_gender = get_gender(u)
        print(result_gender)