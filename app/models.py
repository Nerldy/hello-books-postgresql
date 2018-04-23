from app import db
from datetime import datetime as dt


def _get_date():
	return dt.now()


class Book(db.Model):
	"""this class describes a book table"""
	__tablename__ = 'books'
	id = db.Column(db.Integer, primary_key=True)
	book_title = db.Column(db.String, nullable=False)
	book_isbn = db.Column(db.String, nullable=False, unique=True)
	book_synopsis = db.Column(db.Text, nullable=False)
	book_author = db.Column(db.String, nullable=False)
	date_created = db.Column(db.DateTime, default=_get_date)

	def __init__(self, title, isbn, author, synopsis):
		self.book_title = title
		self.book_isbn = isbn
		self.book_synopsis = synopsis
		self.book_author = author

	def __repr__(self):
		return f'<title {self.book_title}'
