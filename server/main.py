import database


if __name__ == "__main__":
	mydb = database.Database(
		host="localhost", port="3306", user="root", password="root", database="member"
  )
	