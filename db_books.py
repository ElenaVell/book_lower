from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///blog.sqlite')
db_session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String(140), unique=True)
    author = Column(String(200))
    description = Column(Text)
    genre_id = Column(Integer, ForeignKey('genre.id'))
    image = Column(String(500))

    def __init__(self, title=None, author=None, description=None, genre_id=None, image=None):
        self.title = title
        self.image = image
        self.description = description
        self.author = author
        self.genre_id = genre_id

    def __repr__(self):
        return '<Book {} {} {}>'.format(self.title, self.author, self.description)


class Genre(Base):
    __tablename__ = 'genre'
    id = Column(Integer, primary_key=True)
    name = Column(String(140))
    books = relationship('Book', backref='book')

    def __init__(self, name=None):
        self.name = name


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
