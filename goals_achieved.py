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


def random_weather():
    temperature = random.randint(-40, 40)
    conditions = random.choice(['Clouds', 'Clear'])
    wind = random.randint(0, 15)
    weather = (temperature, conditions, wind)
    temp, cond, wind = weather
    return temp, cond, wind


def goals_achieved(temperature, conditions, wind):
    achieved_goals = []
    sql_statement = ['target_minvalue', 'target_maxvalue', ('target_minvalue', 'target_maxvalue'), ('target_minvalue', 'target_maxvalue'), ('target_minvalue', 'target_maxvalue'), 'target_text', 'target_text', 'target_minvalue']
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

temp, condition, wind = random_weather()
print(temp, condition, wind)
print(goals_achieved(temp, condition, wind))
