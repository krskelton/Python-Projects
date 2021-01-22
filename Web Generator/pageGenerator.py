"""
Python Ver: 3.9

Author:     Kristin Skelton

Purpose:    Create files, Open browser windows with webbrowser module,
            Tkinter GUI module

"""

import webbrowser
import os
from tkinter import *
import tkinter as tk


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry("{}x{}".format(300, 200))
        self.master.title("Web Page Generator")

        self.varPhrase = StringVar()

        #label   
        self.lbl_phrase = tk.Label(self.master, text='Enter phrase:')
        self.lbl_phrase.grid(row=0, column=0, padx=(40,30), pady=(30,0))

        #input field
        self.txt_phrase = tk.Entry(self.master, text=self.varPhrase)
        self.txt_phrase.grid(row=1, column=0, padx=(40,30), pady=(30,30))

        #submit button
        self.btn_submit = tk.Button(self.master, text="Submit", command=self.submit)
        self.btn_submit.grid(row=2, column=0, padx=(40,30), pady=(0,30))

    def submit(self):
        phrase = self.varPhrase.get()

        #create file if not already created
        htmlFile = open("index.html", "w")
        #write code to file
        htmlFile.write("<html><body><h1>" + phrase + "</h1></body></html>")
        #close file
        htmlFile.close()

        #get file name that we just created
        fileName = 'index.html'
        #open in a new tab
        webbrowser.open('file://' + os.path.realpath(fileName))

        


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
    


