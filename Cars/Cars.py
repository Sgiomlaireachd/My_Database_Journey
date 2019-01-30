import mysql.connector
from mysql.connector import Error
import matplotlib.pyplot as plt
import sys

def connect():
    try:
        db = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            passwd = sys.argv[1],
            database = 'testdb'
        )
        cursor = db.cursor()
    except Error as e:
        print(e)
        return 0,0
    else:
        print("Connected.")
        return (db,cursor)

def request(cursor,sql,title):
    cursor.execute(sql)
    result = cursor.fetchall()
    first = [i[0] for i in result]
    second = [i[1] for i in result]
    plt.bar(first,second)
    plt.title(title)
    plt.show()

def main():
    db,cursor = connect()
    request(cursor,"SELECT cyl, AVG(hp) AS AVERAGE FROM cars GROUP BY cyl ORDER BY AVERAGE;","Dependency Cyl and Hp")
    request(cursor,"SELECT origin, AVG(mpg) AS AVERAGE FROM cars GROUP BY origin ORDER BY AVERAGE;","Dependency Origin and Mpg")
    request(cursor,"SELECT origin, AVG(weight) AS AVERAGE FROM cars GROUP BY origin ORDER BY AVERAGE;","Average Weight in origins")
    request(cursor,"SELECT yr, COUNT(name) AS AMOUNT FROM cars GROUP BY yr ORDER BY AMOUNT;","Amount of cars by years")

if __name__ == "__main__": main()