import xml.etree.ElementTree as ET
import pandas as pd

def Library_root(path_and_file):

    tree = ET.parse(path_and_file)
    root = tree.getroot()
    return root

def symParse(root_):

    SymNames = []

    simpleSYMdetail = {}

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
    sym_start_string = "./drawing/library/symbols/symbol[@name='"
    sym_end_path = "']/"
    i=0
    for item in root_.findall('./drawing/library/symbols/'):

        SymNames.append(item.attrib.get('name'))
        # print(item.attrib.values())
        string = sym_start_string + SymNames[i] + sym_end_path
        # Get all symbol names and store in sym_name list

        for item_ in root_.findall(string):
            if item_.tag == 'pin':
                Sym_Pin_Name.append(item_.attrib.get('name'))
                Sym_Pin_X.append(item_.attrib.get('x'))
                Sym_Pin_Y.append(item_.attrib.get('y'))
                Sym_Pin_Length.append(item_.attrib.get('length'))
                Sym_Pin_Rot.append(item_.attrib.get('rot'))
                Sym_Pin_Dir.append(item_.attrib.get('direction'))
                Sym_Pin_Funct.append(item_.attrib.get('function'))
            if item_.tag == 'wire':
                Sym_Shape_x1.append(item_.attrib.get('x1'))
                Sym_Shape_y1.append(item_.attrib.get('y1'))
                Sym_Shape_x2.append(item_.attrib.get('x2'))
                Sym_Shape_y2.append(item_.attrib.get('y2'))
                Sym_Shape_width.append(item_.attrib.get('width'))
                Sym_Shape_layer.append(item_.attrib.get('layer'))
            if item_.tag == 'text':
                Sym_Text_x.append(item_.attrib.get('x'))
                Sym_Text_y.append(item_.attrib.get('y'))
                Sym_Text_size.append(item_.attrib.get('size'))
                Sym_Text_layer.append(item_.attrib.get('layer'))
                Sym_Text_actualText.append(item_.text)

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

        print(SymNames[i])
        print(symPindata)
        print(symShapedata)
        print(symTextdata)
        i += 1