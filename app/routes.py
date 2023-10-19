from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm

@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    title="Home"
    user={"username": "Miguel P", "age":46}
    posts=[{'author': "Mark Manson", 'content':"Hello Hi dsada"},{'author':"Gerard Way", 'content':"MCR"}]
    return render_template("index.html", title=title, user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form= LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title= 'Sign In', form= form)
