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
    sql = "INSERT INTO game(co2_consumed, co2_budget, screen_name, location) VALUES (0, 100000, '"+name+"', 'EFHK');"
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
    for row in result:
        print(f"You are located in {row[0]} in {row[1]}.")
    return

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


def update_co2_budget(co2_left, trip_distance, id):
    new_co2 = str(co2_left - trip_distance)
    sql = "UPDATE game SET co2_consumed=" + new_co2 + " WHERE id='" + id + "';"
    cursor = connection.cursor()
    cursor.execute(sql)
    return

def random_weather():
    temperature = random.randint(-40, 40)
    conditions = random.choice(['Cloudy', 'Clear'])
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


# if weather conditions meet any goals update goals_reached table
def update_goals_reached(goals_to_update, id):
    for i in goals_to_update:
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
player_name = str(input("Enter Your Name to start a new game:"))

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
    menu_input = int(input("Please Enter the number of the command which you want to run: "))
    if menu_input == 1:
        get_municipality(current_icao(player_id))
    if menu_input == 2:
        print("Print goals achieved")
    elif menu_input == 3:
        availableCo2 = available_co2(player_name)
        print(f"Your available CO2 is {availableCo2}.")
    elif menu_input == 4:
        icao = input("Enter the ICAO code of your destination.")
        lat_and_long = latitude_and_longitude(icao)
        distance = calculate_distance_km(icao, current_icao(player_id))
        availableCo2 = available_co2(player_name)
        if distance < availableCo2:
            travel(player_id,icao)
            update_co2_budget(availableCo2, distance, player_id)
            weather = random_weather()
            goals = goals_achieved(weather[0], weather[1], weather[2])
            update_goals_reached(goals, player_id)
            print(weather)
            print(goals)
            if count_goals(player_id) >= 5:
                print("You win!")
                break


        else:
            print("you don't have C02 budget.")
    else:
        continue







# - view current location
# - view goals (need function)
# - view co2 budget
# - travel to new airport


# -> If the player selects 'view current location': - The player's current location is displayed on the screen

# -> If the player selects 'view goals': - A list of remaining goals appear

# -> If the player selects 'view co2 budget': - The remaining co2 in the player's budget is displayed

# -> If the player selects 'travel to a new airport'

# if the player has enough c02>0 : - The player is asked to enter an ICAO code for the airport the wish to tavel to:

# After the player enters the code, the program checks that the player has enough co2 budgeted for the trip and informs them how far away the airport is and how much co2 will be consumed. If they have enough co2, they are then asked if they want to proceed. If not, they return to the first options list.

   # - If the player selects yes:
   #   - the players location is updated
   #   - the players co2 budgeted is updated
   #   - goals acheived are updated if any weather conditions correnspond with unrealized goals
   #   - All updated information is displayed to the player.
   #   - The player then goes back to the first option list
   #   - Check if the goals that are acheived are >=5 ; if so
   #   - player WINS!

print("Game Over")
