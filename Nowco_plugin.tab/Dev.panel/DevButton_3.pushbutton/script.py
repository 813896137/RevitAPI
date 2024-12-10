# -*- coding: utf-8 -*-
__title__   = "Create Column by Grids"
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
import clr
clr.AddReference('System')
from System.Collections.Generic import List
from Autodesk.Revit.DB.Structure import StructuralType
# pyRevit
from pyrevit import revit

# Revit Document and Transaction
app    = __revit__.Application
uidoc  = __revit__.ActiveUIDocument
doc    = __revit__.ActiveUIDocument.Document #type:Document

# 2B Define Renaming Rules
from rpw.ui.forms import *
components = [Label('Base Level (number):'), TextBox('level_nmb'),
            Separator(),      Button('Create Column by Grids')]

# Create UI Form + Show it
form = FlexForm('Column Placement', components)
form.show()


user_inputs = form.values
if not user_inputs:
    print("Operation canceled.")
    exit()

level_nmb = user_inputs['level_nmb']
level_name = "L{}".format(level_nmb)

# Transaction to place columns
t = Transaction(doc, 'Place Columns at Grid Intersections')

# Collect Level
level_collector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Levels).WhereElementIsNotElementType()
level = next((lvl for lvl in level_collector if lvl.Name == level_name), None)

if not level:
    print("Error: Level '{}' not found.".format(level_name))
    exit()

col_symbol_id = ElementId(1107653)  # Replace with your Column Family Type ID
col_symbol = doc.GetElement(col_symbol_id)

# Collect Grids
grids = FilteredElementCollector(doc).OfClass(Grid).ToElements()

# Separate Numeric and Alphabetical Grids
numeric_grids = [grid.Curve for grid in grids if grid.Name.isdigit()]
alphabetic_grids = [grid.Curve for grid in grids if not grid.Name.isdigit()]

# Find Intersections
intersections = []
result = clr.StrongBox[IntersectionResultArray](IntersectionResultArray())

for num_grid in numeric_grids:
    for alph_grid in alphabetic_grids:
        if num_grid.Intersect(alph_grid, result) == SetComparisonResult.Overlap:
            intersection_point = result.Value.get_Item(0).XYZPoint
            intersections.append(intersection_point)

# Place Columns at Intersections
t.Start()

try:
    for point in intersections:
        doc.Create.NewFamilyInstance(point, col_symbol, level, StructuralType.Column)
except Exception as e:
    print("Error: {0}".format(e))  # Use .format() for string formatting
    t.RollBack()
else:
    t.Commit()


#==================================================
#🚫 DELETE BELOW
from Snippets._customprint import kit_button_clicked    # Import Reusable Function from 'lib/Snippets/_customprint.py'
kit_button_clicked(btn_name=__title__)                  # Display Default Print Message
