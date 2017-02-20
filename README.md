# PrMan Privmar Tool - v0.2.0
Artist friendly tool for using RenderMan's Primitive Variables in Maya.


When you want variation from your RenderMan shader, you could use Primvar.
This RenderMan functionality gives you the ability to use only one shader for
many objects and create variety at render time. But the process of assigning
these attributes could be time consuming and discouraging for an artist.

To make this process easier, I created a tool that speeds up the process.
Primvar Manager for Maya.

<img src="http://alijafargholi.com/wp-content/uploads/2016/05/primVar_manager.png" alt="Drawing" style="width: 100px;margin: auto;"/>

Installation
============

1. [Download the Package](https://github.com/alijafargholi/prman_camera_projection_setup/archive/master.zip)
2. Unzip the downloaded file and rename it to **rfmPrimVarTool**.
3. Then move the entire *rfmPrimVarTool*  folder to the specified path:
    * Mac OS X
        * ~/Library/Preferences/Autodesk/maya/scripts
    * Linux
        * /maya/\<version>/scripts
    * Windows
        * \<drive>:\Documents and Settings\\\<username>\\My Documents\\maya\\scripts

4. Then in a new instance of Maya, open the script editor and run the following
 in a *Python* tab:

    ```python
    from rfmPrimVarTool.src import primVarApp
    reload(primVarApp)
    primVarApp.create_ui()
    ```

> Note:
>> Probably you don't want to run the script from the python tab
every time you wan to open the tool, you could drag and drop the code from the *python* tab to a *shell*

Release Notes
=============
* v 0.2.0
    * Added [Qt.py](https://github.com/mottosso/Qt.py) that helps the tool to be used in both Maya 2016 and 2017.
* v 0.1.0
    * First release.
    * The *Edit* section still is WIP