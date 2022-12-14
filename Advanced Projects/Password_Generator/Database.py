import sqlite3 as sql


# Class for the DataBase

class sqldb(object):

	def __init__(self, Website_Name, User_Input, Password_Input):

		self.Website_Name = Website_Name
		self.User_Input = User_Input
		self.Password_Input = Password_Input
		self.connection = sql.connect('DataBase.db')
		self.cursor = self.connection.cursor()

		try:
			self.cursor.execute('CREATE TABLE DataBase (Website TEXT, Username TEXT, Password TEXT)')
			self.connection.commit()
		except sql.OperationalError():
			pass

	def __addData__(self):

		self.cursor.execute('INSERT INTO DataBase VALUES(?,?,?)', (self.Website_Name, self.User_Input, self.Password_Input))
		self.connection.commit()

	def __FetchData__(self):

		self.cursor.execute('SELECT * FROM DataBase WHERE Website=?', (self.Website_Name))
		row = self.cursor.fetchall()
		for rows in row:
			print(rows)
