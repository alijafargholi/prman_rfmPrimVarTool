#! /usr/bin/env python
# This free software incorporates by reference the text of the WTFPL, Version 2

"""
Primitive Variable F Widget.

.. module:: `FprimVarWidgets`
   :platform: Unix, Windows,
   :synopsis: This is the widget for Primitive Variable F.

.. moduleauthor:: Ali Jafargholi <ali.jafargholi@gmail.com>
"""

# IMPORT STANDARD MODULES
import sys

# IMPORT LOCAL MODULES
import PyQt4.QtCore as QtCore
import PyQt4.QtGui as QtGui
from images import images_rc

# GLOBAL VARIABLE
fPrimVarWidgetUi = None


class FprimVarWidgets(QtGui.QFrame):
    def __init__(self, *args, **kwargs):
        super(FprimVarWidgets, self).__init__(*args, **kwargs)
        self.init_ui()
        self.setup_signals()

    def init_ui(self):
        """
        """
        self.widget_height = 150
        self.setFixedHeight(self.widget_height)
        self.setFrameStyle(QtGui.QFrame.Panel | QtGui.QFrame.Raised)

        # Widgets --------------------------------------------------------------
        widget_label = QtGui.QLabel("rmanF primVar")
        widget_label.setObjectName("widgetTitle")
        self.delete_this = QtGui.QPushButton()
        self.delete_this.setFixedHeight(25)
        self.delete_this.setFixedWidth(25)
        self.delete_this.setObjectName("close")
        attr_name_label = QtGui.QLabel("Attribute Name:")
        self.attr_name = QtGui.QLineEdit()
        attr_type_label = QtGui.QLabel("Value Type")
        self.type_int = QtGui.QRadioButton("Integer")
        self.type_float = QtGui.QRadioButton("Float")
        min_value_label = QtGui.QLabel("Min:")
        self.min_value = QtGui.QLineEdit()
        max_value_label = QtGui.QLabel("Max:")
        self.max_value = QtGui.QLineEdit()
        primvar_node_label = QtGui.QLabel("PrimVar Node Name:")
        self.primvar_node_name = QtGui.QLineEdit()
        self.primvar_node_name.setMinimumWidth(120)
        self.get_node_name = QtGui.QPushButton("Get It")
        self.get_node_name.setMinimumHeight(35)
        self.get_node_name.setMaximumWidth(50)
        self.get_node_name.setToolTip(
            "Select the PrimVar node and click this "
            "to get the name")
        self.create_node = QtGui.QPushButton("Create PrimVar Node")
        self.create_node.setMinimumHeight(35)
        self.create_node.setToolTip("Create a new PrimVar node")

        # Layouts --------------------------------------------------------------
        main_layout = QtGui.QVBoxLayout()
        layout1 = QtGui.QHBoxLayout()
        layout2 = QtGui.QHBoxLayout()
        layout3 = QtGui.QHBoxLayout()
        layout4 = QtGui.QHBoxLayout()
        layout5 = QtGui.QHBoxLayout()
        for layout in [main_layout, layout1, layout2, layout3, layout4,
                       layout5]:
            layout.setContentsMargins(1, 1, 1, 1)
            layout.setSpacing(2)
            layout.setAlignment(QtCore.Qt.AlignTop)

        for layout in [layout1, layout2, layout3, layout4, layout5]:
            main_layout.addLayout(layout)

        self.setLayout(main_layout)

        # Assign widgets to layout ---------------------------------------------
        layout1.addWidget(widget_label)
        layout1.addSpacerItem(QtGui.QSpacerItem(2, 2,
                                                QtGui.QSizePolicy.Expanding))
        layout1.addWidget(self.delete_this)
        layout2.addWidget(attr_name_label)
        layout2.addWidget(self.attr_name)
        layout3.addWidget(attr_type_label)
        layout3.addWidget(self.type_float)
        layout3.addWidget(self.type_int)
        layout4.addWidget(min_value_label)
        layout4.addWidget(self.min_value)
        layout4.addWidget(max_value_label)
        layout4.addWidget(self.max_value)
        layout4.addSpacerItem(QtGui.QSpacerItem(2, 2,
                                                QtGui.QSizePolicy.Expanding))
        layout5.addWidget(primvar_node_label)
        layout5.addWidget(self.primvar_node_name)
        layout5.addWidget(self.get_node_name)
        layout5.addWidget(self.create_node)

    def setup_signals(self):
        """
        """
        self.delete_this.clicked.connect(self.delete_widget)

    def delete_widget(self):
        """
        """
        self.deleteLater()


def create_ui():
    """
    Create an instance of the GUI
    :return: QWidget
    """
    global fPrimVarWidgetUi
    if fPrimVarWidgetUi:
        fPrimVarWidgetUi = FprimVarWidgets()
    fPrimVarWidgetUi.show()


def close_ui():
    """
    Close the existing Ui
    :return: None
    """
    global fPrimVarWidgetUi
    if fPrimVarWidgetUi:
        fPrimVarWidgetUi.deleteLater()
        fPrimVarWidgetUi = None


def main():
    """
    If the application is ran in terminal, create a stand alone app and raise
    the window
    :return: QWidget
    """
    global fPrimVarWidgetUi

    app = QtGui.QApplication(sys.argv)
    fPrimVarWidgetUi = FprimVarWidgets()
    fPrimVarWidgetUi.show()
    fPrimVarWidgetUi.raise_()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
