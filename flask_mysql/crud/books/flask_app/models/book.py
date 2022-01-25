from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author

db = 'authors_books'

class Book:
    def __init__(self, data):
        self.id = data['id']

        self.title = data['title']
        self.num_of_pages = data['num_of_pages']

        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.fav_by_auth = []

    #--------------------
    # Get all books
    #--------------------
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL(db).query_db(query)
        all_books = []
        for book in results:
            all_books.append(cls(book))
        return all_books

    #--------------------
    # Insert new book
    #--------------------
    @classmethod
    def add_book(cls, data):
        query = """
        INSERT INTO books(title, num_of_pages, created_at, updated_at)
        VALUES (%(title)s, %(num_of_pages)s, NOW(), NOW());
        """
        results = connectToMySQL(db).query_db(query, data)
        return results

    #------------------------------
    # Insert into favorites
    #------------------------------
    @classmethod
    def add_fav(cls, data):
        query = """
        INSERT INTO favorites(book_id, author_id)
        VALUES(%(book_id)s, %(auth_id)s)
        """
        return connectToMySQL(db).query_db(query, data)


    #--------------------------------
    # book favorited by authors
    #--------------------------------
    @classmethod
    def book_fav_by_auth(cls, data):
        query = """
        SELECT * FROM books LEFT JOIN favorites ON books.id = favorites.book_id
        LEFT JOIN authors ON authors.id = favorites.author_id WHERE books.id =  %(book_id)s
        """
        results = connectToMySQL(db).query_db(query, data)
        book_fav = cls(results[0])
        for book in results:
            print(book)
            if book['author_id'] == None:
                break
            data = {
                "id" : book['author_id'],
                "name" : book['name'],
                "created_at" : book['authors.created_at'],
                "updated_at" : book['authors.updated_at']
            }
            book_fav.fav_by_auth.append(author.Author(data))
        return book_fav
