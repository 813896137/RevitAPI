# -*- coding: utf-8 -*-
__title__   = "Newco"
__doc__     = """Version = 1.0
Date    = 10.30.2024
________________________________________________________________
Description:

Rename Views in Revit by using find/replace Logic.

________________________________________________________________
How-To:

1. Click on the button
2. select views
3.Define Renaming Rules
4. Rename View

________________________________________________________________
TODO:

________________________________________________________________

________________________________________________________________
Author: Justin Guo"""



# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝
#==================================================
from Autodesk.Revit.DB import *

import clr
clr.AddReference('System')
from System.Collections.Generic import List

# pyRevit
from pyrevit import revit, forms                                        # import pyRevit modules. (Lots of useful features)


# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝
#==================================================
app    = __revit__.Application
uidoc  = __revit__.ActiveUIDocument
doc    = __revit__.ActiveUIDocument.Document #type:Document


# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝
#==================================================

#Select Views
sel_id = uidoc.Selection.GetElementIds()
sel_elem = [doc.GetElement(e_id) for e_id in sel_id]
sel_views = [el for el in sel_elem if issubclass(type(el), View)]

#if none selected
if not sel_views:
    sel_views = forms.select_views()

#Ensure Views Selected
if not sel_views:
    forms.alert("oh no! Justin! no view selected. please try again", exitscript= True)

# 2A Define Renaming Rules
# prefix = 'JG_'
# find = 'FloorPlan'
# replace = 'Justin_Level'
# suffix = ''

# 2B Define Renaming Rules
from rpw.ui.forms import *
components = [Label('Prefix:'), TextBox('prefix'),
            Label('Find:'), TextBox('find'),
            Label('Replace:'), TextBox('replace'),
            Label('Suffix:'), TextBox('suffix'),
            Separator(),      Button('Rename_Views')]

# Create UI Form + Show it
form = FlexForm('Title', components)
form.show()


user_inputs = form.values

prefix = user_inputs['prefix']
find = user_inputs['find']
replace = user_inputs['replace']
suffix = user_inputs['suffix']


t = Transaction(doc, 'JG-Rename Views')
t.Start()
for view in sel_views:
    old_name = view.Name
    new_name = prefix + old_name.replace(find, replace) + suffix
    for i in range(20):
        try:
            view.Name = new_name
            print('{} -> {}' .format(old_name, new_name))
            break
        except:
            new_name += '*'


t.Commit()
print('-'*50)
print('Justin you did!')

#==================================================
#🚫 DELETE BELOW
from Snippets._customprint import kit_button_clicked    # Import Reusable Function from 'lib/Snippets/_customprint.py'
kit_button_clicked(btn_name=__title__)                  # Display Default Print Message
