# Delete Operation

## Command Used:
```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
books_count = Book.objects.count()
print(f"Books remaining: {books_count}")