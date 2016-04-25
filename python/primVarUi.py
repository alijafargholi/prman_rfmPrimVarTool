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
import os
import random
import logging
from functools import partial

# IMPORT LOCAL MODULES
import PySide.QtCore as QtCore
import PySide.QtGui as QtGui
from gui.cPrimVarWidget import CprimVarWidgets
from gui.fPrimVarWidget import FprimVarWidgets
from gui.nvpmPrimVarWidgets import NVPMprimVarWidgets
from gui.sPrimVarWidgets import SprimVarWidgets

from utils import core
from gui.images import images_rc

try:
    import pymel.core as pm
except ImportError as e:
    logging.error("\n\n\nThis tool was not able to import the 'pymel' "
                  "library.\nThat is required for this tool to "
                  "function.\nPlease contact the developer for assistant.\n "
                  "Contact info: ali.jafargholi@gmail.com\n\n" + (80 * "*") +
                  "\n" + str(e) + "\n" + (80 * "*") + "\n")

# GLOBAL VARIABLE
primVarUi = None
NEW_ATTRS = []

__version__ = "0.1.0"


class PrimVarUi(QtGui.QMainWindow):
    """

    """
    def __init__(self, *args, **kwargs):
        super(PrimVarUi, self).__init__(*args, **kwargs)
        self.setup_ui()
        # self.setup_stylesheet()
        self.setup_signals()

    def setup_ui(self):
        # Window Settings
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QtGui.QIcon(":/icons/windowIcon"))
        self.setWindowTitle("Primitive Variables(primVar) Manager - v{"
                            "}".format(__version__))
        self.setObjectName("primVarManager")
        self.setMinimumWidth(550)
        self.resize(550, 700)
        central_widget = QtGui.QWidget()
        self.central_layout = QtGui.QVBoxLayout()
        central_widget.setLayout(self.central_layout)
        self.setCentralWidget(central_widget)

        wiki_action = QtGui.QAction(QtGui.QIcon(''), '&Wiki', self)
        wiki_action.setStatusTip("Got to wiki page")
        wiki_action.triggered.connect(self.go_to_wiki)

        close_action = QtGui.QAction(QtGui.QIcon('../images/exit.png'), '&Exit',
                                     self)
        close_action.setStatusTip('Exit application')
        close_action.triggered.connect(close_ui)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        file_menu.addAction(wiki_action)
        file_menu.addAction(close_action)

        # Layout ---------------------------------------------------------------
        self.setLayout(QtGui.QVBoxLayout())
        self.central_layout.setContentsMargins(0, 0, 0, 0)
        self.central_layout.setSpacing(1)

        # Main widgets ---------------------------------------------------------
        # Widgets
        self.create_widget_button = QtGui.QPushButton("Create PrimVar "
                                                      "Attributes")
        self.manage_widget_button = QtGui.QPushButton("Manage PrimVars")
        label_type = QtGui.QLabel("PrimVar Type:")
        self.primvar_types = QtGui.QComboBox()
        self.primvar_types.setMinimumWidth(150)
        self.primvar_types.setMinimumHeight(30)
        self.primvar_types.addItems(list(reversed(core.EXISTING_ATTR.keys())))
        self.primvar_types.setToolTip("""rmanF - constant or vertex floats\n
rmanP - constant or vertex points\n
rmanV - constant or vertex vectors\n
rmanN - constant or vertex normals\n
rmanC - constant or vertex colors\n
rmanS - constant string\n
rmanM - vertex mpoint (for blobs)\n
Visit: https://renderman.pixar.com/view/how-to-primitive-variables""")
        self.new_attribute = QtGui.QPushButton("New")
        self.assign_attributes = QtGui.QPushButton("Assign")
        self.assign_attributes.setObjectName("assign")
        self.assign_attributes.setMinimumHeight(40)
        # Layouts
        layout1 = QtGui.QHBoxLayout()
        layout2 = QtGui.QHBoxLayout()
        layout3 = QtGui.QHBoxLayout()
        for layout in [layout1, layout2, layout3]:
            layout.setContentsMargins(2, 2, 2, 2)
            layout.setSpacing(1)

        layout1.setAlignment(QtCore.Qt.AlignCenter)
        layout1.addWidget(self.create_widget_button)
        layout1.addSpacerItem(QtGui.QSpacerItem(2, 2,
                                                QtGui.QSizePolicy.Expanding))
        layout1.addWidget(self.manage_widget_button)
        layout2.addWidget(label_type)
        layout2.addWidget(self.primvar_types)
        layout2.addSpacerItem(QtGui.QSpacerItem(2, 2,
                                                QtGui.QSizePolicy.Expanding))
        layout2.addWidget(self.new_attribute)
        layout3.addWidget(self.assign_attributes)

        # Adding scroll area ---------------------------------------------------
        scroll_area = QtGui.QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFocusPolicy(QtCore.Qt.NoFocus)
        scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        # Main Widget ----------------------------------------------------------
        main_widget = QtGui.QWidget()
        self.main_layout = QtGui.QVBoxLayout()
        self.main_layout.setContentsMargins(2, 2, 2, 2)
        self.main_layout.setSpacing(1)
        self.main_layout.setAlignment(QtCore.Qt.AlignTop)
        main_widget.setLayout(self.main_layout)
        scroll_area.setWidget(main_widget)

        # Main layout assignment -----------------------------------------------
        self.central_layout.addLayout(layout1)
        self.central_layout.addLayout(layout2)
        self.central_layout.addWidget(scroll_area)
        self.central_layout.addLayout(layout3)

    def setup_signals(self):
        """
        """
        self.new_attribute.clicked.connect(self.create_new_attr)
        self.assign_attributes.clicked.connect(self.assign_new_attr)

    def assign_new_attr(self):
        """

        :return:
        """
        shapes = list(core.get_shapes(core.unpack(pm.ls(sl=True))))
        if not shapes:
            error_message = "\n" + ("*" * 80) + "\n\t\t\tNo Object is " \
                                                "selected.\n\n" + ("*" * 80) \
                            + "\n"
            logging.error(error_message)
            return
        for att in NEW_ATTRS:
            if att.attr_type == "rmanF":
                attribute_name = "rmanF" + att.attr_name.text()
                self.assign_f(shapes,
                              attribute_name,
                              att.type_float.isChecked(),
                              att.min_value.value(),
                              att.max_value.value())
                if att.primvar_node_name.text():
                    self.setup_primvar_node(att.primvar_node_name.text(),
                                            attribute_name,
                                            "float")

            if att.attr_type == "rmanS":
                attribute_name = "rmanS" + att.attr_name.text()
                self.assign_s(shapes, attribute_name, att.new_strings)

            if att.attr_name == "rmanC":
                pass
        # Close the UI at the end
        close_ui()

    @staticmethod
    def assign_f(shape_nodes, attr_name, is_float, min_value, max_value):
        """

        :param shape_nodes:
        :param attr_name:
        :param is_float:
        :param min_value:
        :param max_value:
        :return:
        """
        # create float attribute
        for shape_node in shape_nodes:
            core.add_attr(shape_node, attr_name, attributeType='double')
            if is_float:
                core.set_attr(shape_node, attr_name, random.uniform(
                    min_value, max_value))
            else:
                core.set_attr(shape_node, attr_name, random.randint(
                    min_value, max_value))

    @staticmethod
    def setup_primvar_node(node_name, attr_name, attr_type):
        """

        :param node_name:
        :param attr_name:
        :param attr_type:
        :return:
        """
        try:
            core.set_attr(pm.PyNode(node_name), "varname", attr_name)
            core.set_attr(pm.PyNode(node_name), "type", attr_type)
        except Exception as e:
            logging.warning(str(e))

    @staticmethod
    def assign_s(shape_nodes, attr_name, string_list):
        """

        :param shape_nodes:
        :param attr_name:
        :param string_list:
        :return:
        """
        string_values = [str(value) for value in string_list[0]]
        for shape in shape_nodes:
            core.add_attr(shape, attr_name, dataType="string")
            core.set_attr(shape, attr_name, str(random.choice(string_values)))

    @staticmethod
    def go_to_wiki():
        """
        Opens the browser link and direct it to the help page for this tool
        """
        link_page = "https://renderman.pixar.com/view/how-to-primitive" \
                    "-variables "
        pm.launch(web=link_page)

    @staticmethod
    def delete_widget(widget):
        """
        """
        NEW_ATTRS.remove(widget)
        widget.deleteLater()

    def setup_stylesheet(self):
        """
        """
        try:
            style_sheet = open(os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                'gui/styleSheets/styleSheet.css')).read()
            self.setStyleSheet(style_sheet)
        except IOError as e:
            error_message = "\n" + ("*" * 80) + "\n" + str(e) + \
                            "\n\t\t\tCan't find the CSS file for style " \
                            "sheet.\n\n" + ("*" * 80) + "\n"
            logging.warning(error_message)

    def create_new_attr(self):
        """
        """
        if self.primvar_types.currentText() == "rmanF":
            new_primvar_widget = FprimVarWidgets()
        if self.primvar_types.currentText() == "rmanC":
            new_primvar_widget = CprimVarWidgets()
        if self.primvar_types.currentText() == "rmanP":
            new_primvar_widget = NVPMprimVarWidgets(attr_type="rmanP")
        if self.primvar_types.currentText() == "rmanV":
            new_primvar_widget = NVPMprimVarWidgets(attr_type="rmanV")
        if self.primvar_types.currentText() == "rmanN":
            new_primvar_widget = NVPMprimVarWidgets(attr_type="rmanN")
        if self.primvar_types.currentText() == "rmanS":
            new_primvar_widget = SprimVarWidgets()
        self.main_layout.addWidget(new_primvar_widget)
        new_primvar_widget.delete_this.clicked.connect(partial(
            self.delete_widget, new_primvar_widget))
        NEW_ATTRS.append(new_primvar_widget)


def create_ui():
    """
    Create an instance of the GUI
    :return: QWidget
    """
    global primVarUi
    if not primVarUi:
        primVarUi = PrimVarUi()
        # primVarUi = PrmanFPrimVarWidget()

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
    Simply run help if called directly.
    """
    # import __main__
    # help(__main__)
    global primVarUi

    app = QtGui.QApplication(sys.argv)
    primVarUi = PrimVarUi()
    primVarUi.show()
    primVarUi.raise_()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
