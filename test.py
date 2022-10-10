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



def available_co2():
    sql = "select @co2_left:= co2_budget - co2_consumed as co2_left from game where screen_name= 'Vesa' ;"
    cursor = connection.cursor()
    cursor.execute(sql)
    co2_avail = cursor.fetchall()
    print(co2_avail[0][0])
    return co2_avail



print(available_co2())