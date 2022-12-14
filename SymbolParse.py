import pandas as pd
import layersEagle as LE

def Symbol_and_path (root_):
    symbols_path = "./drawing/library/symbols/"
    sym_start_string = symbols_path + "symbol[@name='"
    sym_end_path = "']/"

    i=0
    SymNames = []
    SymAndPathDict = {}

    for item in root_.findall(symbols_path):
        SymNames.append(item.attrib.get('name'))
        string = sym_start_string + SymNames[i] + sym_end_path
        SymAndPathDict[SymNames[i]]=string
        i += 1
    return SymAndPathDict

# def symParse_detail (root_,libPath):
#

def symParse_pin (root_,libPath):
    Symbol_pin_Detail = {}
    Sym_Pin_Name = []
    Sym_Pin_X = []
    Sym_Pin_Y = []
    Sym_Pin_Length = []
    Sym_Pin_Rot = []
    Sym_Pin_Dir = []
    Sym_Pin_Funct = []
    for item_ in root_.findall(libPath):
        if item_.tag == 'pin':
            Sym_Pin_Name.append(item_.attrib.get('name'))
            Sym_Pin_X.append(item_.attrib.get('x'))
            Sym_Pin_Y.append(item_.attrib.get('y'))
            Sym_Pin_Length.append(item_.attrib.get('length'))
            Sym_Pin_Rot.append(item_.attrib.get('rot'))
            Sym_Pin_Dir.append(item_.attrib.get('direction'))
            Sym_Pin_Funct.append(item_.attrib.get('function'))
    Symbol_pin_Detail['PinName'] = Sym_Pin_Name
    Symbol_pin_Detail['xLoc'] = Sym_Pin_X
    Symbol_pin_Detail['yLoc'] = Sym_Pin_Y
    Symbol_pin_Detail['PinLength'] = Sym_Pin_Length
    Symbol_pin_Detail['Rot'] = Sym_Pin_Rot
    Symbol_pin_Detail['PinDir'] = Sym_Pin_Dir
    Symbol_pin_Detail['PinFunc'] = Sym_Pin_Funct

    symPindata = pd.DataFrame(data=Symbol_pin_Detail)
    #print(symPindata)
    return symPindata

def symParse_text (root_,libPath):
    Symbol_Attributes_Detail = {}
    Sym_Text_x = []
    Sym_Text_y = []
    Sym_Text_size = []
    Sym_Text_layer = []
    Sym_Text_actualText = []
    for item_ in root_.findall(libPath):
        if item_.tag == 'text':
            Sym_Text_x.append(item_.attrib.get('x'))
            Sym_Text_y.append(item_.attrib.get('y'))
            Sym_Text_size.append(item_.attrib.get('size'))
            Sym_Text_layer.append(LE.getNamefromNumLayers(item_.attrib.get('layer')))
            Sym_Text_actualText.append(item_.text)
    Symbol_Attributes_Detail['x'] = Sym_Text_x
    Symbol_Attributes_Detail['y'] = Sym_Text_y
    Symbol_Attributes_Detail['size'] = Sym_Text_size
    Symbol_Attributes_Detail['layer'] = Sym_Text_layer
    Symbol_Attributes_Detail['Contains'] = Sym_Text_actualText

    symTextdata = pd.DataFrame(data=Symbol_Attributes_Detail)
    return symTextdata

def symParse_shape (root_,libPath):
    Symbol_shape_Details = {}
    Sym_Shape_x1 = []
    Sym_Shape_x2 = []
    Sym_Shape_y1 = []
    Sym_Shape_y2 = []
    Sym_Shape_width = []
    Sym_Shape_layer = []

    # Get all symbol names and store in sym_name list
    for item_ in root_.findall(libPath):
        if item_.tag == 'wire':
            Sym_Shape_x1.append(item_.attrib.get('x1'))
            Sym_Shape_y1.append(item_.attrib.get('y1'))
            Sym_Shape_x2.append(item_.attrib.get('x2'))
            Sym_Shape_y2.append(item_.attrib.get('y2'))
            Sym_Shape_width.append(item_.attrib.get('width'))
            Sym_Shape_layer.append(LE.getNamefromNumLayers(item_.attrib.get('layer')))
        Symbol_shape_Details['x1'] = Sym_Shape_x1
        Symbol_shape_Details['y1'] = Sym_Shape_y1
        Symbol_shape_Details['x2'] = Sym_Shape_x2
        Symbol_shape_Details['y2'] = Sym_Shape_y2
        Symbol_shape_Details['width'] = Sym_Shape_width
        Symbol_shape_Details['layer'] = Sym_Shape_layer
    symShapedata = pd.DataFrame(data=Symbol_shape_Details)
    return symShapedata