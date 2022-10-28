import xml.etree.ElementTree as ET
import pandas as pd

tree = ET.parse('./Test_Libraries/EagleTestLibrary_1.lbr')
root = tree.getroot()

SymNames = []

Symbol_Attributes_Detail = {}
Sym_Text_x = []
Sym_Text_y = []
Sym_Text_size = []
Sym_Text_layer = []
Sym_Text_actualText = []

Symbol_pin_Detail = {}
Sym_Pin_Name = []
Sym_Pin_X = []
Sym_Pin_Y = []
Sym_Pin_Length = []
Sym_Pin_Rot = []
Sym_Pin_Dir = []
Sym_Pin_Funct = []

Symbol_shape_Details = {}
Sym_Shape_x1 = []
Sym_Shape_x2 = []
Sym_Shape_y1 = []
Sym_Shape_y2 = []
Sym_Shape_width = []
Sym_Shape_layer = []

###################################################################
# FOR SYMBOLS INFO
# Gather all Symbols Names
for item in root.findall('./drawing/library/symbols/'):
    SymNames.append(item.attrib.get('name'))
    # Get all symbol names and store in sym_name list

# getting pin names with respective Symbols
sym_start_string = "./drawing/library/symbols/symbol[@name='"
sym_end_path = "']/"

for names in SymNames:
    string = sym_start_string + names + sym_end_path
    for item in root.findall(string):
        if item.tag == 'pin':
            Sym_Pin_Name.append(item.attrib.get('name'))
            Sym_Pin_X.append(item.attrib.get('x'))
            Sym_Pin_Y.append(item.attrib.get('y'))
            Sym_Pin_Length.append(item.attrib.get('length'))
            Sym_Pin_Rot.append(item.attrib.get('rot'))
            Sym_Pin_Dir.append(item.attrib.get('direction'))
            Sym_Pin_Funct.append(item.attrib.get('function'))
        if item.tag == 'wire':
            Sym_Shape_x1.append(item.attrib.get('x1'))
            Sym_Shape_y1.append(item.attrib.get('y1'))
            Sym_Shape_x2.append(item.attrib.get('x2'))
            Sym_Shape_y2.append(item.attrib.get('y2'))
            Sym_Shape_width.append(item.attrib.get('width'))
            Sym_Shape_layer.append(item.attrib.get('layer'))
        if item.tag == 'text':
            Sym_Text_x.append(item.attrib.get('x'))
            Sym_Text_y.append(item.attrib.get('y'))
            Sym_Text_size.append(item.attrib.get('size'))
            Sym_Text_layer.append(item.attrib.get('layer'))
            Sym_Text_actualText.append(item.text)

    Symbol_pin_Detail['PinName'] = Sym_Pin_Name
    Symbol_pin_Detail['xLoc'] = Sym_Pin_X
    Symbol_pin_Detail['yLoc'] = Sym_Pin_Y
    Symbol_pin_Detail['PinLength'] = Sym_Pin_Length
    Symbol_pin_Detail['Rot'] = Sym_Pin_Rot
    Symbol_pin_Detail['PinDir'] = Sym_Pin_Dir
    Symbol_pin_Detail['PinFunc'] = Sym_Pin_Funct

    Symbol_shape_Details['x1'] = Sym_Shape_x1
    Symbol_shape_Details['y1'] = Sym_Shape_y1
    Symbol_shape_Details['x2'] = Sym_Shape_x2
    Symbol_shape_Details['y2'] = Sym_Shape_y2
    Symbol_shape_Details['width'] = Sym_Shape_width
    Symbol_shape_Details['layer'] = Sym_Shape_layer

    Symbol_Attributes_Detail['x'] = Sym_Text_x
    Symbol_Attributes_Detail['y'] = Sym_Text_y
    Symbol_Attributes_Detail['size'] = Sym_Text_size
    Symbol_Attributes_Detail['layer'] = Sym_Text_layer
    Symbol_Attributes_Detail['Contains'] = Sym_Text_actualText

    Sym_Pin_Name = []
    Sym_Pin_X = []
    Sym_Pin_Y = []
    Sym_Pin_Length = []
    Sym_Pin_Rot = []
    Sym_Pin_Dir = []
    Sym_Pin_Funct = []

    Sym_Shape_x1 = []
    Sym_Shape_x2 = []
    Sym_Shape_y1 = []
    Sym_Shape_y2 = []
    Sym_Shape_width = []
    Sym_Shape_layer = []

    Sym_Text_x = []
    Sym_Text_y = []
    Sym_Text_size = []
    Sym_Text_layer = []
    Sym_Text_actualText = []

    symPindata = pd.DataFrame(data=Symbol_pin_Detail)
    symShapedata = pd.DataFrame(data=Symbol_shape_Details)
    symTextdata = pd.DataFrame(data=Symbol_Attributes_Detail)

    print(names)
    print(symPindata)
    print(symShapedata)
    print(symTextdata)
