from bs4 import BeautifulSoup
from urllib.request import urlopen
from db import *
import datetime
from test import *
import time
#from parse_users import *

BASE_URL = "https://www.livelib.ru"

BROWSERS = [
    "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11",
    ""
]

def get_gender(section_url):
    print("Fetching URL '{}'".format(section_url))
    resp = urlopen(section_url)
    if resp.getcode() != 200:
        print("Returned code {}, this user skipped".format(resp.getcode()))
        return []
    html = resp.read()
    soup = BeautifulSoup(html, "html.parser")
    users = []
    profile_info = soup.find_all('div', class_='profile-info-column')
    if profile_info == []:
        #print(html)
        print("Please visit URL '{}' and enter Captcha by hands".format(section_url))
        time.sleep(70)
        profile_info = soup.find_all('div', class_='profile-info-column')
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
