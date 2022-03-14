from flask import Flask, render_template, request, redirect
app = Flask(__name__)

# our index route will handle rendering our form

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def users():
    print(request.form)
    print(request.form["secret"])
    return redirect("/")


@app.route('/show')
def show():
    return render_template("show.html")



if __name__ == "__main__":
    app.run(debug=True)