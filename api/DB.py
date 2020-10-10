import sqlite3
import pandas as pd

class DB:

    def __init__(self):

        self.connect()

        self.cur = self.conn.cursor()

        #self.cur.execute("DROP TABLE IF EXISTS restaurants")

        self.checkDB()

    def connect(self):
        print("="*10 + "Connecting To weat.db" + "="*10)
        self.conn = sqlite3.connect('weat.db')
        print("="*10 + "Connection Successful" + "="*10)

    def checkDB(self):
        self.cur.execute(" SELECT name FROM sqlite_master WHERE type='table'")
        tables = self.cur.fetchone()
        if(tables):
            print("weat.db contains tables:")
            for table in tables:
                #print(pd.read_sql_query("SELECT * FROM {tableName}".format(tableName = table), self.conn))
                print('\t'+table)
        else:
            print("weat.db does not exist.\n Creating table \"restaurants\" and filling it with values from mock_database.csv")
            self.fillMockDB()

    def fillMockDB(self,):
        mock_data = pd.read_csv("./data/mock_database.csv") 
        df = pd.DataFrame(mock_data)
        df.to_sql("restaurants", self.conn, if_exists="replace")




