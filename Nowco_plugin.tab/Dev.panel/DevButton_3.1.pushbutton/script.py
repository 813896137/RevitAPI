# -*- coding: utf-8 -*-


# Imports

from Autodesk.Revit.DB import *

import clr
clr.AddReference('System')
from System.Collections.Generic import List
from Autodesk.Revit.DB import *
# pyRevit
from pyrevit import script, revit, forms                                        # import pyRevit modules. (Lots of useful features)


# Variables
#==================================================
app    = __revit__.Application
uidoc  = __revit__.ActiveUIDocument
doc    = __revit__.ActiveUIDocument.Document #type:Document
output = script.get_output()

#import

all_walls = FilteredElementCollector(doc, doc.ActiveView.Id).OfClass(Wall).ToElements()

for wall in all_walls:
    Linkify_wall = output.linkify(wall.Id, wall.Name)
    print(Linkify_wall)

#Linkify Multiple - Walls
# all_walls = FilteredElementCollector(doc, doc.ActiveView.Id).OfClass(Wall).ToElements()
# wall_ids = [wall.Id for wall in all_walls]
# Linkify_walls = output.linkify(wall_ids, 'walls {}'.format(len(wall_ids)))
# print(Linkify_walls)

#limit 100 150 elements
# all_walls = FilteredElementCollector(doc, doc.ActiveView.Id).OfClass(Wall).ToElements()
# wall_ids = [wall.Id for wall in all_walls]
# Linkify_walls = output.linkify(wall_ids, 'walls {}'.format(len(wall_ids)))
# print('Here are all walls: {}'.format(Linkify_walls))

#linkify-View
# all_views = FilteredElementCollector(doc).OfClass(ViewPlan).ToElements()
# for view in all_views:
#     linkify_view = output.linkify(view.Id, 'View:{}'.format(view.Name))
#     print(linkify_view)