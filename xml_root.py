import xml.etree.ElementTree as ET

def Library_root(path_and_file):

    tree = ET.parse(path_and_file)
    root = tree.getroot()
    return root