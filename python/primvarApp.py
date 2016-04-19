# IMPORT STANDARD MODULES
import os
import logging
import random

# IMPORT LOCAL MODULES
import _core
try:
    import pymel.core as pm

except ImportError as e:
    logging.error("\n\n\nThis tool was not able to import the 'pymel' "
                  "library.\nThat is required for this tool to "
                  "function.\nPlease contact the developer for assistant.\n "
                  "Contact info: ali.jafargholi@gmail.com\n\n" + (100 * "*") +
                  "\n" + str(e) + "\n" + (100 * "*") + "\n")

shapes = list(_core.get_shapes(_core.unpack(pm.ls(sl=True))))
shapeNode = shapes[0]

# create float attribute -------------------------------------------------------
_core.add_attr(shapeNode, "rmanFmetalicX13", attributeType='double')

# create color attribute -------------------------------------------------------
_core.add_attr(shapeNode, "rmanFmetalicXX22", attributeType='float3',
               usedAsColor=True)

_core.add_attr(shapeNode, "r", attributeType='float', parent="rmanFmetalicXX22")
_core.add_attr(shapeNode, "g", attributeType='float', parent="rmanFmetalicXX22")
_core.add_attr(shapeNode, "b", attributeType='float', parent="rmanFmetalicXX22")

# create vector attribute ------------------------------------------------------
_core.add_attr(shapeNode, "rmanNtangant", attributeType='float3')

_core.add_attr(shapeNode, "x", attributeType='float', parent="rmanNtangant")
_core.add_attr(shapeNode, "y", attributeType='float', parent="rmanNtangant")
_core.add_attr(shapeNode, "z", attributeType='float', parent="rmanNtangant")

# create string attribute
# -------------------------------------------------------
_core.add_attr(shapeNode, "rmanSbaseColor", dataType="string")

# Assign random color ----------------------------------------------------------
for node in shapes:
    _core.add_attr(node, "rmanFbaseColor", attributeType='float3',
                   usedAsColor=True)

    _core.add_attr(node, "r", attributeType='float', parent="rmanFbaseColor")
    _core.add_attr(node, "g", attributeType='float', parent="rmanFbaseColor")
    _core.add_attr(node, "b", attributeType='float', parent="rmanFbaseColor")

for node in shapes:
    _core.set_attr(node, "rmanFbaseColor", _core.get_random_vector())
