from crypt import methods
from flask_app import app
from flask import render_template, request, session, redirect
from flask_app.models.author import Author
from flask_app.models.book import Book

@app.route("/authors")
def authors():
    authors = Author.get_all()
    print(authors)
    return render_template('authors.html', authors = authors)

@app.route('/new_author', methods=['POST'])
def add_author():
    data = {
        "name" : request.form['name']
    }
    new_auth = Author.add_author(data)
    print(new_auth)
    return redirect("/authors")

@app.route('/author/<int:author_id>')
def show_one_author(author_id):
    data = {
        "author_id" : author_id
    }
    all_books = Book.get_all()
    author = Author.auth_fav_book(data)
    return render_template("authors_fav.html", all_books = all_books , author = author)

@app.route('/book/add', methods=['POST'])
def auth_fav():
    print(request.form)
    data = {
        "book_id" : request.form['book_id'],
        "author_id" : request.form['author_id']
    }
    Author.add_fav(data)
    return redirect(f"/author/{request.form['author_id']}")
