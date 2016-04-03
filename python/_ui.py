#! /usr/bin/env python
# This free software incorporates by reference the text of the WTFPL, Version 2

"""
User interface for the PrimVar tool.

.. module:: `_ui`
   :platform: Unix, Windows
   :synopsis: This module creates a GUI that would help artist assign and
   modify primvar attributes to the objects.

.. moduleauthor:: Ali Jafargholi <ali.jafargholi@gmail.com>
"""

# IMPORT STANDARD MODULES
import sys

# IMPORT LOCAL MODULES
# import PySide.QtCore as QtCore
import PySide.QtGui as QtGui

# GLOBAL VARIABLE
primVarUi = None


class PrimVarUi(QtGui.QWidget):
    """

    """
    def __init__(self, *args, **kwargs):
        super(PrimVarUi, self).__init__(*args, **kwargs)


def create_ui():
    """
    Create an instance of the GUI
    :return: QWidget
    """
    global primVarUi
    if primVarUi:
        primVarUi.show()
    else:
        primVarUi = PrimVarUi()
        primVarUi.show()


def close_ui():
    """
    Clese the existing Ui
    :return: None
    """
    global primVarUi
    if primVarUi:
        primVarUi.deleteLater()
        primVarUi = None


def main():
    """
    If the application is ran in terminal, create a stand alone app and raise
    the window
    :return: QWidget
    """
    global primVarUi

    app = QtGui.QApplication(sys.argv)
    primVarUi = PrimVarUi()
    primVarUi.show()
    primVarUi.raise_()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
