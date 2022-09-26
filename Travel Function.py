
import mariadb
from geopy import distance

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
    sql = "select name FROM airport, game WHERE game.location=airport.ident AND game.screen_name={screen_name}"
    cursor = connection.cursor()
    cursor.execute(sql)
    location = cursor.fetchall()

    # determine distance between the two locations
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident= '" + iaco + "';"
    cursor = connection.cursor()
    cursor.execute(sql)
    response = cursor.fetchall()
    iaco_location = response

    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident= '" + location + "';"
    cursor = connection.cursor()
    cursor.execute(sql)
    response = cursor.fetchall()
    local = response

    trip_distance = distance.distance(iaco_location, local).km:.2f

    # calculate co2 budget conversion given the distance
    new_co2 = ''

    # if player has enough co2 to travel between locations:
        # update current location
        sql = "UPDATE game SET location=local WHERE screen_name={player}"

        # update co2 budget
        sql = "UPDATE game SET co2_consumed=new_co2 WHERE screen_name={player}"

        # compare weather conditions between current location and goals

            # if weather conditions meet any goals update goals_reached table

    # if player doesn't have enough co2, re-prompt player with original options


