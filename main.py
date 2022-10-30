import win_tkinters as dg
import SymbolParse as symPrsr

library_names = dg.get_multiple_file('Please Select one or more Eagle Libraries')
# ask the user for excel file result output
Excel_prmpt = dg.yes_no_prompt('Output Files ?', 'Want to Save Complete results in EXCEL')

symAndpath ={}

if Excel_prmpt == True:
    print("selected yes")
    save_as = dg.saveAs_Excel("Select location where to save")
    print(save_as)
else:
    print("selected no")

for library_name in library_names:
    xmlroot=symPrsr.Library_root(library_name)
#    symPrsr.symParse_pin(xmlroot)
    symAndpath = symPrsr.Symbol_and_path(xmlroot)
    for keys, values in symAndpath.items():
        print("********************************************************")
        print(keys)
        print(values)
        print(symPrsr.symParse_shape(xmlroot,values))
        print("########################################################")

    print("00000000000000000000000000000000000000000000000000000000")
