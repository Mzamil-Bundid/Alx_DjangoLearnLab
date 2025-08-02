import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


def query_books_by_author(author_name):
    """
    Query all books by a specific author
    """
    try:
        # Get the author object
        author = Author.objects.get(name=author_name)
        
        # Query all books by this author using the ForeignKey relationship
        books = Book.objects.filter(author=author)
        
        print(f"\nBooks by {author_name}:")
        print("-" * 30)
        for book in books:
            print(f"- {book.title}")
        
        # Alternative approach using related_name
        books_alternative = author.books.all()
        print(f"\nAlternative query - Books by {author_name}:")
        print("-" * 30)
        for book in books_alternative:
            print(f"- {book.title}")
            
        return books
        
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found.")
        return None


def list_books_in_library(library_name):
    """
    List all books in a library
    """
    try:
        # Get the library object
        library = Library.objects.get(name=library_name)
        
        # Query all books in this library using the ManyToMany relationship
        books = library.books.all()
        
        print(f"\nBooks in {library_name}:")
        print("-" * 30)
        for book in books:
            print(f"- {book.title} by {book.author.name}")
            
        return books
        
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
        return None


def retrieve_librarian_for_library(library_name):
    """
    Retrieve the librarian for a library
    """
    try:
        # Get the library object
        library = Library.objects.get(name=library_name)
        
        # Get the librarian using OneToOne relationship via objects.get
        librarian = Librarian.objects.get(library=library)
        
        print(f"\nLibrarian for {library_name}:")
        print("-" * 30)
        print(f"- {librarian.name}")
        
        return librarian
        
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
        return None
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to '{library_name}'.")
        return None


def sample_data_creation():
    """
    Create sample data for testing queries
    """
    print("Creating sample data...")
    
    # Create authors
    author1, created = Author.objects.get_or_create(name="J.K. Rowling")
    author2, created = Author.objects.get_or_create(name="George Orwell")
    author3, created = Author.objects.get_or_create(name="Jane Austen")
    
    # Create books
    book1, created = Book.objects.get_or_create(
        title="Harry Potter and the Philosopher's Stone",
        author=author1
    )
    book2, created = Book.objects.get_or_create(
        title="Harry Potter and the Chamber of Secrets",
        author=author1
    )
    book3, created = Book.objects.get_or_create(
        title="1984",
        author=author2
    )
    book4, created = Book.objects.get_or_create(
        title="Animal Farm",
        author=author2
    )
    book5, created = Book.objects.get_or_create(
        title="Pride and Prejudice",
        author=author3
    )
    
    # Create libraries
    library1, created = Library.objects.get_or_create(name="Central Library")
    library2, created = Library.objects.get_or_create(name="University Library")
    
    # Add books to libraries
    library1.books.add(book1, book2, book3)
    library2.books.add(book3, book4, book5)
    
    # Create librarians
    librarian1, created = Librarian.objects.get_or_create(
        name="Alice Johnson",
        library=library1
    )
    librarian2, created = Librarian.objects.get_or_create(
        name="Bob Smith",
        library=library2
    )
    
    print("Sample data created successfully!")


def main():
    """
    Main function to demonstrate all query samples
    """
    print("Django ORM Query Samples")
    print("=" * 40)
    
    # Create sample data
    sample_data_creation()
    
    # Demonstrate queries
    print("\n" + "=" * 40)
    print("QUERY DEMONSTRATIONS")
    print("=" * 40)
    
    # Query 1: All books by a specific author
    query_books_by_author("J.K. Rowling")
    query_books_by_author("George Orwell")
    
    # Query 2: List all books in a library
    list_books_in_library("Central Library")
    list_books_in_library("University Library")
    
    # Query 3: Retrieve the librarian for a library
    retrieve_librarian_for_library("Central Library")
    retrieve_librarian_for_library("University Library")


if __name__ == "__main__":
    main()