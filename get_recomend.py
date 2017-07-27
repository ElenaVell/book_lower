from db import User, Post
'''при вызове команды /review дает рекомендацию на основе понравившейся юзеру книги. Бот ищет название
в списках рецензий пользователей сайта www.livlib.ru и если находит - выдает ссылку на другую книгу, которая
также понравилась пользователю сайта. Если книга не найдена - у пользователя спрашивается имя любимого автора.
Если такой автор есть в базе данных - то выдается ссылка на книгу этого автора.'''

def get_recomend(bot,update,user_data = {}):
    user_data['last_command'] = "review"
    mytext = 'Введите название понравившейся книги: '
    update.message.reply_text(mytext)


def review_chat(bot,update, user_data = {}):
	links = Post
	recomends = links.query.all()
	my_book = update.message.text
	my_book = my_book
	for r in range(len(recomends)):
		user = links.query.get(r+1)
		user_book = user.title
		if my_book in user_book:
			r_user = links.query.filter(Post.user_id == user.user_id).order_by(Post.rating.desc()).all()
			for r in r_user:
				if my_book != r.title:
					book=str(r)
					update.message.reply_text(book)
					del user_data['last_command']
					break
    

def get_recomend_by_author_chat(bot,update, user_data = {}):
	mytext = 'Рецензии на данную книгу нет. Введите имя любимого автора: '
	update.message.reply_text(mytext)
	links = Post
	recomends = links.query.all()
	favorit_author = update.message.text
	for r in range(len(recomends)):
		user = links.query.get(r+1)
		user_author = user.book_author
		if favorit_author in user_author:
			r_user = links.query.filter(Post.book_author == user_author).order_by(Post.rating.desc()).first()
			author = str(r_user)
			update.message.reply_text(author)
			del user_data['last_command']
			break
