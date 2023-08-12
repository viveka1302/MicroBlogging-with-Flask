from app import app
from flask import render_template

@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    title="Home"
    user={"username": "Miguel P", "age":46}
    posts=[{'author': "Mark Manson", 'content':"Hello Hi dsada"},{'author':"Gerard Way", 'content':"MCR"}]
    return render_template("index.html", title=title, user=user, posts=posts)