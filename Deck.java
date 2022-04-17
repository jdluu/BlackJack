

import java.util.ArrayList;

class Deck extends Card {
    private ArrayList<Card> cards;
    private String[] suits = {"Hearts", "Diamonds", "Clubs", "Spades"};
    private String[] ranks = {"Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"};

    // Default constructor
    public Deck() {
        this.cards = new ArrayList<Card>();
    }

    /**
     * Creates a deck of 52 cards
     */
    public void generateDeck() {
        for (int i = 0; i < suits.length; i++) {
            for (int j = 0; j < ranks.length; j++) {
                Card card = new Card(suits[i], ranks[j]);
                cards.add(card);
            }
        }
        shuffle();
    }

    /**
     * Shuffles the deck
     * @return none
     */
    public void shuffle() {
        // Randomize the order of the cards
        for (int i = 0; i < cards.size(); i++) {
            int randomIndex = (int) (Math.random() * cards.size());
            Card temp = cards.get(i);
            cards.set(i, cards.get(randomIndex));
            cards.set(randomIndex, temp);
        }

    }

    /**
     * Deals a card from the deck
     * @return the card that was dealt
     */
    public Card deal() {
        // Deal a random card from the deck
        int randomIndex = (int) (Math.random() * cards.size());
        Card card = cards.get(randomIndex);
        cards.remove(randomIndex);
        return card;
    }


}