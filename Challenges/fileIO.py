import os

fname = "Hello.txt"

fpath = "C:\\A\\"

abPath = os.path.join(fpath, fname)
print(abPath)
