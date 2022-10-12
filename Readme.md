Introduction: 
This document describes the functionality of flight simulator game created by group 2. It is intended to be used as a training purpose which gives the interested reader through the open source code the insight how the flight-game can be modeled in specific parts.

Vision:
The purpose of this game is to gain five out of eight goals from the mentioned goal table of the given flight-game database by using the mininmun amount of CO2. A budget of 10000 CO2 is provided to every player.CO2 will be deducted from players budget for each flight with an undetermined algorithm determining distance traveled as a part of the function. Players would be given a budget of CO2 for a trip from one country's airport to another considering they are in operating mode.


Functional requirements:

This game only has one player..
During the begining of the game a player will be greeted and have to enter their name.
Next the player is presented with a list of options: 

- view current location 
- view goals 
- view co2 budget 
- travel to new airport

If the player selects 'view current location': 
- The player's current location is displayed on the screen.

If the player selects 'view goals': 
- A list of all or remaining goals appear.

If the player selects 'view co2 budget': 
- The remaining co2 in the player's budget is displayed.

If the player selects 'search weather conditions': 
- The player is prompted to enter the ICAO code of the airport to view the weather conditions.

If the player selects 'travel to a new airport': 
- The player is asked to enter an ICAO code for the airport they wish to travel to.

After the player enters the code, the program checks that the player has enough CO2 budgeted for the trip and informs them how far away the airport is and how much CO2 will be consumed. If they have enough CO2, If the player selects yes: 

     - The players location is updated
     - The players co2 budget is updated
     - Goals acheived are updated if any weather conditions correnspond with unrealized goals
     - All updated information is displayed to the player
     - The player then goes back to the first option
     
     
     
     
     
     
     
     
When a player achieves five out of eight weather goals. The player wins the game.

Quality requirements:

Player will be given 
