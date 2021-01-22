import sqlite3

#get personal data from user
firstName = input("enter your first name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter your age: "))
personData = (firstName, lastName, age)

#execute insert statment for supplied person data
with sqlite3.connect("test_database.db") as connection:
    c = connection.cursor()
    c.execute("INSERT INTO People VALUES(?,?,?)", personData)
    c.execute("UPDATE People SET Age=? WHERE FirstName=? AND LastName=?",
              (45, 'Luigi', 'Vercotti'))
