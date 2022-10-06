import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='root123',
    autocommit=True
)
def get_municipality(id):
    location = "SELECT name, municipality FROM airport WHERE ident ='"+id+"'"
    cursor = connection.cursor()
    cursor.execute(location)
    result = cursor.fetchall()
    for row in result:
        print(f"The Airport is in  {row[0]} in {row[1]}.")
    return

airport_id = input("ENTER ident")
get_municipality()


# The input is Ident(primary key of the airport table)
# The output is the name of the airport and municipality.