import tkinter
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog

parent = tkinter.Tk() # Create the object
parent.overrideredirect(1) # Avoid it appearing and then disappearing quickly
parent.iconbitmap("./icon/mamoth.ico") # Set an icon (this is optional - must be in a .ico format)
parent.withdraw() # Hide the window as we do not want to see this one

file_types = [('Eagle Library or XML', '*.lbr;*.xml'), ('All files', '*')]

def get_single_file(title):#selection of a single file.
    return filedialog.askopenfilename(title=title, filetypes=file_types, parent=parent)


def get_multiple_file(title):#Ask the user to select a one or more file names.
    return filedialog.askopenfilenames(title=title, filetypes=file_types, parent=parent)

def yes_no_prompt(winName,statement):
    return messagebox.askyesno(winName,statement,parent=parent)  # Yes / No

def yes_no_cancel_prompt(winName,statement):
    return messagebox.askyesno(winName,statement,parent=parent)  # Yes / No /cancel

def saveAs_Excel(title):
    return filedialog.asksaveasfilename(title=title, defaultextension='.',filetypes=(("Excel", "*.xls"), ("TXT", "*.txt")), parent=parent)