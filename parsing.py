import tkinter
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog
import xml.etree.ElementTree as ET
import json

parent = tkinter.Tk() # Create the object
parent.overrideredirect(1) # Avoid it appearing and then disappearing quickly
parent.iconbitmap("abc.ico") # Set an icon (this is optional - must be in a .ico format)
parent.withdraw() # Hide the window as we do not want to see this one

# Ask the user to select a single file name.
library_name = filedialog.askopenfilename(title='Select a file', parent=parent)

# Ask the user to select a one or more file names.
#library_names = filedialog.askopenfilenames(title='Select one or more files', parent=parent)


###########################################



tree= ET.parse(library_name)
#tree= ET.parse('passive.lbr')
root=tree.getroot()

libDict={key: [] for key in ['Symbol', 'LandPattern', 'Device']}
#Create a dictionary with SYMBOL LANDPATTER AND DEVICES as keys
libItems_countDict={}
sym_name=[]
patt_name=[]
device_name=[]

SymDict_pin={}# Key = Symbol_Name; Value = Symbol_Pins
Sym_pins=[]# for Name of pins
FpDict_pad={}# Key = Fp_Name; Value = Fp_Pads+SMDs
Fp_pad=[]# for Name of pads
Dev_FpDict={}# Key = Dev_Name; Value = Fp_Name
Dev_FpList=[] # for names of FP/s in a device
Dev_SymDict={}# Key = Dev_Name; Value = Sym_Name
Dev_SymList=[]# for names of Sym/s in a device

## ^^ JUST A LOT OF VARIABLEs


#Gather all Symbols Names
for item in root.findall('./drawing/library/symbols/'):
    sym_name.append(item.attrib.get('name'))
    # Get all symbol names and store in sym_name list

## getting pin names with respective Symbols
sym_start_string="./drawing/library/symbols/symbol[@name='"
sym_end_path="']/"

for names in sym_name:        
    string=sym_start_string+names+sym_end_path
    for item in root.findall(string):
        if(item.tag=='pin'):
            Sym_pins.append(item.attrib.get('name'))
    SymDict_pin[names]=Sym_pins
    Sym_pins=[]
    # Get pin names with respective Symbols
print(SymDict_pin)

    
