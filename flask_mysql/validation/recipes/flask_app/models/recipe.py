from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user import User

db = "user_recipes"

class Recipe:
    def __init__(self, data):
        self.id = data["id"]

        self.name = data["name"]
        self.description = data["description"]
        self.instruction = data["instruction"]
        self.time = data["time"]
        self.user_id = data["user_id"]
        self.date = data["date"]

        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        self.user = {}

    @staticmethod
    def recipe_validate(data):
        is_valid = True
        if len(data["name"]) < 3:
            flash("Name must be at least 3 characters long")
            is_valid = False
        if len(data["description"]) < 5:
            flash("Description must be at least 5 characters long")
            is_valid = False
        if len(data["instruction"]) < 3:
            flash("Description must be at least 3 characters long")
            is_valid = False
        if data["date"] == "":
            flash('Please enter a date')
            is_valid = False
        return is_valid
    
    @classmethod
    def add_recipe(cls, data):
        query = """
        INSERT INTO recipes (name, description, instruction, time, date, user_id, created_at)
        VALUES (%(name)s, %(description)s, %(instruction)s, %(time)s, %(date)s, %(user_id)s, NOW());
        """
        results = connectToMySQL(db).query_db(query, data)
        return results
    

    @classmethod
    def get_recipe_w_user(cls, data):
        query = """
        SELECT * FROM recipes LEFT JOIN users ON users.id = recipes.user_id 
        WHERE recipes.id = %(recipe_id)s;
        """
        results = connectToMySQL(db).query_db(query, data)

        recipe = cls(results[0])

        user_data = {
            "id" : results[0]['id'],
            "first_name" : results[0]['first_name'],
            "last_name" : results[0]['last_name'],
            "email" : results[0]['email'],
            "password" : results[0]['password'],
            "created_at" : results[0]['created_at'],
            "updated_at" : results[0]['updated_at']
        }
        
        recipe.user = User(user_data)
        return recipe

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(db).query_db(query)

        recipes = []
        for row in results:
            recipes.append(cls(row))
        return recipes
    
    @classmethod
    def update_recipe(cls, data):
        query = """UPDATE recipes SET name = %(name)s, 
        description = %(description)s, instruction = %(instruction)s, 
        date = %(date)s, time = %(time)s, updated_at = NOW() WHERE id = %(recipe_id)s;
        """
        results = connectToMySQL(db).query_db(query, data)
        return

    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM recipes WHERE id = %(recipe_id)s;"
        results = connectToMySQL(db).query_db(query, data)
        return