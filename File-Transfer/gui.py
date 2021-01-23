import shutil
import os
from datetime import datetime, timedelta
import time
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askdirectory


#Frame for gui
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #define our master frame configuration
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry("{}x{}".format(600,400))
        self.master.title("File Check")
        load_gui(self)

#build the gui
def load_gui(self):
    #gui elements for choosing the origin file path
    self.lbl_title1 = tk.Label(self.master, text="Origin File Path")
    self.lbl_title1.grid(row=0, column=0)
    self.lbl_checkFiles = tk.Label(self.master, text="File Path: ")
    self.lbl_checkFiles.grid(row=1, column=0)

    #Button for the user to choose their file with the popup directory
    self.btn_checkFilePath = tk.Button(self.master, text="Choose File", command=lambda: ChooseOriginFile(self))
    self.btn_checkFilePath.grid(row=1, column=1)

    #gui elements for choosing the destination file path
    self.lbl_title2 = tk.Label(self.master, text="Destination File Path")
    self.lbl_title2.grid(row=3, column=0)
    self.lbl_copiedFiles = tk.Label(self.master, text="File Path: ")
    self.lbl_copiedFiles.grid(row=4, column=0)

    #Button for the user to choose their file with the popup directory
    self.btn_copiedFilePath = tk.Button(self.master, text="Choose File", command=lambda: ChooseDestinationFile(self))
    self.btn_copiedFilePath.grid(row=4, column=1)

    #Button to actually copy the files from the origin to the destination
    self.btn_checkFiles = tk.Button(self.master, text="Check Files", command=lambda: CopyFiles(self))
    self.btn_checkFiles.grid(row=6, column=0)


def ChooseOriginFile(self):
    #set variable to file value
    #use askdirectory to allow the user to choose the file path
    self.varOriginPath = askdirectory()
    #display the file path on the gui window
    self.lbl_checkFilePath = tk.Label(self.master, text=self.varOriginPath)
    self.lbl_checkFilePath.grid(row=2, column=0)

def ChooseDestinationFile(self):
    #set variable to file value
    #use ask directory to allow the user to choose the file path
    self.varDestinationPath = askdirectory()
    #display the file path on the gui window
    self.lbl_checkFilePath = tk.Label(self.master, text=self.varDestinationPath)
    self.lbl_checkFilePath.grid(row=5, column=0)

def CopyFiles(self):
    #get list of files in the original folder
    files = os.listdir(self.varOriginPath)

    #iterate through the files
    for i in files:
        #get the date from the file
        modifyDate = datetime.fromtimestamp(os.path.getmtime(self.varOriginPath + "/" +i))
        #get today's date
        todaysDate = datetime.today()

        #get the date 24 hours ago
        modifyDateLimit = modifyDate + timedelta(days=1)

        #if the date modified is greater than today's date
        if modifyDateLimit > todaysDate:
            #copy the files from one path to another
            shutil.copy(self.varOriginPath+ "/" + i, self.varDestinationPath+ "/" + i)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
        
