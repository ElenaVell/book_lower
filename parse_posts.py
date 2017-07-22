from bs4 import BeautifulSoup
from urllib.request import urlopen
from db import *
from post_links import *

def get_reviews(section_url):
	html = urlopen(section_url).read()
	if html:

		bs = BeautifulSoup(html, 'html.parser')
		reviews =[]
		u = User

		for item in bs.find_all(itemprop='review'):
			review = {}
			title = item.find('span', class_='book-title')
			title = title.find('a')
			book_author = item.find('span', class_='book-author')
			book_author = book_author.find('a')
			image = item.find('img')
			rating=item.find('div', class_='event-rating')
			#import ipdb; ipdb.set_trace()
			if rating == None:
				rating = '0'
				review['rating'] = rating
			else:
				rating=rating.find_all('span')[0]
				review['rating'] = rating.text
			content = item.find('div', class_='description')
			nickname = item.find(itemprop ='author')
			review['title'] = title.get('title')
			review['book_author'] = book_author.get('title')
			review['image'] = image.get('src')
			review['content'] = content.text
			review['nickname'] = nickname.text
			reviews.append(review)
			#print(reviews)
		for row in reviews:
			author = u.query.filter(User.nickname == row['nickname']).first()
			row['user_id'] = author.id
		for r in reviews:
			post = Post(r['title'], r['book_author'], r['image'], r['rating'], r['content'], r['nickname'], r['user_id'])
			db_session.add(post)
		
		return reviews

		
	else:
		print('Что-то пошло не правильно')

if __name__ == "__main__":
	#results = get_reviews('https://www.livelib.ru/reader/Arlett/reviews')
	#db_session.commit()
	#print(results)
    links = users_url()
    for u in links[16::]:
    	result_reviews = get_reviews(u)
    	db_session.commit()
    	print(u)

			
	
	
