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

# player_name = input("Enter Your Name")
#
# def greetings(name):
#     sql = "INSERT INTO game (screen_name, co2_consumed, co2_budget, location) VALUES ('"+name+"', 0, 10000,'EFHK');"
#     cursor = connection.cursor()
#     cursor.execute(sql)
#     connection.commit()
#     return
# greetings(player_name)


player_name = input("Enter Your Name")

def greetings(name):
    max_id = "SELECT MAX(id) from game;"
    cursor = connection.cursor()
    cursor.execute(max_id)
    # connection.commit()
    max_num = int(cursor.fetchall()[0][0])
    sql = "INSERT INTO game (id, screen_name, co2_consumed, co2_budget, location) VALUES(" + str(max_num + 1) +",'"+name+"', 0, 10000,'EFHK');"
    cursor = connection.cursor()
    cursor.execute(sql)
    cursor.fetchall()
    connection.commit()
    return
greetings(player_name)




