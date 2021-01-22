import sqlite3

conn = sqlite3.connect('db_roster')

with conn:
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS Roster( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_Name TEXT, \
        col_Species TEXT, \
        col_IQ INTEGER)")
    conn.commit()

conn.close()

conn = sqlite3.connect('db_roster')

with conn:
    cur = conn.cursor()

    values = [(1, 'Jean-Baptiste Zorg', 'Human', 122), 
                (2, 'Korben Dallas', 'Meat Popsicle', 100),
                (3, 'Ak\'not', 'Mangalore', -5)]
    cur.executemany("INSERT INTO Roster VALUES (?,?,?,?);", values);
    
    conn.commit()

conn.close()


conn = sqlite3.connect('db_roster')

with conn:
    cur = conn.cursor()

    updateQuery = """UPDATE Roster SET col_Species = 'Human' WHERE col_name = 'Korben Dallas'"""
    cur.execute(updateQuery)
    conn.commit()

conn.close()

conn = sqlite3.connect('db_roster')

with conn:
    cur = conn.cursor()

    cur.execute("SELECT col_Name, col_IQ FROM Roster")
    varRoster = cur.fetchall()

    for item in varRoster:
        print(item[0])
