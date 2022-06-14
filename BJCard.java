public class BJCard implements Card {
    private String suit;
    private String rank;

    // Default constructor
    public BJCard() {
        this.suit = "";
        this.rank = "";
    }

    // Constructor
    public BJCard(String suit, String rank) {
        this.suit = suit;
        this.rank = rank;
    }

    /**
     * Getter method to return the suit of the card
     * @return the suit of the card
     */
    public String getSuit() {
        return this.suit;
    }

    /**
     * Getter method to return the rank of the card
     * @return the rank of the card
     */
    public String getRank() {
        return this.rank;
    }

    /**
     * Reads the card's rank and returns the value of the card
     * @return the value of the card
     */
    public int getValue() {
        if (this.rank == "Ace") {
            return 11;
        } 
        else if (this.rank == "King" || this.rank == "Queen" || this.rank == "Jack") {
            return 10;
        } 
        else {
            return Integer.parseInt(this.rank);
        }
    }
}
