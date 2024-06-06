from flask import Flask,render_template,redirect
from flask import request
import sqlite3

# from data import Articles

app = Flask(__name__)


# connect = sqlite3.connect('flaskapp.db') 
#connect.execute('CREATE TABLE IF NOT EXISTS articles(id INTEGER AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255),author VARCHAR(100), body TEXT,create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)') 

#create a route
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')


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
    
    return render_template('articles.html', posts=posts)
   
# @app.route('/article/<string:id>/')
# def article(id):
#     return render_template('article.html', id=id)

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


if __name__=='__main__':
    app.run(debug=True)