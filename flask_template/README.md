# Flask Template

- [ ] make a new directory for our application

```bash
mkdir flask_app
cd flask_app
```

- [ ] create the virtual environment
  
```bash
[python -m] pipenv install flask
pipenv shell
```

- [ ] create [`server.py`](server.py)

```bash
touch server.py
```

- [ ] start the server
```
python server.py
```

## Add views

- [ ] add [templates](templates/index.html)

```
mkdir templates
```

- [ ] import the `render_template` method from the flask module

```py
from flask import Flask, render_template # importing the Flask class from the flask module
```
- [ ] return the `render_template` method passing it the string name of the file to be rendered.
- [ ] use **jinja** to render data from `server.py` to our views

```html

<body>
    <h1>Lists</h1>
    <table>
        {% for student in students  %}
        <tr>
           <td> {{student['name']}}</td>
           <td>{{student['age']}}</td>
        </tr>
        {% endfor %}
    </table>

</body>

```

## Add static files i.e. css/javascript

- [ ] add the jinja syntax to the head section of the html file

```html
<!-- based on the folder structure on the right -->
<!-- linking a css style sheet -->
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">
<!-- linking a javascript file -->
<script type="text/javascript" src="{{ url_for('static', filename='my_script.js') }}"></script>
<!-- linking an image -->
<img src="{{ url_for('static', filename='my_img.png') }}">
```

- [ ] add the [static](static) folder