import random

numberDecks = 1
reshuffleCount = 12

types = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]
suits = ["C", "D", "H", "S"]

deck = []
playerHand = []
dealerHand = []

playerTurn = False
playerTotal = 0
dealerTotal = 0

def startHand():
	global playerTotal, dealerTotal, playerTurn
	if len(deck) < reshuffleCount:
		print("The deck is being reshuffled now.")
		shuffleDeck()

	playerHand.clear()
	dealerHand.clear()
	playerTotal = 0
	dealerTotal = 0

	playerTotal = addCard(playerHand, playerTotal);
	dealerTotal = addCard(dealerHand, dealerTotal);
	playerTotal = addCard(playerHand, playerTotal);
	dealerTotal = addCard(dealerHand, dealerTotal);

	playerTurn = (playerTotal < 21)
	if playerTotal == 21:
		dealerPlay()

def isPlayerTurn():
	return playerTurn

def playerHit():
	global playerTotal, playerTurn
	if playerTurn:
		playerTotal = addCard(playerHand, playerTotal)
		playerTurn = (playerTotal < 21)

def dealerPlay():
	global dealerTotal, playerTurn
	playerTurn = False;
	if playerTotal <= 21:
		while dealerTotal <= 16:
			dealerTotal = addCard(dealerHand, dealerTotal)

def playerCards():
	return ", ".join(playerHand).upper().replace("T", "10")

def dealerCards():
	cards = ", ".join(dealerHand)
	if playerTurn:
		cards = "??" + cards[2:]
	return cards.upper().replace("T", "10")

def handResults():
	if playerTurn:
		return "Please Hit or Stand"
	else:
		dealerPlay()
	
	if playerTotal > 21:
		return "Player Busted - You Lost!"
	elif dealerTotal > 21:
		return "Dealer Busted - You Win!"
	elif playerTotal == dealerTotal:
		return "Its a Tie - No One Won!"
	elif playerTotal > dealerTotal:
		return "You Won - Dealer Lost!"
	else:
		return "You Lost - Dealer Won!"

def addCard(hand, current):
	if len(deck) == 0:
		print("OOPS - No more cards in the deck!")
		return current

	card = deck.pop(0)
	hand.append(card)

	type = card[0]
	value = 0
	if type == "A":
		value = 11
	elif type == "T" or type == "J" or type == "Q" or type == "K":
		value = 10
	else:
		value = int(type)

	total = current + value
	if total > 21:
		for index in range(len(hand)):
			card = hand[index]
			type = card[0]
			if type == "A":
				total = total - 10
				suit = card[1]
				card = "a" + suit
				hand[index] = card
				break
	return total

def shuffleDeck():
	deck.clear()
	for count in range(numberDecks):
		for type in types:
			for suit in suits:
				deck.append(type + suit)
	random.shuffle(deck)

shuffleDeck()