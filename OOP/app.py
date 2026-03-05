# Library Management Web Application
# This Flask app provides a web interface for managing a library's book collection.
# Users can view available books, add new books, borrow books, and return books.

from flask import Flask, request, render_template, redirect, url_for
from functions import Book, Library

# Create Flask application instance
app = Flask(__name__)

# Initialize the library database connection
lib = Library()

# Route for the home page: displays available books and handles book actions
@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        # Get form data
        action = request.form.get('action')
        title = request.form.get('title').lower()  # Convert to lowercase for case-insensitive matching
        author = request.form.get('author').lower()
        
        # Handle different actions
        if action == 'add':
            book = Book(title, author)
            lib.add_book(book)
        elif action == 'borrow':
            book = Book(title, author)
            lib.borrow_book(book)
        elif action == 'return':
            book = Book(title, author)
            lib.return_book(book)
        
        # Redirect to refresh the page
        return redirect(url_for('index'))
    
    # Get available books for display
    available_books = lib.get_available_books()
    return render_template('index.html', books=available_books)