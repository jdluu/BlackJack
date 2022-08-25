

class Card:
    suit = ""
    rank = ""


    # Constructor 
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    # Getter method that returns the suit of the card
    def getSuit(self):
        return self.suit
    
    # Getter method that returns the rank of the card
    def getRank(self):
        return self.rank
    
    # Getter method that returns the value of the card
    def getVal(self):
        if self.rank == "A":
            return 11;
        elif self.rank == "J" or self.rank == "Q" or self.rank == "K":
            return 10;
        else:
            return int(self.rank);
    
