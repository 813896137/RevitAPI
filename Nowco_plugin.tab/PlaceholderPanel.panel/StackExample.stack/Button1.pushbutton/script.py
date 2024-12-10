# -*- coding: utf-8 -*-
__title__   = "Create Sheets"
__doc__     = """Version = 1.0
Date    = 15.06.2024
________________________________________________________________
Description:

This is the placeholder for a .pushbutton
You can use it to start your pyRevit Add-In

________________________________________________________________
How-To:

1. [Hold ALT + CLICK] on the button to open its source folder.
You will be able to override this placeholder.

2. Automate Your Boring Work ;)

________________________________________________________________
TODO:
[FEATURE] - Describe Your ToDo Tasks Here
________________________________________________________________
Last Updates:
- [15.06.2024] v1.0 Change Description
- [10.06.2024] v0.5 Change Description
- [05.06.2024] v0.1 Change Description 
________________________________________________________________
Author: Erik Frits"""

# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝
#==================================================
#.NET Imports
import clr
clr.AddReference('System')
from System.Collections.Generic import List
from Autodesk.Revit.DB import *

# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝
#==================================================
app    = __revit__.Application
uidoc  = __revit__.ActiveUIDocument
doc    = __revit__.ActiveUIDocument.Document #type:Document
t = Transaction(doc, 'JG-RoomLoad')

# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝
#==================================================

#UI
from rpw.ui.forms import *
components = [Label('Sheetname:'), TextBox('sheetname'),
            Label('Sheetcount:'), TextBox('sheetcount'),
            Separator(),      Button('Createsheets')]

# Create UI Form + Show it
form = FlexForm('Title', components)
form.show()


user_inputs = form.values

sheetname = user_inputs['sheetname']
sheetcount = user_inputs['sheetcount']


t.Start()
shtnam = []
shtnbr = []

for i in range(int(sheetcount)):
    shtnam.append(str(sheetname))
    shtnbr.append(str(sheetname) + str(101 + i))
sheetlist = []

for num in range(int(sheetcount)):
    sht = ViewSheet.Create(doc, ElementId(952584))
    sht.Name = shtnam[num]
    sht.SheetNumber = shtnbr[num]
    sheetlist.append(sht)

t.Commit()


#==================================================
#🚫 DELETE BELOW
from Snippets._customprint import kit_button_clicked    # Import Reusable Function from 'lib/Snippets/_customprint.py'
kit_button_clicked(btn_name=__title__)                  # Display Default Print Message
