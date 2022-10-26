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
file_types = [('Eagle Library or XML', '*.lbr;*.xml'), ('All files', '*')]
library_name = filedialog.askopenfilename(title='Select a file', filetypes=file_types, parent=parent)

# Ask the user to select a one or more file names.
#library_names = filedialog.askopenfilenames(title='Select one or more files', parent=parent)

# ask the user for excel file result output
outputExcelprompt = messagebox.askyesno('Output Excel File ?', 'Do You Want To Create an Excel File with Results?', parent=parent) # Yes / No / Cancel

if outputExcelprompt == True:
    print("selected yes")
    save_as = filedialog.asksaveasfilename(title='Save as',defaultextension='.',filetypes=(("Excel", "*.xls"),("TXT", "*.txt")),parent=parent)
    print(save_as)
    #path = filedialog.asksaveasfilename(title='Select file',defaultextension='.',filetypes=(png, eps, txt, xml))
else:
    print("selected no")

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


###################################################################
    #FOR SYMBOLS INFO
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

###################################################################
    #FOR FOOTPRINTS INFO
#Gather all Footprints Names
for item in root.findall('./drawing/library/packages/'):
    patt_name.append(item.attrib.get('name'))

## getting pad/smd names with respective Symbols
fp_start_string="./drawing/library/packages/package[@name='"
fp_end_path="']/"

for names in patt_name:        
    string=fp_start_string+names+fp_end_path
    for item in root.findall(string):
        if(item.tag=='pad'):
            Fp_pad.append(item.attrib.get('name'))
        elif(item.tag=='smd'):
            Fp_pad.append(item.attrib.get('name'))
    FpDict_pad[names]=Fp_pad
    Fp_pad=[]

###################################################################
    #FOR DEVICES INFO
#Gather all Devices Names
for item in root.findall('./drawing/library/devicesets/'):
    device_name.append(item.attrib.get('name'))
    
## getting pad/smd names with respective Symbols
dev_start_string="./drawing/library/devicesets/deviceset[@name='"
dev_sym_path="']/gates/"
end_str="']/"
dev_fp_path="']/devices/"

#Devices with Respective symbols and Footprints (Seperate dictionaries)
for names in device_name:
    string=dev_start_string+names+dev_sym_path
    for item in root.findall(string):
        if(item.tag=='gate'):
            Dev_SymList.append(item.attrib.get('symbol'))
    Dev_SymDict[names]=Dev_SymList
    Dev_SymList=[]
    ## gathers Device ,[Symbols]

    string=dev_start_string+names+dev_fp_path
    for item in root.findall(string):
        if(item.tag=='device'):
            Dev_FpList.append(item.attrib.get('package'))
    Dev_FpDict[names]=Dev_FpList
    Dev_FpList=[]
    ## gathers Device ,[Footprints]

#shove them in Dictionary.. One Dictionary for all Names
libDict["Symbol"]=sym_name
libDict["LandPattern"]=patt_name
libDict["Device"]=device_name
#Number of total items in the Library
for key in libDict:
    libItems_countDict[key]=len(libDict[key])
    # getting total number of Syms, Fps, and Devs in a lbr file.
print("This Library ",library_name," Contains : ")
print("".join("| {0:<13s}->{1:>8d} |\n".format(k, v) for k, v in libItems_countDict.items()))
