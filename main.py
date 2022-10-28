import win_tkinters as dg
import SymbolParse as symPrsr

library_names = dg.get_multiple_file('Please Select one or more Eagle Libraries')
# ask the user for excel file result output
Excel_prmpt = dg.yes_no_prompt('Output Files ?', 'Want to Save Complete results in EXCEL')

if Excel_prmpt == True:
    print("selected yes")
    save_as = dg.saveAs_Excel("Select location where to save")
    print(save_as)
else:
    print("selected no")

for library_name in library_names:
    symPrsr.symParse(symPrsr.Library_root(library_name))

