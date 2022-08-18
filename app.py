# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request, render_template
 
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__, static_url_path="")
 
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/home')
def get_homepage():
    return render_template("home.html")

@app.route('/game/')
def get_blackjack():
    return render_template('blackjack.html')

@app.route('/rules/')
def get_rules():
    return render_template('rules.html')

@app.route('/stats/')
def get_stats():
    return render_template('stats.html')
 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()