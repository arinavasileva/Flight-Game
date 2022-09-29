
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


def travel():
    # ask for IACO code of where the player wants to go
    iaco = input("enter IACO code")
    # determine current location
    sql = "SELECT ident FROM airport, game WHERE game.location=airport.ident AND game.screen_name='Heini'"
    cursor = connection.cursor()
    cursor.execute(sql)
    location = cursor.fetchall()
    # get variable to store current location:
    str_location = ''
    for row in location:
        str_location = row[0]
        print(f"{row[0]}")

    # determine distance between the two locations:
    # Desired location lat and long:
# def desired_lat_and_long(icao)
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident= '" + iaco + "';"
    cursor = connection.cursor()
    cursor.execute(sql)
    response1 = cursor.fetchall()
    for row in response1:
        print(f"{row[0]}")
        print(f"{row[1]}")

    # Current location lat and long:
#def current_lat_and_long( icao code)
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident= '" + str_location + "';"
    cursor = connection.cursor()
    cursor.execute(sql)
    response2 = cursor.fetchall()
    lat = ''
    long = ''
    for row in response2:
        lat = row[0]
        long = row[1]
        print(lat, long)


# Distance between current and travel location
    trip_distance = GD(response1, response2).km
    print(f"the distance is {trip_distance}km")

    # calculate co2 available
    sql = "select @co2_left:= co2_budget - co2_consumed as co2_left from game where screen_name = 'Heini';"
    cursor = connection.cursor()
    cursor.execute(sql)
    response3 = cursor.fetchall()
    co2_left = response3
    # store new available co2 as a variable:
    for row in co2_left:
        co2_left = row[0]
        print(f"co2 left: {co2_left}")


    # if player has enough co2 to travel between locations:
    if co2_left >= trip_distance:
        # update current location
        sql = "UPDATE game SET location=local WHERE screen_name='Heini'"
        cursor = connection.cursor()
        cursor.execute(sql)

        # update co2 budget
        new_co2 = co2_left - trip_distance
        sql = "UPDATE game SET co2_consumed="+new_co2+" WHERE screen_name='Heini'"
        cursor = connection.cursor()
        cursor.execute(sql)

        # compare weather conditions between current location and goals

            # if weather conditions meet any goals update goals_reached table

    # if player doesn't have enough co2, re-prompt player with original options
    if trip_distance > co2_left:
        return


travel()


