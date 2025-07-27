# Django CRUD Operations Documentation

This document contains all CRUD operations performed on the Book model in the Django shell.

## Model Definition
```python
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()