from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, Float, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///users_1.sqlite')

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    nickname = Column(String(50), unique=True)
    gender = Column(String(50))
    last_process = Column(DateTime)
    profile_url = Column(String)
    reviews_url = Column(String)
    posts = relationship('Post', backref='author')

    def __init__(self, nickname=None, gender=None, last_process=None, profile_url=None, reviews_url=None):
        self.nickname = nickname
        self.gender = gender
        self.last_process = last_process
        self.profile_url = profile_url
        self.reviews_url = reviews_url

    def __repr__(self):
        return '<User {} {} >'.format(self.profile_url, self.reviews_url)

class Post(Base):
	__tablename__ = 'posts'
	id = Column(Integer, primary_key=True)
	title = Column(String(140))
	book_author = Column(String(100))
	image = Column(String(500))
	rating = Column(Float)
	content = Column(Text)
	nickname = Column(String(50))
	user_id = Column(Integer, ForeignKey('users.id'))

	def __init__(self, title=None, book_author=None, image=None, rating=None, content=None, nickname=None, user_id=None):
		self.title = title
		self.book_author = book_author
		self.image = image
		self.rating = rating
		self.content = content
		self.nickname = nickname
		self.user_id = user_id

	def __repr__(self):
		return '<Post {} {} {} {} >'.format(self.title, self.book_author, self.image, self.content)
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)