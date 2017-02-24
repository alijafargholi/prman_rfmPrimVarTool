Installation
============

Please follow these instruction to install the package correctly.

Default Installation
********************

.. _Click here to download the Package: https://github.com/alijafargholi/prman_rfmPrimVarTool/archive/master.zip

1. `Click here to download the Package`_:


2. Unzip the downloaded file and rename it to **rfmPrimVarTool**.
3. Then move the entire *rfmPrimVarTool*  folder to the specified path:

    * Mac OS X
       * ~/Library/Preferences/Autodesk/maya/scripts
    * Linux
       * /maya/<version>/scripts
    * Windows
       * <drive>:\\Documents and Settings\\<username>\\My Documents\\maya\\scripts

4. Then in a new instance of Maya, open the script editor and run the following
   in your *Python* tab:

.. code-block:: python

    from rfmPrimVarTool.src import primVarApp
    reload(primVarApp)
    primVarApp.create_ui()


Custom Installation
*******************

In case you don't have access to any of the above location, you can install this tool in a custom location. Following steps describe how to do it:

.. _Click here to download the Package: https://github.com/alijafargholi/prman_rfmPrimVarTool/archive/master.zip

1. `Click here to download the Package`_:


2. Unzip the downloaded file and rename it to **rfmPrimVarTool**.
3. Then move the entire *rfmPrimVarTool*  folder to any location you want:
4. Then in a new instance of Maya, open the script editor and run the following in a *Python* tab:

.. code-block:: python

    import sys, os

    # Update this path to where you copied the package
    PATH_TO_PACKAGE = r"REPLACE/ME/WITH/PATH/TO/WHERE/YOU/COPIED/THE/PACKAGE"

    src_path = os.path.realpath(PATH_TO_PACKAGE)

    # Adding the location to system path
    if not src_path in sys.path:
       sys.path.append(src_path)
       print "added {} to the path\n".format(src_path)

    from rfmPrimVarTool.src import primVarApp
    reload(primVarApp)
    primVarApp.create_ui()


.. note::
    Make sure you set the PATH_TO_PACKAGE to where you copied the *rfmPrimVarTool* package

    example:

    If the path to *rfmPrimVarTool* is this:

    **/Users/Shared/Autodesk/maya/scripts/rfmPrimVarTool**

    Then you need to set the *PATH_TO_PACKAGE* as follow:

    **PATH_TO_PACKAGE = r"/Users/Shared/Autodesk/maya/scripts"**
