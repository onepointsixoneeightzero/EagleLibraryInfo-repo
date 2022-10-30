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