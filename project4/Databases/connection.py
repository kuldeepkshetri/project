import mysql.connector


class Databases:

    def connect(self):

        connection = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="password",
            database="project"
        )

        return connection















class Database:
    def connect(self):
        connection=mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='password',
        database='kuldeepid'
        )
        return connection
