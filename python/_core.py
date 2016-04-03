#! /usr/bin/env python
# This free software incorporates by reference the text of the WTFPL, Version 2

"""
The core functionality for Primvar tool.

.. module:: `_core`
   :platform: Unix, Windows
   :synopsis: Provides core functionality of PrimVar tool.

.. moduleauthor:: Ali Jafargholi <ali.jafargholi@gmail.com>
"""

# IMPORT STANDARD MODULES
import os
import logging
import random

# IMPORT LOCAL MODULES
try:
    import pymel.core as pm
except ImportError as e:
    logging.error("\n\n\nThis tool was not able to import the 'pymel' "
                  "library.\nThat is required for this tool to "
                  "function.\nPlease contact the developer for assistant.\n "
                  "Contact info: ali.jafargholi@gmail.com\n\n" + (100 * "*") +
                  "\n" + str(e) + "\n" + (100 * "*") + "\n")


def add_attr(node, attr_name, debug=False, **kwargs):
    """
    Assign attributes to the given object.

    >>> import pymel.core as pm
    >>> FOO = pm.sphere()
    # Result: [nt.Transform(u'nurbsSphere1'), t.MakeNurbSphere(u'makeNurbSphere2')] #
    >>> shapeNode = FOO[-1]
    # Get the shape of the FOO
    >>> assign_attr(shapeNode, "newAttributeName", attributeType='float')
    # Create a new attribute called "newAttributeName", type float

    :param node: (PyMel nodes) Object to assign new attributes to.
    :param attr_name: (String) attributes name
    :param debug: (Boolean) Set True if you want to print out the result.
    :param kwargs: attribute keywords. ex:
    """

    # Add the attribute if it already doesn't exist
    if not node.hasAttr(attr_name):
        pm.addAttr(node, longName=attr_name, **kwargs)
        if debug:
            logging.info("Attribute '{}' is added to {}".format(attr_name,
                                                                node))
    else:
        logging.warning("Attribute '{}' already exists on {}".format(attr_name,
                                                                     node))


def get_random_vector(minimum=0, maximum=1, kind="float"):
    """
    Returns list of three numbers, vector, integer of float.

    :param minimum: (float or int) Minimum range
    :param maximum: (float or int) Maximum range
    :param kind: (String) Kind of vector, integer or float. Default is float.
    :return vector: (List) List of vector. ex: [1,0,2] or [1.234, 2.426, 1.64]
    """
    if kind == "float":
        return random.sample([random.uniform(minimum, maximum),
                              random.uniform(minimum, maximum),
                              random.uniform(0, maximum)], 3)
    else:
        return random.sample([random.randint(minimum, maximum),
                              random.randint(minimum, maximum),
                              random.randint(0, maximum)], 3)


def get_shapes(nodes, debug=False):
    """
    Yields the name on shape node for each selected object.

    :param nodes: (List of PyMel node) objects to be check for shape node.
    :param debug: (Boolean) If True, it'll output the errors and the process.
    :yield: (PyMel node) shape node of the selected node.
    """
    for node in nodes:
        # If the current selection is a shape node, yield it
        if isinstance(node, pm.nodetypes.Shape):
            yield node
        else:
            # Try to get the shape node and yield the node
            try:
                yield node.getShape()
                if debug:
                    logging.info("Found {} node on {} transform node".format(
                        node.getShape(), node))
            except Exception as e:
                logging.warning("can't find a shape node for {}.\n{}".format(
                    node, e))


def set_attr(node, attr_name, value, debug=False):
    """
    Setting the attribute of the object

    :param node: (PyMel nodes) Object to set its attribute.
    :param attr_name: (String) Attribute name of the object to be set.
    :param value: (String, Int, Float) Value of the attribute to set.
    :param debug: (Boolean) Print out the process of setting the attribute
    """
    try:
        pm.setAttr("{}.{}".format(node, attr_name), value)
        if debug:
            logging.info("{}.{} is set to '{}'".format(node, attr_name, value))
    except Exception as e:
        logging.warning("Can not find {} on {}.\n{}".format(attr_name, node, e))


def unpack(nodes, debug=False):
    """
    Return true if the given node is a group

    :param nodes: (PyMel node) a node to be checked if a group
    :param debug: (Boolean) If True, it'll output the errors and the process.
    :return: True if the node is a group and False otherwise.
    """
    for node in nodes:
        if not pm.listRelatives(node, shapes=1):
            if debug:
                logging.info("Unpacking '{}' group node".format(node))
            inside_nodes = list(unpack(node.getChildren()))
            if inside_nodes:
                for inside_node in inside_nodes:
                    yield inside_node
        else:
            yield node


def main():
    """
    Simply run help if called directly.
    """
    import __main__
    help(__main__)

__all__ = ['add_attr', 'get_random_vector', 'get_shapes', 'set_attr', 'unpack']

if __name__ == '__main__':
    main()


