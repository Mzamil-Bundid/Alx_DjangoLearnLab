## Create a Book instance

**Python command:**
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)
# Expected output: <Book: Book object (1)>  # The number may vary depending on your database state
```
**Expected output:**  
A new Book instance is created with the specified title, author, and publication year. The print statement outputs the Book