import mariadb
import random
from geopy.distance import geodesic as GD


connection = mariadb.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game2',
         user='root',
         password='root123',
         autocommit=True
         )

def greetings(name):
    sql = "INSERT INTO game(co2_consumed, co2_budget, screen_name, location) VALUES (0, 500, '"+name+"', 'EFHK');"
    cursor = connection.cursor()
    cursor.execute(sql)
    return

def find_id(screen_name):
    sql = "Select id from game where screen_name ='" + screen_name +"'"
    cursor = connection.cursor()
    cursor.execute(sql)
    response = cursor.fetchall()
    return str(response[0][0])
def current_icao(id):
    sql = "SELECT ident FROM airport, game WHERE game.location=airport.ident AND game.id='" + id + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    response = cursor.fetchall()
    return response[0][0]

def get_municipality(icao):
    location = "SELECT name, municipality FROM airport WHERE ident ='"+icao+"'"
    cursor = connection.cursor()
    cursor.execute(location)
    result = cursor.fetchall()
    return result

def latitude_and_longitude(icao):
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident= '" + icao + "';"
    cursor = connection.cursor()
    cursor.execute(sql)
    response = cursor.fetchall()
    return response

def calculate_distance_km(starting_location, final_location):
    location1 = latitude_and_longitude(starting_location)
    location2 = latitude_and_longitude(final_location)
    distance = GD(location1, location2).km
    return distance


def available_co2(screen_name):
    sql = "select @co2_left:= co2_budget - co2_consumed as co2_left from game where screen_name= '" + screen_name + "';"
    cursor = connection.cursor()
    cursor.execute(sql)
    co2_avail = cursor.fetchall()
    return co2_avail[0][0]


def travel(id, icao):
    sql = "UPDATE game SET location='" + icao + "' WHERE id='" + id + "';"
    cursor = connection.cursor()
    cursor.execute(sql)
    return


def update_co2_budget(trip_distance, id):
    sql = "SELECT co2_consumed FROM game WHERE id ='" + id + "';"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    new_co2 = str(int(result[0][0]) + trip_distance)
    sql = "UPDATE game SET co2_consumed=" + new_co2 + " WHERE id='" + id + "';"
    cursor = connection.cursor()
    cursor.execute(sql)
    return

def random_weather():
    temperature = random.randint(-40, 40)
    conditions = random.choice(['Clouds', 'Clear'])
    wind = random.randint(0, 15)
    return temperature, conditions, wind


def goals_achieved(temperature, conditions, wind):
    achieved_goals = []
    sql = "SELECT target_minvalue FROM goal WHERE id = '1';"
    cursor = connection.cursor()
    cursor.execute(sql)
    response = cursor.fetchall()
    if temperature >= response[0][0]:
        achieved_goals.append(1)

    sql = "SELECT target_maxvalue FROM goal WHERE id = '2';"
    cursor = connection.cursor()
    cursor.execute(sql)
    response = cursor.fetchall()
    if temperature <= response[0][0]:
        achieved_goals.append(2)

    sql = "SELECT target_minvalue, target_maxvalue FROM goal WHERE id = '3';"
    cursor = connection.cursor()
    cursor.execute(sql)
    response = cursor.fetchall()
    target_minimum = []
    target_maxvalue = []
    for row in response:
        target_minimum = row[0]
        target_maxvalue = row[1]
    if target_minimum <= temperature <= target_maxvalue:
        achieved_goals.append(3)

    sql = "SELECT target_minvalue, target_maxvalue FROM goal WHERE id = '4';"
    cursor = connection.cursor()
    cursor.execute(sql)
    response = cursor.fetchall()
    target_minimum = []
    target_maxvalue = []
    for row in response:
        target_minimum = row[0]
        target_maxvalue = row[1]
    if target_minimum <= temperature <= target_maxvalue:
        achieved_goals.append(4)

    sql = "SELECT target_minvalue, target_maxvalue FROM goal WHERE id = '5';"
    cursor = connection.cursor()
    cursor.execute(sql)
    response = cursor.fetchall()
    target_minimum = []
    target_maxvalue = []
    for row in response:
        target_minimum = row[0]
        target_maxvalue = row[1]
    if target_minimum <= temperature <= target_maxvalue:
        achieved_goals.append(5)

    sql = "SELECT target_text FROM goal WHERE id = '6';"
    cursor = connection.cursor()
    cursor.execute(sql)
    response = cursor.fetchall()
    if response[0][0] == conditions:
        achieved_goals.append(6)

    sql = "SELECT target_text FROM goal WHERE id = '7';"
    cursor = connection.cursor()
    cursor.execute(sql)
    response = cursor.fetchall()
    if response[0][0] == conditions:
        achieved_goals.append(7)

    sql = "SELECT target_minvalue FROM goal WHERE id = '8';"
    cursor = connection.cursor()
    cursor.execute(sql)
    response = cursor.fetchall()
    if response[0][0] <= wind:
        achieved_goals.append(8)

    return achieved_goals

