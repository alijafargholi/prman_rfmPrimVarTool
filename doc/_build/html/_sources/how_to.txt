How To Use Primvar Variable Manager Tool
========================================

In this section I go over how to use each sections to create a unique attribute.

rmanC
-----

This attribute is sutable for adding color variation. Using this UI, you have
options to create:

* random color
* random shade of color
* random grayscale

.. image:: images/randomBaseColorManager.png
    :scale: 50 %
    :align: center

As you can see in above image, you have control over the name of the
    attributes, shade of color, value and saturation.

.. note:: The color system in this UI is HSV.

Here are some examples of using this attribute to generate different results:

Random Color
^^^^^^^^^^^^

1. Choose a new attribute name
2. Select a random color option
3. Modify the saturation and value as you desire

.. note:: (optional, this apply to all the Primvar attributes) specify the name
 of the PxrPrimvar node. This option will you help to set the correct name and
 attributes on the PxrPrimvar node.

4. Select your objects, and click on the **assign** button to attach the new attribute to them.
5. Set the **same** attribute name to the PxrPrimvar node and set type to **color**. If had already specified name of the PxrPrimvar in the UI, it'll bee set automatically.

.. image:: images/randomColorPxrPrimvar.png
    :scale:  50 %
    :align: center

5. Connect the RGB output of the PxrPrimvar to any input color of your shade, in this case baseColor.

.. image:: images/connectPxrPrimvarColor1.png
    :scale:  50 %
    :align: center

.. image:: images/connectPxrPrimvarColor2.png
    :scale:  50 %
    :align: center

Here is the result:

.. image:: images/randomColor_result.png
    :scale: 70 %
    :align: center

.. important:: If you open the *shapeNode* attribute editor of any of the objects, you'll see the new attribute is added.

.. image:: images/shapeNodeAttributeaditor.png

Random Shade of Color
^^^^^^^^^^^^^^^^^^^^^

1. Choose the **Random Shade of Color** option.
2. Click on the color picker button next to it an pick a *Hue*. Remember that you are just picking a hue in HSV color system, meaning that value and saturation will be adjust in the following section.

.. image:: images/selectColor.png
    :scale: 70 %
    :align: center

3. Set the *Max* and *Min* of the **Value** and **Saturation** to add some variation to the *Hue*
4. Assign the attribute, and connect the result RGB of the PxrPrimvar to the color input.

.. image:: images/randomBlue_result.png
    :scale: 70 %
    :align: center

Random Grayscale
^^^^^^^^^^^^^^^^

And here is the result of using the **Random Grayscale** options.

.. image:: images/randomGrayscale_result.png
    :scale: 70 %
    :align: center

rmanF
-----

This is rmanF

rmanS
-----

This is rmanS

rmanV
-----

This is rmanV

rmanP
-----

This is rman P

rmanN
-----

This is rmanN

