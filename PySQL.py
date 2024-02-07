import os
import mysql.connector

host = "localhost"
user = "userpython"
password = "339933"
database = "study"
folder = "queries"


def local_query(sql_query):
    connection = mysql.connector.connect(
        host=host, user=user, password=password, database=database
    )
    cursor = connection.cursor()
    cursor.execute(sql_query)
    columns = [desc[0] for desc in cursor.description]
    print("|", "|".join(columns), "|")
    results = cursor.fetchall()
    for row in results:
        print("|", "|".join(str(value) for value in row), "|")
    cursor.close()
    connection.close()


def query_from_file(file_name):
    with open(file_name, "r") as file:
        return file.read()
def main():
    while True:
        try:
            query_number = int(input("Введите номер запроса для выполнения: "))
            file_path = os.path.join(folder, f"{query_number}query.sql")
            sql_query = query_from_file(file_path)
            local_query(sql_query)
        except FileNotFoundError:
            print("Файл не найден. Пожалуйста, введите существующий номер запроса.")
        except ValueError:
            print("Пожалуйста, введите корректный номер запроса (целое число).")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()