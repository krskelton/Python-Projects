import os

fname = "text.txt"
path = "/Users/kristinskelton/Documents/GitHub/Python-Projects/Challenges"

dirs = os.listdir(path)

for file in dirs:
    if file.endswith(".txt"):
        joinedPath = os.path.join(path, fname)
        time = os.path.getmtime(joinedPath)
        print (file + " " + str(time))

