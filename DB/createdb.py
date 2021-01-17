import sqlite3

#connect to a database
conn = sqlite3.connect('example.db')

#while the connection is open
with conn:
    #the cursor is operating on the db
    cur = conn.cursor()
    #build the database
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fileName TEXT)")
    #commit the changes
    conn.commit()
#close the connection to the db
conn.close()



#connect to a database again
conn = sqlite3.connect('example.db')

#while the connection is open
with conn:
    #the cursor is operating on the db
    cur = conn.cursor()

    #create the list of files
    fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
                'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

    #iterate through fileList and find the files that end with .txt
    for file in fileList:
        if file.endswith(".txt"):
            #add the file to the db
            cur.execute("INSERT INTO tbl_files(col_fileName) VALUES(?)", (file,))
    #commit the changes
    conn.commit()
#close the db
conn.close()



#connect to a database again
conn = sqlite3.connect('example.db')

#while the connection is open
with conn:
    #the cursor is operating on the db
    cur = conn.cursor()
    #build the database
    cur.execute("SELECT col_fileName FROM tbl_files")
    #get the info on the cursor cause that's where the command you just executed lives
    varFiles = cur.fetchall()
    #iterate through the tuple
    for item in varFiles:
        print(item[0])
        msg = "File Name: {}".format(item[0])
        print(msg)
