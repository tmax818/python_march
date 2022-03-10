from flask import Flask, render_template # importing the Flask class from the flask module

app = Flask(__name__) #create an instance of the flask class and passing the required arg

### Routes go here

@app.route('/')
def index():
    return render_template('index.html', phrase="hello", times=50)

@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    student_info = [
       {'name' : 'Michael', 'age' : 35},
       {'name' : 'John', 'age' : 30 },
       {'name' : 'Mark', 'age' : 25},
       {'name' : 'KB', 'age' : 27}
    ]
    return render_template("lists.html", random_numbers = [3,1,5], students = student_info)




if __name__ == "__main__":
    app.run(debug=True)

