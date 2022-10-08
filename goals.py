import mysql.connector
import mariadb

connection = mariadb.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='arina',
    password='1234',
    autocommit=True
)

def game_goals (id):
    location = "SELECT name, description FROM goal"
    location += " WHERE id='" + id + "'"
    print(location)
    cursor = connection.cursor()
    cursor.execute(location)
    result = cursor.fetchall()
    while cursor.rowcount <= 8:
        for row in result:
            print(f"Hello! The current goal is to fly to a country where the weather is {row[1]} and {row[2]}.")
    return








