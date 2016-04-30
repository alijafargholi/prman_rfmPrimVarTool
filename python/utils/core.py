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
from __future__ import division
import logging
import random
import colorsys

# IMPORT LOCAL MODULES
try:
    import pymel.core as pm
except ImportError as e:
    logging.error("\n\n\nThis tool was not able to import the 'pymel' "
                  "library.\nThat is required for this tool to "
                  "function.\nPlease contact the developer for assistant.\n "
                  "Contact info: ali.jafargholi@gmail.com\n\n" + (100 * "*") +
                  "\n" + str(e) + "\n" + (100 * "*") + "\n")

# Global Variables
EXISTING_ATTR = {"rmanF": {}, "rmanP": {}, "rmanV": {}, "rmanN": {},
                 "rmanC": {}, "rmanS": {}}


def add_attr(node, attr_name, debug=False, **kwargs):
    """
    Assign attributes to the given object.

    >>> import pymel.core as pm
    >>> FOO = pm.sphere()
    # Result: [nt.Transform(u'nurbsSphere1'),
               t.MakeNurbSphere(u'makeNurbSphere2')] #
    >>> shapeNode = FOO[-1]
    # Get the shape of the FOO
    >>> add_attr(shapeNode, "newAttributeName", attributeType='float')
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


def get_random_color_shade(min_s=0, max_s=1, min_v=0, max_v=1, hue=360,
                           debug=False):
    """
    Return a random shade of the given hue in RGB. The default is a random
    shade of color red.

    :param min_s: (Float) Minimum saturation of the color. Between 0 and 1.
    :param max_s: (Float) Maximum saturation of the color. Between 0 and 1.
    :param min_v: (Float) Minimum value of the color. Between 0 and 1.
    :param max_v: (Float) Maximum value of the color. Between 0 and 1.
    :param hue: (Float) Spectrum on the color. Between 1 and 360
    :param debug: (Boolean) Set True if you want to print out the result.
    """
    # Since the colorsys library takes value between 0-1, we need to
    # normalize this value by dividing it by 360
    normalized_hue = hue / 360
    random_color = colorsys.hsv_to_rgb(normalized_hue,
                                       random.uniform(min_s, max_s),
                                       random.uniform(min_v, max_v))
    if debug:
        logging.info("Generated a random color <<{}>>".format(random_color))
    return random_color


def get_random_vector(minimum_x=0, maximum_x=1,
                      minimum_y=0, maximum_y=1,
                      minimum_z=0, maximum_z=1,
                      uniform_value=False,
                      kind="float"):
    """
    Returns list of three numbers, vector, integer of float.

    :param minimum_x: (float or int) Minimum x range
    :param maximum_x: (float or int) Maximum x range
    :param minimum_y: (float or int) Minimum y range
    :param maximum_y: (float or int) Maximum y range
    :param minimum_z: (float or int) Minimum z range
    :param maximum_z: (float or int) Maximum z range
    :param uniform_value: (Boolean) If True, result in uniform result.
    :param kind: (String) Kind of vector, integer or float. Default is float.
    :return: (List) List of vector. ex: [1,0,2] or [1.234, 2.426, 1.64]
    """
    if uniform_value:
        if kind == "float":
            random_value = random.uniform(minimum_x, maximum_x)
            return [random_value, random_value, random_value]
        else:
            random_value = random.randint(minimum_x, maximum_x)
            return [random_value, random_value, random_value]

    if kind == "float":
        return random.sample([random.uniform(minimum_x, maximum_x),
                              random.uniform(minimum_y, maximum_y),
                              random.uniform(minimum_z, maximum_z)], 3)
    else:
        return random.sample([random.randint(minimum_x, maximum_x),
                              random.randint(minimum_y, maximum_y),
                              random.randint(minimum_z, maximum_z)], 3)


def get_rman_attr(nodes, debug=False):
    """
    Returns the dictionary of primvar attribute found on the given nodes.

    :param nodes: (List of PyMel nodes) Nodes to query their primvar attributes.
    :param debug: (Boolean) Set True if you want to print out the result.
    """
    global EXISTING_ATTR
    for node in nodes:
        # Go through all attributes of the current node
        for attr in pm.listAttr(node):
            # Check for existance of each primvar attributes
            for attr_type in EXISTING_ATTR.keys():
                if attr_type in attr:
                    # If current attribute doesn't exist in the database
                    # create a list for it
                    if attr not in EXISTING_ATTR[attr_type]:
                        EXISTING_ATTR[attr_type][attr] = []
                        if debug:
                            logging.info("Created the '{}' list on '{}' "
                                         "primvar database".format(attr,
                                                                   attr_type))
                    # Add the founded attribute to the list
                    EXISTING_ATTR[attr_type][attr].append(node)
                    if debug:
                        logging.info("Found '{}' on '{}'".format(attr, node))
    return EXISTING_ATTR


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


def remove_attr(node, attr_name, debug=False):
    """
    Remove the given attribute from the given node

    :param node: (PyMel Node) The object that needs to be its attribute deleted.
    :param attr_name: (Str) Name of the attribute to be deleted from the object.
    :param debug: (Boolean) Set True if you want to print out the result.
    """
    if node.hasAttr(attr_name):
        pm.deleteAttr(node, at=attr_name)
        if debug:
            logging.info("'{}' attribute was deleted from {}".format(
                attr_name, node))
    else:
        logging.warning("'{}' has no attribute called '{}'".format(node,
                                                                   attr_name))


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
            try:
                inside_nodes = list(unpack(node.getChildren()))
                if inside_nodes:
                    for inside_node in inside_nodes:
                        yield inside_node
            except AttributeError as errorLog:
                logging.error("Was not able to gather the 'Shape' of "
                              "'{}'.".format(node))
        else:
            yield node


def main():
    """
    Run help if called directly.
    """
    import __main__
    help(__main__)

__all__ = ['add_attr', 'get_random_vector', 'get_rman_attr', 'get_shapes',
           'remove_attr', 'set_attr', 'unpack']

if __name__ == '__main__':
    main()


