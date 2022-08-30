import random

number_decks = 1
reshuffle_count = 12

types = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]
suits = ["C", "D", "H", "S"]

deck = []
player_hand = []
dealer_hand = []

in_hand = False
player_total = 0
dealer_total = 0

def startHand():
	global player_total, dealer_total, in_hand
	if len(deck) < reshuffle_count:
		print("The deck is being reshuffled now.")
		shuffle_deck()

	player_hand.clear()
	dealer_hand.clear()
	player_total = 0
	dealer_total = 0

	player_total = add_card(player_hand, player_total);
	dealer_total = add_card(dealer_hand, dealer_total);
	player_total = add_card(player_hand, player_total);
	dealer_total = add_card(dealer_hand, dealer_total);

	in_hand = (player_total < 21)
	if player_total == 21:
		play_dealer()

def is_hand_active():
	return in_hand

def hit_player():
	global player_total, in_hand
	if in_hand:
		player_total = add_card(player_hand, player_total)
		in_hand = (player_total < 21)

def play_dealer():
	global dealer_total, in_hand
	in_hand = False;
	if player_total <= 21:
		while dealer_total <= 16:
			dealer_total = add_card(dealer_hand, dealer_total)

def player_cards():
	return ", ".join(player_hand).upper().replace("T", "10")

def dealer_cards():
	cards = ", ".join(dealer_hand)
	if in_hand:
		cards = "??" + cards[2:]
	return cards.upper().replace("T", "10")

def hand_results():
	if in_hand:
		return "Please Hit or Stand"
	else:
		play_dealer()
	
	if player_total > 21:
		return "Player Busted - You Lost!"
	elif dealer_total > 21:
		return "Dealer Busted - You Win!"
	elif player_total == dealer_total:
		return "Its a Tie - No One Won"
	elif player_total > dealer_total:
		return "You Won - Dealer Lost!"
	else:
		return "You Lost - Dealer Won!"

def add_card(hand, current):
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

def shuffle_deck():
	deck.clear()
	for count in range(number_decks):
		for type in types:
			for suit in suits:
				deck.append(type + suit)
	random.shuffle(deck)

shuffle_deck()