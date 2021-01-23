import shutil
import os
from datetime import datetime, timedelta
import time

#set where the source of the files are
source = '/Users/kristinskelton/Documents/GitHub/Python-Projects/File-Transfer/FolderC/'

#set the destination path to folderB
destination = '/Users/kristinskelton/Documents/GitHub/Python-Projects/File-Transfer/FolderD/'
files = os.listdir(source)


#iterate through the files
for i in files:
    #get the date from the file
    modifyDate = datetime.fromtimestamp(os.path.getmtime(source+i))
    #get today's date
    todaysDate = datetime.today()

    #get the date 24 hours ago
    modifyDateLimit = modifyDate + timedelta(days=1)

    #if the date modified is greater than today's date
    if modifyDateLimit > todaysDate:
        #copy the files from one path to another
        shutil.copy(source+i, destination+i)

