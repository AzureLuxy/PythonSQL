import mysql.connector

host = 'localhost'
user = 'userpython'
password = '339933'
database = 'study'

connection = mysql.connector.connect(host=host, user=user, password=password, database=database)

cursor = connection.cursor()

#SQL-запросс
sql_query = "SELECT title, name_author, name_genre, price, amount from author a INNER JOIN book b ON b.author_id=a.author_id INNER JOIN genre g ON g.genre_id=b.genre_id WHERE g.genre_id IN    (SELECT query.genre_id from        (SELECT genre_id, sum(amount) AS total_amount from book GROUP BY genre_id) query WHERE total_amount = (SELECT MAX(total_amount) FROM (SELECT SUM(amount) AS total_amount FROM book GROUP BY genre_id) subquery)) ORDER by title;"

cursor.execute(sql_query)

columns = [desc[0] for desc in cursor.description]

print("|", "|".join(columns), "|")

results = cursor.fetchall()

for row in results:
    print("|", "|".join(str(value) for value in row), "|")

cursor.close()
connection.close()
input("Нажмите Enter для выхода")