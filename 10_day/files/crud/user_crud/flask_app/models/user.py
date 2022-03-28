from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = 'models_schema' #! use this variable to define your DB one time

#! we make a class/model for every non-relation table in our DB
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

 #! class method that queries the database table that corresponds to this model, this is the R in CRUD
    @classmethod
    def get_all(cls) -> list:
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        users = []
        for user in results: #! taking dicts from DB and making user objects
            users.append( cls(user) )
        return users
<<<<<<< HEAD

#! class method to add a user to the DB, this is C in CRUD
=======
    #! class method to add a user to the DB, this is C in CRUD
>>>>>>> bdd191aedc6a83fa01103b14bf789cfe33c8ff85
    @classmethod
    def save(cls, data:dict ) -> int:
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(DATABASE).query_db( query, data )
        #! the return stmt returns the id as an int of the user created

<<<<<<< HEAD
#! class method to retrieve a user from the DB, this is R in CRUD
=======
        #! class method to retrieve a single user from the DB, this is R in CRUD
>>>>>>> bdd191aedc6a83fa01103b14bf789cfe33c8ff85
    @classmethod
    def get_one(cls, data:dict) -> object:
        query = 'SELECT * FROM users WHERE id = %(id)s;'
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0])
<<<<<<< HEAD

=======
>>>>>>> bdd191aedc6a83fa01103b14bf789cfe33c8ff85
#! class method to update a user in the DB, this is U in CRUD
    @classmethod
    def update(cls, data:dict) -> object:
        query = 'UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id = %(id)s;'
        return connectToMySQL(DATABASE).query_db(query, data)

#! class method to delete a user in the DB, this is D in CRUD
    @classmethod
    def destroy(cls, data:dict) -> object:
        query = 'DELETE FROM users WHERE id = %(id)s;'
        return connectToMySQL(DATABASE).query_db(query, data)