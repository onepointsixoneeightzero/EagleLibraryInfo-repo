import xml.etree.ElementTree as ET
import pandas as pd

tree = ET.parse('./Test_Libraries/EagleTestLibrary_1.lbr')
root = tree.getroot()

Symbol_Detail={}
Sym_Pin_Name=[]
Sym_Pin_X=[]
Sym_Pin_Y=[]
Sym_Pin_Length=[]
Sym_Pin_Rot=[]
Sym_Pin_Dir=[]
Sym_Pin_Funct=[]

SymDict_Pin={}
Sym_Pins = []
SymName=[]
###################################################################
# FOR SYMBOLS INFO
# Gather all Symbols Names
for item in root.findall('./drawing/library/symbols/'):
    SymName.append(item.attrib.get('name'))
    # Get all symbol names and store in sym_name list

## getting pin names with respective Symbols
sym_start_string = "./drawing/library/symbols/symbol[@name='"
sym_end_path = "']/"

Naam='pinname'

for names in SymName:
    string = sym_start_string + names + sym_end_path
    for item in root.findall(string):
        if (item.tag == 'pin'):
            Sym_Pin_Name.append(item.attrib.get('name'))
        if (item.tag == 'pin'):
            Sym_Pin_X.append(item.attrib.get('x'))
        if (item.tag == 'pin'):
            Sym_Pin_Y.append(item.attrib.get('y'))
        if (item.tag == 'pin'):
            Sym_Pin_Length.append(item.attrib.get('length'))
        if (item.tag == 'pin'):
            Sym_Pin_Rot.append(item.attrib.get('rot'))
        if (item.tag == 'pin'):
            Sym_Pin_Dir.append(item.attrib.get('direction'))
        if (item.tag == 'pin'):
            Sym_Pin_Funct.append(item.attrib.get('function'))


    Symbol_Detail['PinName']=Sym_Pin_Name
    Symbol_Detail['xLoc'] = Sym_Pin_X
    Symbol_Detail['yLoc'] = Sym_Pin_Y
    Symbol_Detail['PinLength'] = Sym_Pin_Length
    Symbol_Detail['Rot'] = Sym_Pin_Rot
    Symbol_Detail['PinDir'] = Sym_Pin_Dir
    Symbol_Detail['PinFunc'] = Sym_Pin_Funct

    Sym_Pin_Name = []
    Sym_Pin_X = []
    Sym_Pin_Y = []
    Sym_Pin_Length = []
    Sym_Pin_Rot = []
    Sym_Pin_Dir = []
    Sym_Pin_Funct = []


    print(names)
    df=pd.DataFrame(data=Symbol_Detail)
    print(df)
