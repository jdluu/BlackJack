package main;

import game.BJDeck;
import game.BJHand;


public class Main extends BJHand {

    public static void sleep(int time) {
        try {
            Thread.sleep(time);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {

        // Create two hands, one for the player and one for the dealer
        BJHand player = new BJHand();
        BJHand dealer = new BJHand();

        // Generate the deck and shuffle it
        BJDeck deck = new BJDeck();
        deck.generateDeck();
        
        System.out.println("Shuffling the deck...\n");
        sleep(5000);
        System.out.println("Dealing the cards...\n");
        sleep(5000);

        // Deal two cards to each player
        player.addCard(deck.deal());
        player.addCard(deck.deal());

        dealer.addCard(deck.deal());

        // Print both cards for the player and only one for the dealer
        System.out.println("Your cards are: ");
        player.printCards();
        sleep(2000);
        System.out.println("\nThe dealer's card is: ");
        dealer.printCards();
        sleep(2000);

        // Update the totals for both players
        player.update();
        dealer.update();

        // Print the hands of both players
        System.out.println("\nYour hand: " + player.total + "\n");
        sleep(2000);
        System.out.println("Dealer's hand: " + dealer.total + "\n");

        // Keep playing until the player or dealer busts
        while (player.total < 21 && dealer.total < 21) {
            System.out.println("Would you like to hit or stay? (h/s)");
            String input = System.console().readLine();
            
            // If the player hits, add a card to their hand
            if (input.equals("h")) {
                sleep(2000);
                player.addCard(deck.deal());
                // Print the drawn card
                System.out.println("You drew a " + player.cards.get(player.cards.size() - 1).getRank() + " of " + player.cards.get(player.cards.size() - 1).getSuit());
                System.out.println("Your hand:\n");
                player.printCards();
                System.out.println("\nYour total: " + player.total + "\n");
                player.update();
            }
            // If the player stays, the dealer will hit
            else if (input.equals("s")) {
                System.out.println("You chose to stay.\n");
                sleep(2000);
                // Dealer's turn
                while (dealer.total < 17) {
                    dealer.addCard(deck.deal());
                    dealer.update();
                }
                System.out.println("Dealer's hand:");
                dealer.printCards();
                sleep(2000);
                System.out.println("Dealer's total: " + dealer.total + "\n");
                break;
            }
            else {
                System.out.println("Invalid input.");
            }
        }
        
        // Print who won
        if (player.total > 21) {
            System.out.println("You busted!\n");
        }
        else if (dealer.total > 21) {
            System.out.println("Dealer busted!\n");
            System.out.println("You won!\n");
        }
        else if (player.total > dealer.total) {
            System.out.println("You won!\n");
        }
        else if (player.total < dealer.total) {
            System.out.println("Dealer won!\n");
        }
        else {
            System.out.println("It's a tie!\n");
        }
    }
}