from hand import Hand
from deck import Deck

deck = Deck()
player = Hand()
dealer = Hand()
playerTurn = False

def startHand():
    deck.shuffle()

    player.clearHand()
    dealer.clearHand()

    player.addCard(deck.deal())
    player.addCard(deck.deal())

    player.update()
    playerTurn = (player.getTotal() < 21)
    if player.getTotal() == 21:
        dealerPlay()

def isPlayerTurn():
    return playerTurn

def playerHit():
    if playerTurn:
        player.addCard(deck.deal())
        player.update()
        playerTurn = (player.getTotal() < 21)


def dealerPlay():
    playerTurn = False
    if player.getTotal() < 21:
        while dealer.getTotal() < 17:
            dealer.addCard(deck.deal())
            dealer.update()

def playerCards():
    return player.getHand()

def dealerCards():
    return dealer.getHand()

def handResults():
    if playerTurn:
        return "Hit or Stand"
    else:
        print("Dealer's Turn...")
        dealerPlay()
    
    playerTotal = player.getTotal()
    dealerTotal = dealer.getTotal()

    if playerTotal > 21:
        return "You busted!"
    elif dealerTotal > 21:
        return "Dealer busted! You win!"
    elif playerTotal == dealerTotal:
        return "Push! You tied with the dealer!"
    elif playerTotal > dealerTotal:
        return "You win!"
    else:
        return "You lost!"







