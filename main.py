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


def determine_current_location(screen_name):
    sql = "SELECT ident FROM airport, game WHERE game.location=airport.ident AND game.screen_name='" + screen_name + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    location = cursor.fetchall()

    # create variable to store current location:
    current_location = ''
    for row in location:
        current_location = row[0]
    return current_location


# Desired location latitude and longitude:
def desired_lat_and_long(icao):
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident= '" + icao + "';"
    cursor = connection.cursor()
    cursor.execute(sql)
    response = cursor.fetchall()
    return response


# Current location lat and long:
def current_lat_and_long(starting_location):
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident= '" + starting_location + "';"
    cursor = connection.cursor()
    cursor.execute(sql)
    response = cursor.fetchall()
    return response


# Distance between current and travel location
def calculate_distance(starting_location, final_location):
    trip_distance = GD(starting_location, final_location).km
    return trip_distance


# calculate co2 available
def calculate_available_co2(screen_name):
    sql = "select @co2_left:= co2_budget - co2_consumed as co2_left from game where screen_name = 'Heini';"
    cursor = connection.cursor()
    cursor.execute(sql)
    response3 = cursor.fetchall()
    co2_left = response3
    # store new available co2 as a variable:
    for row in co2_left:
        co2_left = row[0]
    return co2_left


def update_current_location(screen_name, icao):
    sql = "UPDATE game SET location='" + icao + "' WHERE screen_name='" + screen_name + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    return


def update_co2_budget(co2_left, trip_distance):
    new_co2 = str(co2_left + trip_distance)
    sql = "UPDATE game SET co2_consumed=" + new_co2 + " WHERE screen_name='Heini'"
    cursor = connection.cursor()
    cursor.execute(sql)


def random_weather():
    temperature = random.randint(-40, 40)
    conditions = random.choice(['Cloudy', 'Clear'])
    wind = random.randint(0, 15)
    randomized_weather = (temperature, conditions, wind)
    return randomized_weather

# compare weather conditions between current location and goals
def compare_weather_conditions(temperature, conditions, wind):
    goals_to_update = ()
    #sql code: select target minimum from goal 1
    #if temp is greater:
        goals_to_update.append(1)
    # sql code: select target maximum from goal 2
    #if temp is less-than:
        goals_to_update.append(2)
    # sql code: select target minimum and maximum from goal 3
    #if temp is between min and max:
        goals_to_update.append(3)
    # sql code: select target minimum and maximum from goal 4
    # if temp is between min and max:
        goals_to_update.append(4)
    # sql code: select target minimum and maximum from goal 5
    # if temp is between min and max:
        goals_to_update.append(5)
    # sql code: select target_text from goal 6
    #if conditions == 'clear'
        goals_to_update.append(6)
    # sql code: select target_text from goal 7
    # if conditions == 'clouds'
        goals_to_update.append(7)
    #sql code: select target min from goal 8
    # if wind greater than target min:
        goals_to_update.append(8)
    return goals_to_update()


# if weather conditions meet any goals update goals_reached table
def update_goals_reached():


# main:
# When a player starts the game, they are greeted and asked to enter their name.
# Their name is saved to the game table of our flight_game database and they are given a c02 budget of 10000.
