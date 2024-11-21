
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# << Project Title >>
## CS110 Final Project  << Semester, Year >>

## Team Members

<< List team member names >>
Connor Basile
***

## Project Description
I am going to work on creating a game that contains all of the most popular card games. Card games that will be included are Rummy, Hearts, Blackjack, 1v1 Poker, and Solitaire. Players can choose to play casually or put in game currency down as bets. In order to access each game, the player will navigate their avatar through a simple in-game menu, which will look like the lobby of a casino or arcade. Each of the games will be accessed by walking to a table that has the same name as the card game that they wish to play.
<< Give an overview of your project >>

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. << Moveable Characters >>
2. << Arithmetic Functions >>
3. << Traverseable Menu >>
4. << Game Results Screen >>
5. << Customize Character Menu >>

### Classes

- << You should have a list of each of your classes with a description >>
Class CardB: This is a class that contains the card object for the game of blackjack. It takes in 5 variables,
        img_file : str - path to image file
        suit: str, contains the specific suit of the card
        number: int, the exact number that is read on the card
        name: string, f.e  "eight" or the queen card "queen"
        worth: int, the numerical value of a card
    The method assign_value takes in the number of the card and assigns a playing value to it
Class Currency: A class which contains the currency object, which is applicable throughout all of the games. It takes in 5 variables,
        total: int, the total amount of currency that the player has
        img_file: str - path to file image
        color: str - color of the currency
        x: int - x coordinate of the currency display
        y: int - y coordinate of the currency display
    The method checkFunds checks the Players total amount of money to see if they have enough money to make a bet
    The method addFunds adds funds into the Players account
## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Run Counter Program  |GUI window appears with count = 0  |
|  2                   | click count button   | display changes to count = 1      |
etc...
