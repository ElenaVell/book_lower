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


try:
    def reader(bot,update,user_data={}):   
        mytext= 'Привет! Назови книгу{}:?'.format(update.message.chat.first_name)
        update.message.reply_text(mytext)
        user_data['key']=True
    def chat(bot,update,user_data={}):    
        book_name = update.message.text
        print(book_name)
        changed_name = quote_plus(book_name)
        BASE_URL = "https://www.livelib.ru"
        url_to_find = BASE_URL + '/find/' + changed_name
        print(url_to_find)
        book_adress = get_url(url_to_find)
        print(book_adress)
        if book_adress:
            final_url = BASE_URL + book_adress
            print(final_url)
            if len(get_review(final_url)) > 4000:
                print(get_review(final_url))
                update.message.reply_text(get_review(final_url)[:4000])
                update.message.reply_text(get_review(final_url)[4000:])
            else:
                update.message.reply_text(get_review(final_url))

        else:
            update.message.reply_text(' Не получается найти такую книгу(')
except EOFError:
    update.message.reply_text('Напиши название маленькими буквами')
    print(" Напиши название маленькими буквами!")

