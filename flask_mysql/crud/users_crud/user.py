from mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']

        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']

        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    # -----------------------------------------------
    # @classmethod get user information from database
    # -----------------------------------------------
    @classmethod
    def users_info(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)     # Calling the connectToMySQL function with the schema I am targeting.
        print(results)
        all_users = []      # Creating a empty list to append my instances of users
        for user in results:
            each_user = cls(user)       # Everytime I'm running through my for loop, I'm creating an instance 
            all_users.append(each_user) # And I'm adding that instance to my list of instances (all_users)
        return all_users

    # --------------------------------------
    # @classmethod insert user to database
    #---------------------------------------
    @classmethod
    def insert_users(cls, data):
        query = """
        INSERT INTO users(first_name, last_name, email, created_at)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW());
        """
        results = connectToMySQL('users_schema').query_db(query, data)
        print(results)
        return results
