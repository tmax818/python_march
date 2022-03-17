
from mysqlconnection import connectToMySQL

class Burger:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.bun = data['bun']
        self.meat = data['meat']
        self.calories = data['calories']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "INSERT INTO restaurants ( name , bun, meat, calories, restaurant_id, created_at , updated_at ) VALUES (%(name)s, %(bun)s, %(meat)s, %(calories)s, %(restaurant_id)s,NOW(),NOW());"
        results = connectToMySQL('first_flask').query_db(query)
        burgers = []
        for burger in results:
            burgers.append( cls(burger) )
        return burgers