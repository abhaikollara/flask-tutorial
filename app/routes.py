from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username':"Abhai"}
    posts = [
        {
            "author":{"username":"Boo"},
            "body": "Meh"
        },
        {
            "author":{"username":"Fooo"},
            "body": "Moo"
        }
    ]
    return render_template('index.html', title="Muhahah", user=user, posts=posts)