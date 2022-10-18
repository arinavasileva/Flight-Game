import mariadb
import random
from geopy.distance import geodesic as GD
from prettytable import PrettyTable

connection = mariadb.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game2',
         user='root',
         password='root123',
         autocommit=True
         )

def greetings(name):
    sql = "INSERT INTO game(co2_consumed, co2_budget, screen_name, location) VALUES (0, 10000, '"+name+"', 'EFHK');"
    cursor = connection.cursor()
    cursor.execute(sql)
    print(f"Hello {name}!  Below you will find a list of options:")
    print("")
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


def get_airports(country):
    sql = "select airport.name as 'airport name', airport.ident as 'icao code' from airport, country where " \
          "airport.iso_country=country.iso_country and country.name='" + country + "' and airport.type = " \
                                                                                   "'large_airport'; "
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    table = PrettyTable(["Airport", "ICAO"])
    table.padding_width = 2
    table.align["Airport"] = "l"
    for i in result:
        icao = i[1]
        airport = i[0]
        table.add_row([airport, icao])
    print(table)
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
    sql_statement = ['target_minvalue', 'target_maxvalue', ['target_minvalue', 'target_maxvalue'], ['target_minvalue', 'target_maxvalue'], ['target_minvalue', 'target_maxvalue'], 'target_text', 'target_text', 'target_minvalue']
    for i in range(8):
        if i == 2 or i == 3 or i == 4:
            sql = "SELECT " + sql_statement[i][0] + "," + sql_statement[i][1] + " FROM goal WHERE id = '" + str(i + 1) + "';"
            cursor = connection.cursor()
            cursor.execute(sql)
            response = cursor.fetchall()
            target_minimum = []
            target_maxvalue = []
            for row in response:
                target_minimum = row[0]
                target_maxvalue = row[1]
            if target_minimum <= temperature <= target_maxvalue:
                achieved_goals.append(i+1)
        else:
            sql = "SELECT "+sql_statement[i]+" FROM goal WHERE id = '"+str(i+1)+"';"
            cursor = connection.cursor()
            cursor.execute(sql)
            response = cursor.fetchall()
            if i == 0:
                if temperature > int(response[0][0]):
                    achieved_goals.append(1)
            if i == 1:
                if temperature < response[0][0]:
                    achieved_goals.append(2)
            if i == 5 or i == 6:
                if response[0][0] == conditions:
                    achieved_goals.append(i+1)
            if i == 7:
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