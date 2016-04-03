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
import PySide.QtCore as QtCore
import PySide.QtGui as QtGui
import maya.OpenMayaUI as mui
# import sip

# GLOBAL VARIABLE
primVarUi = None


class PrimVarUi(QtGui.QDialog):
    """

    """
    def __init__(self, *args, **kwargs):
        super(PrimVarUi, self).__init__(*args, **kwargs)

        # Window Settings
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowTitle("PrimVar Manager")
        self.setObjectName("primVarManager")
        self.setFixedWidth(400)

        # Layout
        self.setLayout(QtGui.QVBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(0)

        # Adding scroll area
        scroll_area = QtGui.QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFocusPolicy(QtCore.Qt.NoFocus)
        scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.layout().addWidget(scroll_area)

        # Main Widget
        main_widget = QtGui.QWidget()
        main_layout = QtGui.QVBoxLayout()
        main_layout.setContentsMargins(2, 2, 2, 2)
        main_layout.setSpacing(1)
        main_layout.setAlignment(QtCore.Qt.AlignTop)
        main_widget.setLayout(main_layout)
        scroll_area.setWidget(main_widget)

    #     self._dock_widget = self._dock_name = None
    #
    # def connect_dock_widget(self, dock_name, dock_widget):
    #     self._dock_name = dock_name
    #     self._dock_widget = dock_widget
    #
    # def close(self):
    #     if self._dock_widget:
    #         pm.deleteUI(self._dock_widget)
    #     else:
    #         QtGui.QDialog.close(self)
    #         self._dock_widget = self._dock_name = None


def create_ui(dock=True):
    """
    Create an instance of the GUI
    :return: QWidget
    """
    global primVarUi
    if not primVarUi:
        primVarUi = PrimVarUi()

    # if dock:
    #     point_to_maya = mui.MQtUtil.mainWindow()
    #     main_maya_window = sip.wrapinstance(long(point_to_maya), QtCore.QObject)
    #
    #     # Parenting the PrimVar UI to the Maya window
    #     primVarUi.setParent(main_maya_window)
    #     ui_size = primVarUi.size()
    #
    #     maya_window_name = mui.MQtUtil.fullName(
    #         long(sip.unwrapinstance(primVarUi)))
    #
    #     dock_info = pm.dockControl(
    #         allowedArea=['right', 'left'],
    #         area='right',
    #         float=False,
    #         content=maya_window_name,
    #         width=ui_size.width(),
    #         height=ui_size.height(),
    #         label="PrimVar Manager"
    #     )
    #
    #     widget = mui.MQtUtil.findControl(dock_info)
    #     dock_widget = sip.wrapinstance(long(widget), QtCore.QObject)
    #
    #     primVarUi.connect_dock_widget(dock_info, dock_widget)

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
