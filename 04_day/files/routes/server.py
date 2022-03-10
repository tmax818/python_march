from flask import Flask # imports the Flask class

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>index</h1>"

@app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "Hello, " + name

@app.route('/users/<username>/<int:id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return f"username: {username * id} "





if __name__ == "__main__":
    app.run(debug=True)