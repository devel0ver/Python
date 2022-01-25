from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

db = 'authors_books'

class Author:
    def __init__(self, data):
        self.id = data['id']

        self.name = data['name']

        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.authors_favorite = []

    #---------------------------
    # get all from authors
    #---------------------------
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL(db).query_db(query)
        all_authors = []
        for author in results:
            all_authors.append(cls(author))
        print(results)
        return all_authors
    
    #---------------------------
    # insert in authors
    #---------------------------
    @classmethod
    def add_author(cls, data):
        query = """
        INSERT INTO authors(name, created_at, updated_at)
        VALUES (%(name)s, NOW(), NOW());
        """
        results = connectToMySQL(db).query_db(query, data)
        return results

    #------------------------------------
    # Authors that not favorited any book
    #------------------------------------
    @classmethod
    def auth_not_fav(cls, data):
        query = """
        SELECT * FROM authors WHERE authors.id 
        NOT IN (SELECT author_id FROM favorites WHERE book_id = %(book_id)s)
        """
        results = connectToMySQL(db).query_db(query, data)
        authors = []
        for auth in results:
            authors.append(cls(auth))
        return authors
    

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM authors WHERE id = %(author_id)s;"
        results = connectToMySQL(db).query_db(query, data)
        print(results)
        return cls(results[0])
    
    #------------------------------
    # Insert into favorites
    #------------------------------
    @classmethod
    def add_fav(cls, data):
        query = """
        INSERT INTO favorites(book_id, author_id)
        VALUES (%(book_id)s, %(author_id)s)
        """
        return connectToMySQL(db).query_db(query, data)
    
    #-------------------------------
    # Author favorite books
    #-------------------------------
    @classmethod
    def auth_fav_book(cls, data):
        query = """
        SELECT * FROM authors LEFT JOIN favorites ON authors.id = favorites.author_id
        LEFT JOIN books ON books.id = favorites.book_id WHERE authors.id =  %(author_id)s
        """
        results = connectToMySQL(db).query_db(query, data)
        author_fav = cls(results[0])
        for row in results:
            print(row)
            if row['book_id'] == None:
                break
            data = {
                "id" : row['book_id'],
                "title" : row['title'],
                "num_of_pages" : row['num_of_pages'],
                "created_at" : row['books.created_at'],
                "updated_at" : row['books.updated_at']
            }
            author_fav.authors_favorite.append(book.Book(data))
        return author_fav