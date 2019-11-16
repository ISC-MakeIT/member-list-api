import mysql.connector as mydb


class Database:
    def __init__(self, host: str, port: str, user: str, password: str, database: str):
        self.conn = mydb.connect(
            host=host, port=port, user=user, password=password, database=database,
        )
        self.conn.ping(reconnect=True)
        self.cursor = self.conn.cursor()
        print(self.conn.is_connected())
