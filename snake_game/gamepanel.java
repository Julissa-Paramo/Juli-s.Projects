import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.util.Random;
import javax.swing.JPanel;

public class GamePanel extends JPanel implements ActionListener {
    static final int SCREEN_WIDTH = 600;
    static final int SCREEN_HEIGHT= 600;
    static final int UNIT_SIZE = 25; //  one sqaure on the grid ( refer to grid drawing in draw method)
    static final int GAME_UNITS = (SCREEN_WIDTH * SCREEN_HEIGHT / UNIT_SIZE);
    static final int DELAY = 75;

    final int x[] = new int[GAME_UNITS]; // hold x coordiantes for body parts of snake
    final int y[] = new int[GAME_UNITS]; // hold y coordinates
    int bodyParts = 6;
    int applesEaten; // starts at 0
    int appleX; // x coordinate of where apple appears , will be random everytime an apple is eaten
    int appleY; // y coordinate
    char direction = 'R'; // snake begins going right
    boolean running = false;
    Timer timer;
    Random random;

    GamePanel(){

        random = new Random();
        this.setPreferredSize(new Dimension(SCREEN_WIDTH, SCREEN_HEIGHT));
        this.setBackground(Color.black);
        this.setFocusable(true);
        this.addKeyListener(new MyKeyAdapter());
        startGame();
    
    


    }

    public void startGame() {
        newApple(); // call new Apple method at start of game to add an apple
        running = true;
        timer = new Timer(DELAY, this);// dictates how fast game is running
        timer.start();
    }

    public void paintComponent(Graphics g){
        super.paintComponent(g);
        draw(g);
    }

    public void draw(Graphics g){
        for(int i = 0;i<SCREEN_HEIGHT/UNIT_SIZE;i++){ // draws lines on game panel for a visible grid
        g.drawLine(i*UNIT_SIZE,0,i*UNIT_SIZE,SCREEN_HEIGHT);
        g.drawLine(0,i*UNIT_SIZE,SCREEN_WIDTH,i*UNIT_SIZE);


        }
    }


// 19:00




    public void newApple(){ // the purpose of this method is to get new coordinates everytime we begin the game or score a point
        appleX = random.nextInt((int)(SCREEN_WIDTH/UNIT_SIZE)) * UNIT_SIZE; // x axis of apple will appear in a random spot
        appleY = random.nextInt((int)(HEIGHT/))
    }

    public void move(){

    }


    public void checkApple(){

    }

    public void checkCollisions(){

    }

    public void gameOver(Graphics g){

    }

    @Override
    public void actionPerformed(ActionEvent e){
    
    }

    public class MyKeyAdapter extends KeyAdapter{
        @Override
        public void keyPressed(KeyEvent e){

        }
    }
}
