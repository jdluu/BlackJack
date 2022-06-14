import java.util.ArrayList;

public class BJHand  {
    public ArrayList<BJCard> cards;
    public int total;
    public int aces;

    public BJHand() {
        this.cards = new ArrayList<BJCard>();
        this.total = 0;
        this.aces = 0;
    }

    public void addCard(BJCard card) {
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
        for (BJCard card : this.cards) {
            this.total += card.getValue();
            if (card.getRank() == "Ace") {
                this.aces += 1;
            }
        }
        this.adjustForAce();
    }

    public void printCards() {
        for (BJCard card : this.cards) {
            System.out.println(card.getRank() + " of " + card.getSuit());
        }
    }
    
}
