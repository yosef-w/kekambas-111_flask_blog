from app import app
from flask import render_template
from fake_data import posts
from app.forms import SignUpForm

@app.route('/')
def index():
    return render_template('index.html', posts=posts, logged_in=False)


@app.route('/signup')
def signup():
    form = SignUpForm()
    return render_template('signup.html', form=form)


@app.route('/login')
def login():
    return render_template('login.html')
