```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
# Deleting the book instance
book.delete()
Book.objects.all()