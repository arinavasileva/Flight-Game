import mariadb
connection = mariadb.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password='root123',
         autocommit=True
         )
print("Hello! Welcome to Flight Game")

player_name = input("Enter Your Name")

def greetings(name):
    sql = "SELECT * FROM game INSERT INTO game (screen_name, co2_budget) VALUES('"+name+"');"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result
greetings(player_name)




