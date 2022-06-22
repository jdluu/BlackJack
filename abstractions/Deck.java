package abstractions;

public interface Deck {
    public void generateDeck();
    public Card deal();
    public void shuffle();
}