from flask import Flask,render_template,redirect
from flask import request
import sqlite3

app=Flask(__name__)

# create a route

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/articles')
def articles():
     # Connect to db
    db = sqlite3.connect('posts.db')  
    cursor = db.cursor()
    
    # Get data from db
    cursor.execute('SELECT * FROM posts ORDER BY id DESC')
    posts = cursor.fetchall()
    
    # Close db connection
    db.close()
    
    return render_template('articles.html',posts=posts)

@app.route('/post/<_id>')
def post(_id):
    # Connect to db
    db = sqlite3.connect('posts.db')  
    cursor = db.cursor()
    
    # Get data from db
    cursor.execute('SELECT * FROM posts WHERE id=%s' % _id)
    post = cursor.fetchone()
    
    # Close db connection
    db.close()
    return render_template('post.html', post=post)


if __name__=="__main__":
    app.run(debug=True)