def check_goals(id):
    sql = "SELECT goal_id FROM goal_reached WHERE game_id = '" + str(id) + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    response = cursor.fetchall()
    return response

# if weather conditions meet any goals update goals_reached table
def update_goals_reached(goals_to_update, id):
    list1 = []
    # check existing goals to compare with new goals to avoid duplicates
    for i in check_goals(id):
        list1.append(i[0])
    list2 = goals_to_update
    # create a list of goals achieved that are not already in table:
    new_list = [item for item in list2 if item not in list1]
    # insert new and unique goals into table
    for i in new_list:
        goal = str(i)
        sql = "INSERT INTO goal_reached (goal_id, game_id) VALUES ('" + goal + "', '" + id + "');"
        cursor = connection.cursor()
        cursor.execute(sql)
    return

def count_goals(id):
    sql = "SELECT COUNT(game_id) FROM goal_reached Where game_id = '" + id + "';"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result[0][0]


# main:
# When a player starts the game, they are greeted and asked to enter their name.
print(f"Welcome to FLight game!")
player_name = str(input("Enter Your Name to start a new game: "))

# Their name is saved to the game table of our flight_game database and they are given a c02 budget of 10000.
greetings(player_name)

# store player id in a variable for function calls
player_id = find_id(player_name)

# While loop to verify that the player has sufficient co2:
while available_co2(player_name) > 0:
    # Next the player is presented with a list of options
    print("1- view current location.")
    print("2- view goals.")
    print("3- view co2 budget.")
    print("4- travel to new airport")
    print("5 - quit and exit game")

    menu_input = int(input("Please Enter the number of the command which you want to run: "))

    # If the player selects 'view current location': - The player's current location is displayed on the screen
    if menu_input == 1:
        airport = get_municipality(current_icao(player_id))
        print(f"You are located in {airport[0][0]} in {airport[0][1]}.")

    # If the player selects 'view goals': - A list of remaining goals appear
    if menu_input == 2:
        print(f"you have achieved goals {check_goals(player_id)}")

    # If the player selects 'view co2 budget': - The remaining co2 in the player's budget is displayed
    elif menu_input == 3:
        availableCo2 = available_co2(player_name)
        print(f"Your available CO2 is {availableCo2}.")

    # If the player selects 'travel to a new airport'
    elif menu_input == 4:
        icao = input("Enter the ICAO code of your destination: ")
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
            print(f"Welcome to {get_municipality(current_icao(player_id))}!")
            print(f"Temperature: {weather[0]}C")
            print(f"Conditions: {weather[1]}")
            print(f"Wind: {weather[2]}m/s")
            print(f"You have achieved goals {goals}!")
            # Every round, check if the player has achieved enough goals to win the game
            if count_goals(player_id) >= 5:
                print("You win!")
                break
        else:
            print("you don't have C02. Select a closer location")

    elif menu_input == 5:
        print("Game Over")
        break
    else:
        print("choose only a number between 1 and 4")



