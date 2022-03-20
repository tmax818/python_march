from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = 'models_schema'

class Model:
    def __init__( self , data ):
        self.id = data['id']
        self.param1 = data['param1']
        self.param2 = data['param2']
        self.param3 = data['param3']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

 #! class method that queries the database table that corresponds to this model, this is the R in CRUD
    @classmethod
    def get_all(cls) -> list:
        query = "SELECT * FROM models;"
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        models = []
        for model in results: #! taking dicts from DB and making model objects
            models.append( cls(model) )
        return models
    #! class method to add a model to the DB, this is C in CRUD
    @classmethod
    def save(cls, data:dict ) -> int:
        query = "INSERT INTO models (param1, param2, user_id, param3) VALUES ( %(param1)s, %(param2)s, %(user_id)s, %(param3)s);"
        return connectToMySQL(DATABASE).query_db( query, data )
        #! the return stmt returns the id as an int of the model created

        #! class method to retrieve a single model from the DB, this is R in CRUD
    @classmethod
    def get_one(cls, data:dict) -> object:
        query = 'SELECT * FROM models WHERE id = %(id)s;'
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0])
#! class method to update a model in the DB, this is U in CRUD
    @classmethod
    def update(cls, data:dict) -> object:
        query = 'UPDATE models SET param1=%(param1)s, param2=%(param2)s, user_id=%(user_id)s WHERE id = %(id)s;'
        return connectToMySQL(DATABASE).query_db(query, data)

#! class method to delete a model in the DB, this is D in CRUD
    @classmethod
    def destroy(cls, data:dict) -> object:
        query = 'DELETE FROM models WHERE id = %(id)s;'
        return connectToMySQL(DATABASE).query_db(query, data)

#! static method for validation of a model.
    @staticmethod
    def validate_model(model:dict) -> bool:
        is_valid = True # ! we assume this is true
        if len(model['param1']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(model['param2']) < 2:
            flash("Name must be at least 3 characters.")
            is_valid = False
        return is_valid