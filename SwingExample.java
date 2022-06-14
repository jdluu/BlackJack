import javax.swing.*;  
public class SwingExample {  
    public static void main(String[] args) {
        //Create and set up the window.  
        JFrame f=new JFrame("BlackJack"); 
          
        JButton b=new JButton("Start Game");//creating instance of JButton  
        b.setBounds(130,300,100, 40);//x axis, y axis, width, height  
          
        f.add(b);//adding button in JFrame  
          
        f.setSize(400,500);//400 width and 500 height  
        f.setLayout(null);//using no layout managers  
        f.setVisible(true);//making the frame visible  
    }  
}  