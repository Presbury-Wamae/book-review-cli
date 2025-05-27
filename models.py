# models.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    genre = Column(String)

    reviews = relationship("Review", back_populates="book", cascade="all, delete")

    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}', author='{self.author}')>"

class Reader(Base):
    __tablename__ = 'readers'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    reviews = relationship("Review", back_populates="reader", cascade="all, delete")

    def __repr__(self):
        return f"<Reader(id={self.id}, name='{self.name}')>"

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    rating = Column(Integer)
    comment = Column(String)
    book_id = Column(Integer, ForeignKey('books.id'))
    reader_id = Column(Integer, ForeignKey('readers.id'))

    book = relationship("Book", back_populates="reviews")
    reader = relationship("Reader", back_populates="reviews")

    def __repr__(self):
        return (
            f"<Review(id={self.id}, rating={self.rating}, "
            f"book_id={self.book_id}, reader_id={self.reader_id})>"
        )
