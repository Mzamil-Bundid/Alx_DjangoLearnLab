## Retrieve the Book instance

**Python command:**
```python
retrieved_book = Book.objects.get(id=book.id)
print(retrieved_book.title, retrieved_book.author, retrieved_book.publication_year)
```

**Output:**
```
Django Basics Jane Doe 2024
```