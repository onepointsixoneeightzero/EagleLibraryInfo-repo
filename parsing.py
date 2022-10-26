import tkinter
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog

parent = tkinter.Tk() # Create the object
parent.overrideredirect(1) # Avoid it appearing and then disappearing quickly
parent.iconbitmap("abc.ico") # Set an icon (this is optional - must be in a .ico format)
parent.withdraw() # Hide the window as we do not want to see this one

# Ask the user to select a single file name.
file_name = filedialog.askopenfilename(title='Select a file', parent=parent)

# Ask the user to select a one or more file names.
#file_names = filedialog.askopenfilenames(title='Select one or more files', parent=parent)
