# Admin Interface Setup for Book Model

## Steps Taken:
1. Registered the Book model with the Django admin in `admin.py`.
2. Customized the admin interface with:
   - `list_display = ['title', 'author', 'publication_year']` to show key fields.
   - `search_fields = ['title', 'author']` for search functionality.
   - `list_filter = ['publication_year']` for filtering by publication year.
3. Applied migrations with `python manage.py makemigrations` and `python manage.py migrate`.
4. Created a superuser with `python manage.py createsuperuser` and tested the admin at `http://127.0.0.1:8000/admin/`.

## Expected Outcome:
- The admin interface should display a list of books with title, author, and publication_year.
- Search and filter options should be functional.