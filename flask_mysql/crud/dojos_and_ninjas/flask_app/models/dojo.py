from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

db = 'dojos_and_ninjas'

class Dojo:
    def __init__(self, data):
        self.id = data['id']

        self.name = data['name']

        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.ninjas = []

    #------------------------------------
    # Get all the dojos from the database
    #------------------------------------
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(db).query_db(query)
        print(results)
        all_dojos = []  # Creating an empty list to append my instances of dojos
        for dojo in results:                # Everytime I'm running through my for loop, I'm creating an instance 
            all_dojos.append(cls(dojo))     # And I'm adding that instance to my list of instances (all_dojos)
        return all_dojos
    
    #------------------------------------
    # Insert the dojo being sent
    #------------------------------------
    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO dojos(name, created_at, updated_at)
        VALUES(%(name)s, NOW(), NOW());
        """
        results = connectToMySQL(db).query_db(query, data)
        return results
    
    #------------------------------------------------------
    # LEFT JOIN TO ninjas to connect ninjas with their dojo
    #------------------------------------------------------
    @classmethod
    def show_one_dojo(cls, data):
        query = """
        SELECT * FROM dojos 
        LEFT JOIN ninjas 
        ON dojos.id = ninjas.dojo_id 
        Where dojos.id = %(dojo_id)s; 
        """
        results = connectToMySQL(db).query_db(query, data)
        # Pulling the primary instance located at position 0 
        dojo = cls(results[0])  
        # Loop through the results (dojo) and pull the ninjas information
        for ninja_info in results:
            ninja_data = {
                "id" : ninja_info['ninjas.id'],
                "first_name" : ninja_info['first_name'],
                "last_name" : ninja_info['last_name'],
                "age" : ninja_info['age'],
                "created_at" : ninja_info['ninjas.created_at'],
                "updated_at" : ninja_info['ninjas.updated_at'],
                "dojo_id" : ninja_info['dojo_id']
            }
            dojo.ninjas.append(ninja.Ninja(ninja_data))
        return dojo

    #------------------------------------------------------
    # INSERT the ninja getting sent
    #------------------------------------------------------
    @classmethod
    def add_ninja(cls, data):
        query = """
        INSERT INTO ninjas(first_name, last_name, age, created_at, updated_at, dojo_id)
        VALUES (%(first_name)s, %(last_name)s, %(age)s, NOW(), NOW(), %(dojo_id)s);
        """
        results = connectToMySQL(db).query_db(query, data)
        return results
