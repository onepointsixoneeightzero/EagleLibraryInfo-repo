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
    Fp_padSmd_type =[]
    Fp_pad_Name = []
    Fp_pad_X = []
    Fp_pad_Y = []
    Fp_drill_dia = []
    Fp_thruholeCu_dia = []
    Fp_pad_shape = []

    Fp_smd_dx = []
    Fp_smd_dy = []
    Fp_smd_layer = []



    for item_ in root_.findall(libPath):
        if item_.tag == 'pad' or item_.tag == 'smd':
            Fp_padSmd_type.append(item_.tag)
            Fp_pad_Name.append(item_.attrib.get('name'))
            Fp_pad_X.append(item_.attrib.get('x'))
            Fp_pad_Y.append(item_.attrib.get('y'))
            Fp_drill_dia.append(item_.attrib.get('drill'))
            Fp_thruholeCu_dia.append(item_.attrib.get('diameter'))
            Fp_pad_shape.append(item_.attrib.get('shape'))
            Fp_smd_dx.append(item_.attrib.get('dx'))
            Fp_smd_dy.append(item_.attrib.get('dy'))
            Fp_smd_layer.append(item_.attrib.get('layer'))

    Fp_pin_Detail['Pad_Type'] = Fp_padSmd_type
    Fp_pin_Detail['Pad_Name'] = Fp_pad_Name
    Fp_pin_Detail['xLoc'] = Fp_pad_X
    Fp_pin_Detail['yLoc'] = Fp_pad_Y
    Fp_pin_Detail['Drill'] = Fp_drill_dia
    Fp_pin_Detail['Cu_dia'] = Fp_thruholeCu_dia
    Fp_pin_Detail['shape/thru'] = Fp_pad_shape
    Fp_pin_Detail['dx'] = Fp_smd_dx
    Fp_pin_Detail['dy'] = Fp_smd_dy
    Fp_pin_Detail['layer_smd'] = Fp_smd_layer

    FpPadData = pd.DataFrame(data=Fp_pin_Detail)
    return FpPadData

def fpParse_onlySmd (root_,libPath):
    Fp_pin_Detail = {}
    Fp_padSmd_type =[]
    Fp_pad_Name = []
    Fp_pad_X = []
    Fp_pad_Y = []
    Fp_smd_dx = []
    Fp_smd_dy = []
    Fp_smd_layer = []

    for item_ in root_.findall(libPath):
        if item_.tag == 'smd':
            SMD_PAD_FLAG = 0
            Fp_padSmd_type.append(item_.tag)
            Fp_pad_Name.append(item_.attrib.get('name'))
            Fp_pad_X.append(item_.attrib.get('x'))
            Fp_pad_Y.append(item_.attrib.get('y'))
            Fp_smd_dx.append(item_.attrib.get('dx'))
            Fp_smd_dy.append(item_.attrib.get('dy'))
            Fp_smd_layer.append(item_.attrib.get('layer'))

        elif item_.tag == 'pad':
            SMD_PAD_FLAG=1

    if SMD_PAD_FLAG ==0:
        Fp_pin_Detail['Pad_Type'] = Fp_padSmd_type
        Fp_pin_Detail['Pad_Name'] = Fp_pad_Name
        Fp_pin_Detail['xLoc'] = Fp_pad_X
        Fp_pin_Detail['yLoc'] = Fp_pad_Y
        Fp_pin_Detail['dx'] = Fp_smd_dx
        Fp_pin_Detail['dy'] = Fp_smd_dy
        Fp_pin_Detail['layer_smd'] = Fp_smd_layer

        FpPadData = pd.DataFrame(data=Fp_pin_Detail)
        return FpPadData
    elif SMD_PAD_FLAG ==1:
        return "NO SMD PRESENT"

def fpParse_onlyPAD (root_,libPath):
    Fp_pin_Detail = {}
    Fp_padSmd_type =[]
    Fp_pad_Name = []
    Fp_pad_X = []
    Fp_pad_Y = []
    Fp_drill_dia = []
    Fp_thruholeCu_dia = []
    Fp_pad_shape = []


    for item_ in root_.findall(libPath):
        if item_.tag == 'pad':
            SMD_PAD_FLAG = 0
            Fp_padSmd_type.append(item_.tag)
            Fp_pad_Name.append(item_.attrib.get('name'))
            Fp_pad_X.append(item_.attrib.get('x'))
            Fp_pad_Y.append(item_.attrib.get('y'))
            Fp_drill_dia.append(item_.attrib.get('drill'))
            Fp_thruholeCu_dia.append(item_.attrib.get('diameter'))
            Fp_pad_shape.append(item_.attrib.get('shape'))

        elif item_.tag == 'smd':
            SMD_PAD_FLAG=1

    if SMD_PAD_FLAG ==0:
        Fp_pin_Detail['Pad_Type'] = Fp_padSmd_type
        Fp_pin_Detail['Pad_Name'] = Fp_pad_Name
        Fp_pin_Detail['xLoc'] = Fp_pad_X
        Fp_pin_Detail['yLoc'] = Fp_pad_Y
        Fp_pin_Detail['Drill'] = Fp_drill_dia
        Fp_pin_Detail['Cu_dia'] = Fp_thruholeCu_dia
        Fp_pin_Detail['shape/thru'] = Fp_pad_shape

        FpPadData = pd.DataFrame(data=Fp_pin_Detail)
        return FpPadData
    elif SMD_PAD_FLAG ==1:
        return "NO ThruHole PRESENT"