import urllib
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote_plus


def get_url(section_url):
    html = urlopen(section_url).read()
    soup = BeautifulSoup(html, "html5lib")
    all = soup.find('a', class_="title")
    if all:
        href = all['href']
        return href
    else:
        return None


def get_review(section_url):
    html = urlopen(section_url).read()
    soup = BeautifulSoup(html, "html5lib")
    counter = 0
    id = 'none'
    for item in soup.find_all('span', class_="vote action action-text"):
        if int(item.text) > counter:
            counter = int(item.text)
            id = item['id']
    word = []
    word = id.split('-')
    new_id = word[3] + '-' + word[4]
    review = soup.find(id=new_id)
    desc = review.find('div', class_="description")
    return desc.text


print("Привет!")
while True:
    try:
        book_name = input('Назови книгу :   \n').strip()
        changed_name = quote_plus(book_name)
        BASE_URL = "https://www.livelib.ru"
        url_to_find = BASE_URL + '/find/' + changed_name
        book_adress = get_url(url_to_find)
        if book_adress:
            final_url = BASE_URL + book_adress
            print(get_review(final_url)) 
        else:
            print(" Не получается найти такую книгу(")
        break
    except EOFError:
        print(" Напиши название маленькими буквами!")
