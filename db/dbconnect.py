from mysql.connector import MySQLConnection

def connect():
    paramsmap = {
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': 'root',
        'database': 'yannickpythondb'
    }

    con = MySQLConnection(**paramsmap)
    return con
