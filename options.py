players_name = input("Enter your name:")
print(f'Hello, {players_name}! Welcome to Flight Game! Please select one of the following options:')


def options_function():
    print("1.View current location")
    print("2.View goals")
    print("3.View co2 budget")
    print("4.Travel to a new airport")
    return


options_selection = int(input("Enter the number of the selected function:"))
if options_selection == 1 :
    current_icao(id)
if options_selection == 2:
    game_goals(id)
if options_selection == 3:
    available_co2(id)
elif options_selection == 4:

    else:
    print("There is not such function number")
