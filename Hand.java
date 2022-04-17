import java.util.ArrayList;

public class Hand  {
    public ArrayList<Card> cards;
    public int total;
    public int aces;

    public Hand() {
        this.cards = new ArrayList<Card>();
        this.total = 0;
        this.aces = 0;
    }

    public void addCard(Card card) {
        this.cards.add(card);
        this.total += card.getValue();
        if (card.getRank() == "Ace") {
            this.aces += 1;
        }
    }

    public void adjustForAce() {
        if (this.total > 21 && this.aces > 0) {
            this.total -= 10;
            this.aces -= 1;
        }
    }

    public void update() {
        this.total = 0;
        this.aces = 0;
        for (Card card : this.cards) {
            this.total += card.getValue();
            if (card.getRank() == "Ace") {
                this.aces += 1;
            }
        }
        this.adjustForAce();
    }

    public void printCards() {
        for (Card card : this.cards) {
            System.out.println(card.getRank() + " of " + card.getSuit());
        }
    }
    
}
