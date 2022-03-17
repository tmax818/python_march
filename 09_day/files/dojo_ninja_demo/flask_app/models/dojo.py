from sqlite3 import DatabaseError
from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = 'dojos_and_ninjas'

class Dojo:
    def __init__(self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

        