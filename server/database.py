import mysql.connector as mydb


class Database:
	def __init__(self, host: str, port: str, user: str, password: str, database: str):
		self.conn = mydb.connect(
			host=host, port=port, user=user, password=password, database=database,
		)
		self.conn.ping(reconnect=True)

		self.cursor = self.conn.cursor()

		print(self.conn.is_connected())

		self.cursor.execute(
			"""
			CREATE TABLE IF NOT EXISTS user(
				student_id        INT(7) NOT NULL,
				name              CHAR(30) NOT NULL,
				department        CHAR(20) NOT NULL,
				PRIMARY KEY(`student_id`)
			)
			"""
		)
		self.conn.commit()

	def register_member(self, student_id, name, department):
		self.cursor.execute(
			"""
			INSERT INTO user VALUES (%s, %s, %s);
			""",
			[student_id, name, department]
		)
		self.conn.commit()
