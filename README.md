# Chrome Dino Bot
A bot that plays the boring chrome dinosaur game that appears when no internet available.

![Game Screenshot](  https://1.bp.blogspot.com/-xOUkeIvVFXk/XsVOuhX4rgI/AAAAAAAAAGs/eCxYA4X5ElMZFzaRNAGmAEcd3WDspS8NwCNcBGAsYHQ/s1600/dino.png)

You will need to install **pyautogui** to make the bot run
```
pip install pyautogui
```
You will need to install **keyboard** to make the bot run
```
pip install keyboard
```
Use this link **chrome://dino/** to access the game even when you have internet (*use chrome*).

# Theory
I capture a screenshot every frame to look for obstacles to avoid.

There are 2 search ranges to find obstacles:

1- To look for the ground obstacles (**Cactus**).

2- To look for the upper obstacles (**Birds**).

* There is no need to programe the bot for Birds because we does'nt need. It make the code fast.

# How to identify obstacle?
An obstacle is considered any pixel in the search area that is different than the background colour.
If the bot finds an obstacle it uses the python **pyautogui** library to press space and let the Dino jump.

The high score so far is **35464**.

Any recommendations are welcomed..

**Credit**
Shivam Kumar Yadav Owner of Computers Ethics. 

*Who am i ?
Ehical Hacker, Programmer, Web Developer ;)

** Contact me For Bussiens Purpose @ :: shivcomdeytech12802@gmail.com **
 
// The screen size varies. Adjust according to your screen. If any doubt ask in Coumminity.
// UPDATES will come in futher 
