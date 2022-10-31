import pandas as pd

LayersDict = {'1': 'Top', '2': 'Route2', '3': 'Route3', '4': 'Route4', '5': 'Route5', '6': 'Route6', '7': 'Route7',
              '8': 'Route8', '9': 'Route9', '10': 'Route10', '11': 'Route11', '12': 'Route12', '13': 'Route13',
              '14': 'Route14', '15': 'Route15', '16': 'Bottom', '17': 'Pads', '18': 'Vias', '19': 'Unrouted',
              '20': 'Dimension', '21': 'tPlace', '22': 'bPlace', '23': 'tOrigins', '24': 'bOrigins', '25': 'tNames',
              '26': 'bNames', '27': 'tValues', '28': 'bValues', '29': 'tStop', '30': 'bStop', '31': 'tCream',
              '32': 'bCream', '33': 'tFinish', '34': 'bFinish', '35': 'tGlue', '36': 'bGlue', '37': 'tTest',
              '38': 'bTest', '39': 'tKeepout', '40': 'bKeepout', '41': 'tRestrict', '42': 'bRestrict',
              '43': 'vRestrict', '44': 'Drills', '45': 'Holes', '46': 'Milling', '47': 'Measures', '48': 'Document',
              '49': 'Reference', '51': 'tDocu', '52': 'bDocu', '88': 'SimResults', '89': 'SimProbes', '90': 'Modules',
              '91': 'Nets', '92': 'Busses', '93': 'Pins', '94': 'Symbols', '95': 'Names', '96': 'Values', '97': 'Info',
              '98': 'Guide'}

layer_table = {}

layer_dict = {}

layer_num = []
layer_name = []
layer_color = []
layer_fill = []
layer_visible = []
layer_active = []

print(len(LayersDict))

def getNamefromNumLayers(num):
    return str(LayersDict[str(num)])


def Read_layers_from_lib(root):
    for item_ in root.findall("./drawing/layers/"):
        if item_.tag == 'layer':
            layer_name.append(item_.attrib.get('name'))
            layer_num.append(item_.attrib.get('number'))
            layer_color.append(item_.attrib.get('color'))
            layer_fill.append(item_.attrib.get('fill'))
            layer_visible.append(item_.attrib.get('visible'))
            layer_active.append(item_.attrib.get('active'))
    layer_table['LayName'] = layer_name
    layer_table['LayNum'] = layer_num
    layer_table['LayColor'] = layer_color
    layer_table['LayFill'] = layer_fill
    layer_table['LayVisible'] = layer_visible
    layer_table['LayActive'] = layer_active

    LayerData = pd.DataFrame(data=layer_table)
    return LayerData

    # layer_dict = dict(zip(layer_name, layer_num)) # for ziping two list in a dict
