
from Deck import Deck
from Hand import Hand
from Card import Card

import time

class BlackJack(Hand):
    pass

    # Create a delay for x seconds
    def delay(self, seconds):
        time.sleep(seconds)
    
    def game(self):

        # Create two hands, one for the player and one for the dealer
        player = Hand()
        dealer = Hand()

        # Create a deck and shuffle it
        deck = Deck()
        deck.shuffle()

        print("Shuffling the deck...\n")
        self.delay(5)
        print("Dealing the cards...\n")
        self.delay(5)

        # Deal two cards to the player and 1 to the dealer
        player.addCard(deck.deal())
        player.addCard(deck.deal())
        dealer.addCard(deck.deal())

        # Show the cards that were dealt to the player and the dealer
        print("\nYou were dealt:")
        player.printHand()
        self.delay(2)
        print("\nThe dealer was dealt:")
        dealer.printHand()
        self.delay(2)

        # Update the total value of the player and the dealer
        player.update()
        dealer.update()

        # Play until the end
        while True:
            print("\nWould you like to hit or stay?")
            choice = input("Enter 'h' to hit or 's' to stay: ")
            if choice == "h":
                player.addCard(deck.deal())
                player.update()
                player.printHand()
                if player.getTotal() > 21:
                    print("\nYou busted!\n")
                    break
            elif choice == "s":
                break
            else:
                print("\nInvalid choice.\n")
                continue
        self.delay(2)
        print("\nThe dealer's turn...\n")
        self.delay(2)
        while dealer.getTotal() < 17:
            dealer.addCard(deck.deal())
            dealer.update()
            dealer.printHand()
            self.delay(2)
        if dealer.getTotal() > 21:
            print("\nThe dealer busted!\n")
        elif dealer.getTotal() > player.getTotal():
            print("\nThe dealer wins!\n")
        elif dealer.getTotal() < player.getTotal():
            print("\nYou win!\n")
        else:
            print("\nIt's a tie!\n")
        exit()


