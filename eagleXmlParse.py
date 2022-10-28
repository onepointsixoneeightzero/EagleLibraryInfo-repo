import xml.etree.ElementTree as ET

tree = ET.parse(library_name)
# tree= ET.parse('passive.lbr')
root = tree.getroot()

###################################################################
# FOR SYMBOLS INFO
# Gather all Symbols Names
for item in root.findall('./drawing/library/symbols/'):
    sym_name.append(item.attrib.get('name'))
    # Get all symbol names and store in sym_name list

## getting pin names with respective Symbols
sym_start_string = "./drawing/library/symbols/symbol[@name='"
sym_end_path = "']/"

for names in sym_name:
    string = sym_start_string + names + sym_end_path
    for item in root.findall(string):
        if (item.tag == 'pin'):
            Sym_pins.append(item.attrib.get('name'))
    SymDict_pin[names] = Sym_pins
    Sym_pins = []