from db import User, Post

def get_recomend():
	links = Post
	recomends = links.query.all()
	my_book = input()
	for r in range(len(recomends)):
		user = links.query.get(r+1)
		user_book = user.title
		#print(user_book)
		if my_book == user_book:
			r_user = links.query.filter(Post.user_id == user.user_id).order_by(Post.rating.desc()).all()
			for r in r_user:
				if my_book != r.title:
					book=r
					print(book)
					break

get_recomend()
