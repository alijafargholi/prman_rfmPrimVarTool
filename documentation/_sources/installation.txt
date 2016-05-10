Installation
============

`Click here to download`_:

.. _Click here to download: https://github.com/alijafargholi/prman_rfmPrimVarTool/archive/master.zip

Unzip the downloaded file and rename it to **rfmPrimVarTool**. Then move the entire *rfmPrimVarTool*  folder to the specified path:

* Mac OS X
   * ~/Library/Preferences/Autodesk/maya/scripts
* Linux
   * /maya/<version>/scripts
* Windows
   * <drive>:\\Documents and Settings\\<username>\\My Documents\\maya\\scripts

Then in a new instance of Maya, open the script editor and run the following in your *Python* tab:

.. code-block:: python
    :emphasize-lines: 1

    from rfmPrimVarTool.src import primVarApp; reload(primVarApp); primVarApp.create_ui()

.. note:: Since probably you don't want to run the script from the python tab everytime you wan to open the tool, you could drag and drop the code from the *python* tab to a *shell*