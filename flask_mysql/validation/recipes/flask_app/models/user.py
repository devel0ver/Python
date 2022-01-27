from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

db = "user_recipes"

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def user_valid(data):
        is_valid = True
        if len(data['first_name']) < 3:
            flash("First name must be at least 3 characters")
            is_valid = False
        if len(data['last_name']) < 3:
            flash("Last name must be at least 3 characters")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid Email!!!")
            is_valid = False
        if User.get_by_email(data):
            flash("Email is already in use! Please use another email.")
            is_valid = False
        if len(data['password']) < 8:
            flash("Password must be at least 8 characters")
            is_valid = False
        if data['password'] != data['conf_pass']:
            flash("Password Must Match Confirmation Password")
            is_valid = False
        return is_valid

    @staticmethod
    def login_validate(data):
        is_valid = True
        user_in_db = User.get_by_email(data)
        if not user_in_db:
            flash("Invalid Credentials!")
            is_valid = False
        elif not bcrypt.check_password_hash(user_in_db.password, data['password']):
            flash("Invalid Credentials!")
            is_valid = False
        return is_valid

    @classmethod
    def create_user(cls, data):
        query = """
        INSERT INTO users (first_name, last_name, email, password, created_at)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW());
        """
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(db).query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(user_id)s;"
        result = connectToMySQL(db).query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])