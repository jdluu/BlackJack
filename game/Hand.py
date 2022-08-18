
from string import capwords
from Card import Card

class Hand:
    cards = []
    total = 0
    aces = 0

    # Get total value of hand
    def getTotal(self):
        total = 0
        for i in range(len(self.cards)):
            temp += self.cards[i].getVal()
        return total
    
    # Add a card to the hand
    def addCard(self, card):
        self.cards.append(card)
        self.total += card.getVal()
        if card.getRank() == "A":
            self.aces += 1

    # Update the hand
    def update(self):
        total = 0
        aces = 0
        for i in range(len(self.cards)):
            total += self.cards[i].getVal()
            if self.cards[i].getRank() == "A":
                aces += 1
        self.total = total
        self.aces = aces
        self.adjust()
    # Adjust hand for ace
    def adjust(self):
        while self.aces > 0 and self.total > 21:
            self.total -= 10
            self.aces -= 1

    # Print the hand
    def printHand(self):
        for i in range(len(self.cards)):
            print(self.cards[i].getRank() + " of " + self.cards[i].getSuit())
        print("Total: " + str(self.total))
        
