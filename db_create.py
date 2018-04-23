from app import db
from app.models import Book

# db.drop_all()
db.create_all()

hello_books = Book(title='Hello Books', isbn='12345-67-890', synopsis='First Book', author='Arnold Odhiambo')

db.session.add(hello_books)
db.session.commit()
