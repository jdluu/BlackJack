package gui;
import javax.swing.*;  
public class SwingExample {  
    public static void main(String[] args) {
        //Create and set up the window.  
        JFrame f=new JFrame("BlackJack"); 
        // Create and set up a button to be displayed in the window.
        JButton b=new JButton("Start Game");
        // Create and set up a label to be displayed in the window.
        JLabel l=new JLabel("Welcome to BlackJack!");
        JPanel panel = new JPanel();
        // Set the x axis, y axis, width, and height 
        b.setBounds(130,300,100, 40);
        l.setBounds(130,100,200,40);
        // Set the width and height of the window.  
        f.setSize(400,500);
        // Add to the window.
        f.add(b);
        f.add(l);
        
        f.setLayout(new CardLayout());//using no layout managers  
        f.setVisible(true);//making the frame visible  
    }  
}  