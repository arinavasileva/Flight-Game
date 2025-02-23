from main_functions import *
# main:
# When a player starts the game, they are greeted and asked to enter their name.
print(f"Welcome to Alien Weather game!")
print("")
print("You are an alien who has traveled to Earth to study the weather conditions on this strange planet. However,")
print("your ship has crash landed but you still need to complete your mission. You must now travel by plane")
print("to any airport of your choice by simply selecting the ICAO code which your alien brain has memorized. ")
print("")
print("Your goal is to experience five of the following eight weather conditions:")
print("Goal 1: Hot (Over 25 degrees)")
print("Goal 2: Cold (Under -20 degrees)")
print("Goal 3: Exactly 0 degrees")
print("Goal 4: Exactly 10 degrees")
print("Goal 5: Exactly 20 degrees")
print("Goal 6: Clear conditions")
print("Goal 7: Cloudy conditions")
print("Goal 8: Windy (Over 10m/s)")
print("")
print("Since you are an alien with superior intelligence and knowledge of the disastrous effects of global warming,")
print("You have a limited co2 budget to complete your mission.")
print("")
print("Good luck Earth explorer!")
print("")
player_name = str(input("Enter Your Name to start a new game: "))
print("")
# Their name is saved to the game table of our flight_game database and they are given a c02 budget of 10000.
greetings(player_name)

# store player id in a variable for function calls
player_id = find_id(player_name)

# While loop to verify that the player has sufficient co2:
while available_co2(player_name) > 0:
    # Next the player is presented with a list of options
    print("1- view current location.")
    print("2- view goals achieved.")
    print("3- view co2 budget.")
    print("4- travel to new airport")
    print("5- quit and exit game")
    print("")
    menu_input = int(input("Please Enter the number of the command which you want to run: "))
    print("")

    # If the player selects 'view current location': - The player's current location is displayed on the screen
    if menu_input == 1:
        airport = get_municipality(current_icao(find_id(player_name)))
        print(f"You are located in {airport[0][0]} in {airport[0][1]}.")
        print("")

    # If the player selects 'view goals': - A list of remaining goals appear
    if menu_input == 2:
        print(f"The number of each goal you have achieved so far: {check_goals(player_id)}")
        print("")

    # If the player selects 'view co2 budget': - The remaining co2 in the player's budget is displayed
    elif menu_input == 3:
        availableCo2 = available_co2(player_name)
        print(f"Your available CO2 is {availableCo2}.")
        print("")

    # If the player selects 'travel to a new airport'
    elif menu_input == 4:
        search = input("Would you like to search for ICAO codes? Y/N?")
        while True:
            if search == 'Y':
                country = input("Enter the country you would like to travel to: ")
                get_airports(country)
                break
            elif search == 'N':
                break
            else:
                print("Please enter Y or N")
                search = input("Would you like to search for ICAO codes? Y/N?")
        icao = input("Enter the ICAO code of your destination: ")
        print("")
        # calculate distance to destination
        distance = calculate_distance_km(icao, current_icao(player_id))
        # calculate available co2
        availableCo2 = available_co2(player_name)
        # ensure player has sufficient co2 in budget for trip
        if distance < availableCo2:
            # update player location
            travel(player_id,icao)
            # update player co2 budget
            update_co2_budget(distance, player_id)
            # generate weather conditions
            weather = random_weather()
            # create list of goals that the weather has achieved for the player
            goals = goals_achieved(weather[0], weather[1], weather[2])
            # use the goals list to update the goals reached table
            update_goals_reached(goals, player_id)
            # inform player of game progress
            print(f"Welcome to {get_municipality(current_icao(player_id))[0][0]}, {get_municipality(current_icao(player_id))[0][1]}!")
            print(f"Temperature: {weather[0]}C")
            print(f"Conditions: {weather[1]}")
            print(f"Wind: {weather[2]}m/s")
            print(f"You have achieved goals {goals}!")
            print("")
            # Every round, check if the player has achieved enough goals to win the game
            if count_goals(player_id) >= 5:
                print("")
                print(f"You have achieved goals {check_goals(player_id)}!")
                print("You win!")

                break
        else:
            print("you don't have C02. Select a closer location")
            print("")

    elif menu_input == 5:
        print("Game Over")
        break
    elif menu_input > 5:
        print("choose only a number between 1 and 4")
        print("")

