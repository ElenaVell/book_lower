from bs4 import BeautifulSoup
from urllib.request import urlopen
from db_books import *

BASE_URL = "https://www.livelib.ru"
def get_all(section_url):
    html = urlopen(section_url).read()
    soup = BeautifulSoup(html, "html.parser")
    books = []
    for item in soup.find_all('tr', class_='column-670 subcontainer version4'):
        book = {}
        img = item.select("a img")[0]
        title = item.find('a', class_='tag-book-title with-cycle')
        author = item.find('a', class_='tag-book-author')
        desc = item.find('p', class_='tag-book-description')
        book['title'] = title['title']
        book['author'] = author['title']
        book['description'] = desc.text
        book['image'] = img['src']
        book['genre'] = 'Юмористическая литература'
        books.append(book) 
        #new_book = Book(**book)
        #db_session.add(new_book)
    return books

    
results = get_all('https://www.livelib.ru/genre/%D0%AE%D0%BC%D0%BE%D1%80%D0%B8%D1%81%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F-%D0%BB%D0%B8%D1%82%D0%B5%D1%80%D0%B0%D1%82%D1%83%D1%80%D0%B0/novelties')
#db_session.commit()
print(results)