# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template
 
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
 
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
@app.route('/home/')
def home():
    return render_template('home.html')

@app.route('/game/')
def game():
    return render_template('game.html')

@app.route('/rules/')
def rules():
    return render_template('rules.html')

@app.route('/stats/')
def stats():
    return render_template('stats.html')
 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()