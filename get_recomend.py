from db import User, Post

def get_recomend():
	links = Post
	recomends = links.query.all()
	my_book = input('Введите название понравившейся книги: ', )
	my_book = my_book.lower()
	for r in range(len(recomends)):
		user = links.query.get(r+1)
		user_book = user.title.lower()
		if my_book in user_book:
			r_user = links.query.filter(Post.user_id == user.user_id).order_by(Post.rating.desc()).all()
			for r in r_user:
				if my_book != r.title:
					book=r
					return book
					break

def get_recomend_by_author():
	links = Post
	recomends = links.query.all()
	favorit_author = input('Рецензии на данную книгу нет. Введите имя любимого автора: ', )
	for r in range(len(recomends)):
		user = links.query.get(r+1)
		user_author = user.book_author
		if favorit_author in user_author:
			r_user = links.query.filter(Post.book_author == user_author).order_by(Post.rating.desc()).first()
			return r_user
			break



if __name__ == "__main__":
	first_review = get_recomend()
	print(first_review)
	if first_review == None:
		second_review = get_recomend_by_author()
		print(second_review)
