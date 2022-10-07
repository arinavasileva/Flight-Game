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

def current_icao(screen_name):
    sql = "SELECT ident FROM airport, game WHERE game.location=airport.ident AND game.screen_name='" + screen_name + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    response = cursor.fetchall()
    return response

def latitude_and_longitude(icao):
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident= '" + icao + "';"
    cursor = connection.cursor()
    cursor.execute(sql)
    response = cursor.fetchall()
    latitude, longitude = response
    return latitude, longitude

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
    return co2_avail


def travel(screen_name, icao):
    sql = "UPDATE game SET location='" + icao + "' WHERE screen_name='" + screen_name + "';"
    cursor = connection.cursor()
    cursor.execute(sql)
    return


def update_co2_budget(co2_avail, trip_distance, screen_name):
    new_co2 = str(co2_avail + trip_distance)
    sql = "UPDATE game SET co2_consumed=" + new_co2 + " WHERE screen_name='" + screen_name + "';"
    cursor = connection.cursor()
    cursor.execute(sql)
    return

def random_weather():
    temperature = random.randint(-40, 40)
    conditions = random.choice(['Clouds', 'Clear'])
    wind = random.randint(0, 15)
    weather = (temperature, conditions, wind)
    temp, cond, wind = weather
    return temp, cond, wind



# if weather conditions meet any goals update goals_reached table
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

def update_goals_reached(achieved_goals, screen_name):
    sql = "UPDATE goal_reached WHERE"


# main:
# When a player starts the game, they are greeted and asked to enter their name.
# Their name is saved to the game table of our flight_game database and they are given a c02 budget of 10000.



