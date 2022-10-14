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
'''
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
    return co2_avail[0]


player_id = find_id("Vesa")
icao = ('kjfk')


print(player_id)
print(current_icao(player_id))
distance = calculate_distance_km(icao, current_icao(player_id))
print(distance)
print(available_co2('Vesa'))


def get_municipality(icao):
    location = "SELECT name, municipality FROM airport WHERE ident ='"+icao+"'"
    cursor = connection.cursor()
    cursor.execute(location)
    result = cursor.fetchall()
    return result


airport = get_municipality('kjfk')

print(airport[0][0])
print(airport[0][1])


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
    for i in check_goals(id):
        list1.append(i[0])
    list2 = goals_to_update
    new_list = [item for item in list2 if item not in list1]


    return new_list


weather = random_weather()
goals = goals_achieved(weather[0], weather[1], weather[2])
print(update_goals_reached(goals, 63))


def update_co2_budget(id):
    sql = "SELECT co2_consumed FROM game WHERE id ='" + id + "';"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result[0][0]

print(update_co2_budget('63'))




def get_airports(country):
    sql = "select airport.name as 'airport name', airport.ident as 'icao code' from airport, country where " \
          "airport.iso_country=country.iso_country and country.name='" + country + "' and airport.type = " \
                                                                                   "'large_airport'; "
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        icao = row[1]
        airport = row[0]
        print(f"{icao}: {airport}")
    return



'''
search = input("Would you like to search for ICAO codes? Y/N?")
while search != '':
    if search == 'Y':
        country = input("Enter the country you would like to travel to: ")
        get_airports(country)
        break
    elif search == 'N':
        break
    else:
        print("Please enter Y or N")
        search = input("Would you like to search for ICAO codes? Y/N?")