class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_book_borrowed = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

        else:
            return("Book not found")

    def book_borrow(self, book):
        if book not in self.books:
            return("Book not found!")

        elif book.is_book_borrowed:
            return(f"{book.title} is already borrowed.")

        else:
            book.is_book_borrowed = True
            return(f"{book.title} is borrowed successfully.")

    def book_return(self, book):
        if book not in self.books:
            return("Book not found!")

        elif book.is_book_borrowed:
            book.is_book_borrowed = False
            return(f"{book.title} returned successfully.")

        else:
            return(f"{book.title} is already returned")

    def all_books(self):
        for book in self.books:
            print(f"""
=====================================
            {book.title}
=====================================
    
Title: {book.title}
Author: {book.author}
Status: {"Borrowed" if book.is_book_borrowed else "Available"}""")

    def book_search(self, title):
        for book in self.books:
            if book.title == title:
                return(f"{title} is available")

        return(f"{title} not found")

# Create books

book1 = Book("Harry Potter", "J.K. Rowling")
book2 = Book("The Hobbit", "J.R.R. Tolkien")
book3 = Book("Atomic Habits", "James Clear")
book4 = Book("The Alchemist", "Paulo Coelho")
book5 = Book("1984", "George Orwell")


# Create library

library = Library()


# Add all books

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_book(book5)

# Display all books

library.all_books()


# Borrow The Hobbit

print(library.book_borrow(book2))


# Display all books

library.all_books()


# Try borrowing The Hobbit again

print(library.book_borrow(book2))


# Borrow 1984

print(library.book_borrow(book5))


# Display all books

library.all_books()


# Return The Hobbit

print(library.book_return(book2))


# Display all books

library.all_books()


# Try returning The Hobbit again

print(library.book_return(book2))


# Search for Atomic Habits

library.book_search("Atomic Habits")


# Search for a book that doesn't exist

library.book_search("Harry Potter 2")


# Remove The Alchemist

library.remove_book(book4)


# Display all books again

library.all_books()


# Try removing The Alchemist again

library.remove_book(book4)