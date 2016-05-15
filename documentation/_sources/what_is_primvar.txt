What is Primvar
===============

`RenderMan`_:

.. _RenderMan: https://renderman.pixar.com/view/how-to-primitive-variables

| A primitive variable (primVar) is a mechanism in RenderMan that allows you to
| attach arbitrary data to objects (primitives) in your scene. These values
| passe from your object to its shader at render time. Their power lies in their
| ability to overwrite shader parameters.
| For example, an object can modify the shader attached to it. For a single
| object, we can just set the shader parameter ourselves. But if we have 10,000
| objects -using the same base shader but with small differences in diffuse
| color- we don't want to make 10,000 instances of our shader and set the
| diffuse color in each of them. Instead, we harness the power of primVars and
| attach a color primVar to each object. If we set up our base shader to read
| this primVar value, we can use just one shader on all 10,000 objects.

.. image:: https://rendermansite.pixar.com/ca_twopointo_cms_data/images/12999_5829.jpg
   :align: center