How To
======

In this section I go over how to use each sections to create a unique attribute.

rmanC
-----

This attribute is suitable for adding color variation. Using this UI, you have
options to create:

* random color
* random shade of color
* random grayscale

.. image:: images/randomBaseColorManager.png
    :scale: 50 %
    :align: center

As you can see in above image, you have control over the name of the attributes, shade of color, value and saturation.

.. note:: All the color system in this UI is HSV.

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

This a useful variable for make variation in any shader attribute that gets floating number as an input, such as *Specular*, *Roughness*, *Bump, *Metallic*, and so on.

To demonstrate this, I assigned a *PxrLMMetal* to all the Spheres, and the
result is as follow.

.. image:: images/metallic_result.png
    :scale: 40 %
    :align: center

Then click on a *Create* button to make a new Primvar attribute UI.

Make sure to:
*Give it a meaningful name.
*Choose a appropriate *value* *type* (the float type is more common)
*Adjust the *min/max* limit.

.. image:: images/randomRmanF.png
    :scale: 50 %
    :align: center

.. note:: As previously mentioned, if you specify the *PixPrimvar* node name,
it'll automatically adjust it's value.

.. image:: images/rmanFPixrPrimVar.png
    :scale: 70 %
    :align: center

After assigning the attribute to the **selected objects** you'll see newly
created attribute on the shape node.

.. image:: images/attachedRmanFAttr.png
    :scale: 80 %
    :align: center

Then from *PxrPrimvar* node, connect the *Result F* to the any shader's attribute that you want to make variation, in this case I'm going to connect it to the *roughness*.

.. image:: images/connectPxrPrimvarFloat1.png
    :scale:  50 %
    :align: center

.. image:: images/connectPxrPrimvarFloat2.png
    :scale:  50 %
    :align: center

Once they're connected the result is as follow:

.. image:: images/rmanF_result.png
    :scale: 40 %
    :align: center

rmanS
-----

*Coming soon*