
from sqlalchemy import Column, String, Integer, Text

from app import db

import os

class Book(db.Model):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True)
    isbn = Column(String(13))
    author = Column(String(255))
    title = Column(Text)

try:
    os.remove("sample.db")
except:
    pass

db.create_all()

book1 = Book()
book1.isbn = "1795234318"
book1.author = "Anthony Brun"
book1.title = "Python Programming: A Step By Step Guide From Beginner To Expert (Beginner, Intermediate & Advanced)"

book2 = Book()
book2.isbn = "9781617294433"
book2.author = "Francois Chollet"
book2.title = "Deep Learning with Python"

db.session.add(book1)
db.session.add(book2)
db.session.commit()
