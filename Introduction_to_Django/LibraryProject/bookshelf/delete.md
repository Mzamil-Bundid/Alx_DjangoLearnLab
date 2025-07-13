## Delete the Book instance

**Python command:**
```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
print(Book.objects.all())
# Expected output: <QuerySet []>
```
**Expected output:**  
The Book instance is deleted. Retrieving all books returns an empty