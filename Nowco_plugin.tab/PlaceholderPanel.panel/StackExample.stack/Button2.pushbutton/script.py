# -*- coding: utf-8 -*-
__title__   = "Retrieve Materials"
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
from Autodesk.Revit.DB import *
#.NET Imports
import clr
clr.AddReference('System')
from System.Collections.Generic import List

# pyRevit
from pyrevit import revit, forms

# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝
#==================================================
app    = __revit__.Application
uidoc  = __revit__.ActiveUIDocument
doc    = __revit__.ActiveUIDocument.Document #type:Document
t = Transaction(doc, 'Retrieve Wall Materials')

# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝
#==================================================

sel_id = uidoc.Selection.GetElementIds()
sel_elem = [doc.GetElement(e_id) for e_id in sel_id]
sel_Element = [el for el in sel_elem if isinstance(el, (Wall, Floor))]


#Ensure Views Selected
if not sel_Element:
    forms.alert("No Wall/Slab selected. please try again", exitscript= True)

t.Start()

Wallname = []
wallcount = 1
for E in sel_Element:
    nam_mar = []
    # Retrieve the WallType of the wall element
    if isinstance(E, Wall):
        w_type = E.WallType
        Tpy_text = 'Wall'
    elif isinstance(E, Floor):
        w_type = E.FloorType
        Tpy_text = 'Floor'
    else:
        continue
    # Get the compound structure of the wall type to access its layers
    com_strc = w_type.GetCompoundStructure()

    if com_strc is not None:
        num_lay = com_strc.LayerCount
        lst = []

        # Loop through each layer and get material ID
        for i in range(num_lay):
            layid = com_strc.GetMaterialId(i)
            # Check if the material ID is valid
            if layid != ElementId.InvalidElementId:
                lst.append(layid)

        # Retrieve and print the material names for each layer
        for n in range(len(lst)):
            mat = doc.GetElement(lst[n])
            nam_mar.append( '(' + 'Layer' + str(n + 1) + '-' + mat.Name + ')')
    wall_info = E.Name + '-' + Tpy_text + ' ' + str(wallcount) + ': ' + ', '.join(nam_mar)
    Wallname.append(wall_info)
    wallcount += 1
t.Commit()

for name in Wallname:
    print(name)
#🤖 Automate Your Boring Work Here





#==================================================
#🚫 DELETE BELOW
from Snippets._customprint import kit_button_clicked    # Import Reusable Function from 'lib/Snippets/_customprint.py'
kit_button_clicked(btn_name=__title__)                  # Display Default Print Message
