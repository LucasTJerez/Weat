import mysql.connector
config = {
        'user': 'root',
        'password': 'Dit63yuw',
        'host': '127.0.0.1',
        'port': '3306',
        'database': 'weat',
        'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)

cnx.close();
