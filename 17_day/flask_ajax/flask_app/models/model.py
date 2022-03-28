from flask_app.config.mysqlconnection import connectToMySQL
import requests

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

    @classmethod
    def data(cls):
        name = "tmax818"
        endpoint = f"https://api.github.com/users/{name}"
        res = requests.get(endpoint)
        return res.json()