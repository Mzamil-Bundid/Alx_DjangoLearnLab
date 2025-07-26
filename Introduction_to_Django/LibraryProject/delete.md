# Delete Operation

## Command Used:
```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
print("Book deleted successfully")

# Confirm deletion
all_books = Book.objects.all()
print(f"All books after deletion: {all_books}")