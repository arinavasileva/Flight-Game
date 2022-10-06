import mariadb
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


def update_current_location(screen_name):
    sql = "UPDATE game SET location='" + iaco + "' WHERE screen_name='Heini'"
    cursor = connection.cursor()
    cursor.execute(sql)