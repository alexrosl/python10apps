import mysql.connector

con = mysql.connector.connect(
    user="root",
    password="password",
    host="localhost",
    port="3306",
    database="english_dictionary"
)
cursor = con.cursor()

word = input("Enter word: ")

query = cursor.execute("SELECT * FROM cities WHERE definition='%s'" % word)
results = cursor.fetchall()

if results:
    for result in results:
        print(result[0])
else:
    print("No results")