from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///book.sqlite')

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String(140), unique=True)
    author = Column(String(200))
    description = Column(Text)
    image = Column(String(500))
    genre = Column(String(50))

    def __init__(self, title=None, author=None, description=None, image=None, genre=None):
        self.title = title
        self.image = image
        self.description = description
        self.author = author
        self.genre = genre

    def __repr__(self):
        return '<Book {} {} {} {} {}>'.format(self.title,self.author, self.image, self.description, self.genre)

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine) 

        