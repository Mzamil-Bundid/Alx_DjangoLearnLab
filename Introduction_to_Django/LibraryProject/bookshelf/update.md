## Update the title of the Book instance

**Python command:**
```python
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)
# Expected output: Nineteen Eighty-Four
```
**Expected output:**  
The Book instance's title is updated to "Nineteen Eighty-Four". The print statement confirms the