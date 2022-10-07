# Flight-Game
Flight Simulator Group Project


Introduction  :
# This document describes the functionality of Group one's flight simulator game.
 
 
The purpose of the game:
#  The purpose of the game is to reach 5 of the eight goals from the exisiting goal table of the flight_game database, using the least amount of CO2. Each player begins with a budget of 10000 co2. Each "flight" will deduct co2 from the player's budget through an as of yet undetermined algorithm which takes the distance traveled as part of it's function. Players can fly between any two airports in the world as long as they are in operation and the player has enough budgeted co2 for the trip.
 
 
 Game play:
# This game will be able to be played by one or more players.
 
# When a player starts the game, they are greeted and asked to enter their name. Their name is saved to the game table of our flight_game database and they are given a c02 budget of 10000.
 
 -> 'Welcome to flight game! What is your name?'
 
 -> 'Bob'
 
 -> 'Hello Bob! Welcome to Flight Game! Please select one of the following options:'
 
-> Next the player is presented with a list of options:
    - view current location
    - view goals
    - view co2 budget
    - travel to new airport
    
-> If the player selects 'view current location':
    - The player's current location is displayed on the screen
    
-> If the player selects 'view goals':
    - A list of remaining goals appear
 
-> If the player selects 'view co2 budget':
    - The remaining co2 in the player's budget is displayed

-> If the player selects 'view players':
    - A list of all players is displayed included their goals reached, location, and co2 budget

-> If the player selects 'search weather conditions':
    - The player is prompted to enter the ICAO code of the airport which they want to view the weather:
    
    -> 'Please enter the ICAO code for the airport you wish to view the weather conditions: '
    
    -> 'EFHK'
    
    -> 'It is currently 12 degrees celcius and partly cloudy at Vaanta Aiport, Finland':
    
-> If the player selects 'travel to a new airport':
    - The player is asked to enter an ICAO code for the airport the wish to tavel to
    
    -> 'Please enter the ICAO code for the airport you wish to travel to: '
    
    -> 'KJFK'
    
    - After the player enters the code, the program checks that the player has enough co2 budgeted for the trip and informs them how far away the airport         is and how much co2 will be consumed. If they have enough co2, they are then asked if they want to proceed. If not, they return to the first options       list.
      
    -> 'John F. Kennedy International Airport is 6626km away' 
    
    -> 'This flight will consume 2000 co2. Do you wish to proceed?:  y/n?'
       - If the player selects no:
         - the player goes back to the very first options list.
         
       - If the player selects yes:
         - the players location is updated
         - the players co2 budgeted is updated
         - goals acheived are updated if any weather conditions correnspond with unrealized goals
         - All updated information is displayed to the player.
         - The player then goes back to the first option list
 
Winning the game:
# When a player achieves five out of eight weather goals. The player wins the game.
    
 
 
 

 
 
