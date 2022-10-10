# import mysql.connector
#
# connection = mysql.connector.connect(
#     host='127.0.0.1',
#     port=3306,
#     database='flight_game',
#     user='root',
#     password='root123',
#     autocommit=True
# )
# def get_municipality(id):
#     location = "SELECT name, municipality FROM airport WHERE ident ='"+id+"'"
#     cursor = connection.cursor()
#     cursor.execute(location)
#     result = cursor.fetchall()
#     for row in result:
#         print(f"The Airport is in  {row[0]} in {row[1]}.")
#     return
#
# airport_id = input("ENTER ident")
# get_municipality(airport_id)
#
#
#
#
# player_name = input("Enter Your Name")
#
# def greetings(name):
#     max_id = "SELECT MAX(id) from game;"
#     cursor = connection.cursor()
#     cursor.execute(max_id)
#     # connection.commit()
#     max_num = int(cursor.fetchall()[0][0])
#     sql = "INSERT INTO game (id, screen_name, co2_consumed, co2_budget, location) VALUES(" + str(max_num + 1) +",'"+name+"', 0, 10000,'EFHK');"
#     cursor = connection.cursor()
#     cursor.execute(sql)
#     cursor.fetchall()
#     connection.commit()
#     return
# greetings(player_name)


# The input is Ident(primary key of the airport table)
# The output is the name of the airport and municipality.




menu_input = input("Please Enter the number of the command which you want to run: ")
print("1- view current location.")
print("2- view goals.")
print("3- view co2 budget.")
print("4- travel to new airport")

if menu_input == 1:
    get_municipality('EFHK')
elif menu_input == 2:
    available_co2(screen_name)
elif menu_input == 3:

elif menu_input == 4:

else:
    print("Please enter a number between 1-4.")



