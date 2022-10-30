import pandas as pd

def Footprint_and_path (root_):
    fp_path = "./drawing/library/packages/"
    fp_start_string = fp_path + "package[@name='"
    fp_end_path = "']/"

    i=0
    FpNames = []
    FpAndPathDict = {}

    for item in root_.findall(fp_path):
        FpNames.append(item.attrib.get('name'))
        string = fp_start_string + FpNames[i] + fp_end_path
        FpAndPathDict[FpNames[i]]=string
        i += 1
    return FpAndPathDict

def fpParse_pin (root_,libPath):
    Fp_pin_Detail = {}
    Fp_pad_Name = []
    Fp_pad_X = []
    Fp_pad_Y = []
    Fp_drill_dia = []
    Fp_pad_shape = []
    Fp_Pin_Dir = []
    Fp_Pin_Funct = []
    for item_ in root_.findall(libPath):
        if item_.tag == 'pin':
            Fp_pad_Name.append(item_.attrib.get('name'))
            Fp_pad_X.append(item_.attrib.get('x'))
            Fp_pad_Y.append(item_.attrib.get('y'))
            Fp_drill_dia.append(item_.attrib.get('length'))
            Fp_pad_shape.append(item_.attrib.get('rot'))
            Fp_Pin_Dir.append(item_.attrib.get('direction'))
            Fp_Pin_Funct.append(item_.attrib.get('function'))
    Fp_pin_Detail['PinName'] = Fp_pad_Name
    Fp_pin_Detail['xLoc'] = Fp_pad_X
    Fp_pin_Detail['yLoc'] = Fp_pad_Y
    Fp_pin_Detail['PinLength'] = Fp_drill_dia
    Fp_pin_Detail['Rot'] = Fp_pad_shape
    Fp_pin_Detail['PinDir'] = Fp_Pin_Dir
    Fp_pin_Detail['PinFunc'] = Fp_Pin_Funct

    symPindata = pd.DataFrame(data=Fp_pin_Detail)
    #print(symPindata)
    return symPindata