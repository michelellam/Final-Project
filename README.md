# POOP GAME
## CS 110 Final Project
### Fall Semester, 2021
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit#)


### Team: Yurtle 
#### Michelle Lam and Hoyeon Yoo

***

## Project Description *(Software Lead)*
Our game is a poop game. The main objective is avoid the falling poop with other falling objects. If the player collides with a coin, the player will speed up and if the plater collides with bomb, the player will speed down. The score is how long you can survive (in seconds) without colliding with poop. 

***    

## User Interface Design *(Front End Specialist)*
* ![gameover](/assets/gameover.png)
* This screen will only initiate when the player collides with the poop object. 
* ![playing](/assets/playing.png)
* This is what the screen looks like while the game is running. 

***        

## Program Design *(Backend Specialist)*
* Non-Standard libraries
    * Pygame: https://www.pygame.org/docs/
    *   Pygame is a set of Python modules designed to create video games. It is easy to use as a beginners level.  

* Classes
    * Controller.py - This is where we draw the screen and where it handles all the events that are happening in the game. 
    * bomb.py - This is where we create the bomb object, making the bomb fall each frame, the update method as well as display a message every time the player hits a bomb. 
    * coin.py - This is where we create the coin object, as well as how to make the coin fall each frama, which will be updating in the update method, and a message everytime the player hits the coin. 
    * player.py - This is where we create our player. Inside of this class, it have methods of moving left and right,when the user hits the left and right keys. It also has a speed up/speed down method depending if the player hits the coin/bomb.  
    * poop.py - This is where we create our poop object. Inside of this class, it has a method to make the poop fall and a update method. 

## Project Structure *(Software Lead)*

The Project is broken down into the following file structure:
* main.py
* bin
    * ![bombdoc](/src/bomb.py)
    * ![coindoc](/src/coin.py)
    * ![controllerdoc](/src/controller.py)
    * ![playerdoc](/src/player.py)
    * ![poopdoc](/src/poop.py)
* assets
    * ![bomb](/assets/bomb.png)
    * ![background](/assets/background.png)
    * ![coin.png](/assets/coin.png)
    * ![class](/assets/Milestone 3 -2.pdf)
    * ![player](/assets/player.png)
    * ![poop](/assets/poop.png)

***

## Tasks and Responsibilities *(Software Lead)*

### Software Lead - Michelle Lam and Hoyeon Yoo

 Worked as integration specialist by always meeting outside of class together, and always have some sort of to-do list to achieve this by the day. We keep track of each other's code and always update each other if we made some progress on our own time. 

### Front End Specialist - Michelle Lam

 Michelle worked on the entire controller.py class and focused on connecting all the events (collisions) together, updating the game, and displaying text onto the screen.  

### Back End Specialist - Hoyeon Yoo

Hoyeon worked on all the classes: poop.py, coin.py, bomb.py, and player.py. She contributed on the speed up/speed down, reduce speed, and poop fall in the controller.py section as well. 

## Testing *(Software Lead)*
* Each time we added a new feature in the game, we would test it multiple times to make sure it was fully working. When there's an error after we add a new feature, we would test one code at a time, and if works, we would add another code and keep going. 
    * When we added the collison events for player touching the coin, sometimes the player would go out of the screen even though, we set up boundaries in the program. After we have fixed that, we would test it multiple times to make sure it works.

* Your ATP

| Step                  | Procedure     | Expected Results  | Actual Results |
| ----------------------|:-------------:| -----------------:| -------------- |
|  1  | Open terminal, navigate to folder, and type, “python3 main.py”  | Program Starts |          |
|  2  | user uses left arrow key  | Player moves left |                 |
|  3  | User uses right arrow key | Player moves right |                |
|  4  | Collides with Falling Coin | Player speeds up |                 |
|  5  | Collides with Bomb | Player slows down |            |
|  6  | Collides with Falling Poop | Game over screen initiates and displays score |         |
