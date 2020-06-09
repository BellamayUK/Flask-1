from flask import render_template, url_for
from application import app

blogData = [
    {
        "name": {"first":"Wheat", "last":"Dolmio"},
        "title":"First Post",
        "content":"Just thinkin about the pasta"
    },
    {
        "name": {"first":"Rye o Rye Delilah", "last":"Dolmio"},
        "title":"Second Post",
        "content":"Rye would you do that?"
    }
]




@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html', title='Home', bella_sched="Make Pasta")

@app.route('/about')
def about():
    return render_template('about.html', title='About', desc="How to make pasta")

@app.route('/login')
def login():
    return render_template('login.html', title='Login', desc= 'login')

@app.route('/register')
def register():
    return render_template('register.html', title='Register', desc='register!')


@app.route('/post')
def post():
    return render_template('post.html', title='Post', desc='I like pasta too')
