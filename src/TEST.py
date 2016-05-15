import random

# Random integer between 0 and 5
# print random.randint(0, 5)

# Random float between -1 and 1
# print random.uniform(-1, 1)

# Random float between 0 and 1
# print random.random()

# Random color
# print random.sample([random.uniform(0, 1),
#                      random.uniform(0, 1), random.uniform(0, 1)], 3)

# Choice a random element of from a list
# print random.choice(["one", "two", "three", "four"])

# foo = {"bar": {"x": ["Z"]}}
#
#
# if "x" not in foo["bar"]:
#     foo["bar"]["x"] = []
#     foo["bar"]["x"].append("Y")
# else:
#     print foo["bar"]["x"]
#

# IMPORT STANDARD MODULES
import os
import logging
import random

# IMPORT LOCAL MODULES
import core
try:
    import pymel.core as pm

except ImportError as e:
    logging.error("\n\n\nThis tool was not able to import the 'pymel' "
                  "library.\nThat is required for this tool to "
                  "function.\nPlease contact the developer for assistant.\n "
                  "Contact info: ali.jafargholi@gmail.com\n\n" + (100 * "*") +
                  "\n" + str(e) + "\n" + (100 * "*") + "\n")

shapes = list(core.get_shapes(core.unpack(pm.ls(sl=True))))
shapeNode = shapes[0]

# create float attribute -------------------------------------------------------
core.add_attr(shapeNode, "rmanFmetalicX13", attributeType='double')

# create color attribute -------------------------------------------------------
core.add_attr(shapeNode, "rmanFmetalicXX22", attributeType='float3',
               usedAsColor=True)

core.add_attr(shapeNode, "r", attributeType='float', parent="rmanFmetalicXX22")
core.add_attr(shapeNode, "g", attributeType='float', parent="rmanFmetalicXX22")
core.add_attr(shapeNode, "b", attributeType='float', parent="rmanFmetalicXX22")

# create vector attribute ------------------------------------------------------
core.add_attr(shapeNode, "rmanNtangant", attributeType='float3')

core.add_attr(shapeNode, "x", attributeType='float', parent="rmanNtangant")
core.add_attr(shapeNode, "y", attributeType='float', parent="rmanNtangant")
core.add_attr(shapeNode, "z", attributeType='float', parent="rmanNtangant")

# create string attribute
# -------------------------------------------------------
core.add_attr(shapeNode, "rmanSbaseColor", dataType="string")

# Assign random color ----------------------------------------------------------
for node in shapes:
    core.add_attr(node, "rmanFbaseColor", attributeType='float3',
                   usedAsColor=True)

    core.add_attr(node, "r", attributeType='float', parent="rmanFbaseColor")
    core.add_attr(node, "g", attributeType='float', parent="rmanFbaseColor")
    core.add_attr(node, "b", attributeType='float', parent="rmanFbaseColor")

for node in shapes:
    core.set_attr(node, "rmanFbaseColor", core.get_random_vector())