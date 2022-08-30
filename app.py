# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request, render_template

import BlackJack 
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__, template_folder='templates', static_folder='static')
 
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.

# The home page of my website
@app.route('/')
def get_homepage():
    return render_template("home.html")

# The rules of BlackJack 
@app.route('/rules/')
def getRules():
    return render_template('rules.html')

# Stats of BlackJack players
@app.route('/stats/')
def getStats():
    return render_template('stats.html')

# 
@app.route('/blackjack/')
def getBlackjack():
    BlackJack.startHand()
    return render_template('blackjack.html', 
        handResults = BlackJack.handResults(), 
        playerCards = BlackJack.playerCards(), 
        dealerCards = BlackJack.dealerCards())

@app.post("/blackjack/")
def postBlackJack():
    submitButton = request.form.get("submitButton")

    if BlackJack.isPlayerTurn():
        if submitButton.upper() == "H":
            BlackJack.playerHit()
        else:
            BlackJack.dealerPlay()
    
    return render_template('blackjack.html', handResults = BlackJack.handResults(), playerCards = BlackJack.playerCards(), dealerCards = BlackJack.dealerCards())



# main driver function
if __name__ == "__main__":
    # run() method of Flask class runs the application
    # on the local development server.
     app.run(debug=True ,port=5000,use_reloader=False)