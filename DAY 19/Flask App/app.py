from flask import Flask
from flask import render_template
from data import Articles

app=Flask(__name__)

Articles = Articles()

#creating a route
@app.route('/')
def index():
    return render_template("Home.html")

@app.route('/about')
def about():
    return render_template("about.html") 

@app.route('/articles')
def articles():
    return render_template('articles.html',articles = Articles)

# @app.route('/product/<id>')
# def product(id):
#     return 'This is product page and you are viewing:'+str(id)

if __name__=='__main__':
    app.run(debug=True)