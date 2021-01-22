import sqlite3

#connect to db - creates one if it doesn't exist
connection = sqlite3.connect("test_database.db")
#instantiate a cusor object
c = connection.cursor()
#create table
c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")
#Insert values
c.execute("INSERT INTO People VALUES('Ron', 'Obvious', 42)")
#commit changes
connection.commit()
#close connection
connection.close()

#create a temporary db in ram
connection = sqlite3.connect(':memory:')
#delete the people table
c.execute("DROP TABLE IF EXISTS People")

