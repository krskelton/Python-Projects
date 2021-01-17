import sqlite3

#connect to a database
conn = sqlite3.connect('test.db')

#while the connection is open
with conn:
    #the cursor is operating on the db
    cur = conn.cursor()
    #build the database
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_persons( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT,\
            col_lname TEXT, \
            col_email TEXT \
            )")
    #commit the changes
    conn.commit()
#close the connection to the db
conn.close()


#connect to a database again
conn = sqlite3.connect('test.db')

#while the connection is open
with conn:
    #the cursor is operating on the db
    cur = conn.cursor()
    #build the database
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email)\
        VALUES (?, ?, ?)",\
                ('Bob', 'Smith', 'bsmith@gmail.com'))
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email)\
        VALUES (?, ?, ?)",\
                ('Sarah', 'Jones', 'sjones@gmail.com'))
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email)\
        VALUES (?, ?, ?)",\
                ('Kristin', 'Skelton', 'kskelton82@gmail.com'))
    #commit the changes
    conn.commit()
#close the db
conn.close()



#connect to a database again
conn = sqlite3.connect('test.db')

#while the connection is open
with conn:
    #the cursor is operating on the db
    cur = conn.cursor()
    #build the database
    cur.execute("SELECT col_fname, col_lname, col_email FROM tbl_persons WHERE col_fname = 'Sarah'")
    #get the info on the cursor cause that's where the command you just executed lives
    varPerson = cur.fetchall()
    #iterate through the tuple
    for item in varPerson:
        msg = "First name: {}\nLastName: {}\nEmail: {}".format(item[0], item[1], item[2])

    print(msg)
