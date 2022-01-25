from flask_app import app
from flask import render_template, request, session, redirect
from flask_app.models.author import Author
from flask_app.models.book import Book

@app.route('/books')
def new_book():
    all_books = Book.get_all()
    return render_template('books.html', all_books = all_books)

@app.route('/new_book', methods=['POST'])
def add_book():
    data = {
        'title' : request.form['title'],
        'num_of_pages' : request.form['num_of_pages']
    }
    new_book = Book.add_book(data)
    print(new_book)
    return redirect('/books')

#---------------------------------
# Add books favorite by authors
#---------------------------------

@app.route('/book/<int:book_id>')
def show_book_and_auth(book_id):
    data = {
        "book_id" : book_id
    }
    book = Book.book_fav_by_auth(data)
    auths = Author.get_all()
    return render_template('book_fav.html', book = book, auths = auths)

@app.route('/auth/add', methods=['POST'])
def book_fav():
    print(request.form)
    data = {
        "auth_id" : request.form['auth_id'],
        "book_id" : request.form['book_id']
    }
    Book.add_fav(data)
    return redirect(f"/book/{request.form['book_id']}")