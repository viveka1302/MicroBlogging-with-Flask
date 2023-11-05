from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    title="Home"
    user={"username": "Vivek", "age":20}
    posts=[{'author': "Devyansh Samyal", 'content':"Hello Hi!!"},{'author':"Mihir Dhingra", 'content':"Hola amigo"}]
    return render_template("index.html", title=title, user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form= LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title= 'Sign In', form= form)
