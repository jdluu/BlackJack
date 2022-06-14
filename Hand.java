import java.util.ArrayList;

abstract class Hand {

    // Fields
    public ArrayList<Card> cards;
    public int total;
    public int aces;

    // Constructor
    public Hand() {
        this.cards = new ArrayList<Card>();
        this.total = 0;
        this.aces = 0;
    }

    public abstract int getHandValue();
    public abstract void addCard(Card card);
    public abstract void printCards();

    public void adjustForAce() {
        if (this.getHandValue() > 21 && this.aces > 0) {
            this.total -= 10;
            this.aces -= 1;
        }
    }

    
}