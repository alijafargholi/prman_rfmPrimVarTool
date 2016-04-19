#! /usr/bin/env python
# This free software incorporates by reference the text of the WTFPL, Version 2

"""
Primitive Variable Normal Widget.

.. module:: `SprimVarWidgets`
   :platform: Unix, Windows,
   :synopsis: This is the widget for Primitive Variable N.

.. moduleauthor:: Ali Jafargholi <ali.jafargholi@gmail.com>
"""

# IMPORT STANDARD MODULES
import sys
import os

# IMPORT LOCAL MODULES
import PyQt4.QtCore as QtCore
import PyQt4.QtGui as QtGui
from images import images_rc

# GLOBAL VARIABLE
SELECTED_FILES = []

class SprimVarWidgets(QtGui.QFrame):
    def __init__(self, *args, **kwargs):
        super(SprimVarWidgets, self).__init__(*args, **kwargs)
        self.attr_type = "rmanS"
        self.setup_ui()
        self.setup_signals()

    def setup_ui(self):
        self.setFrameStyle(QtGui.QFrame.Panel | QtGui.QFrame.Raised)

        # Widgets --------------------------------------------------------------
        widget_label = QtGui.QLabel("rmanS primVar")
        widget_label.setObjectName("widgetTitle")
        self.delete_this = QtGui.QPushButton()
        self.delete_this.setFixedHeight(25)
        self.delete_this.setFixedWidth(25)
        self.delete_this.setObjectName("close")
        attr_name_label = QtGui.QLabel("Attribute Name:")
        self.attr_name = QtGui.QLineEdit()

        self.gather_file = QtGui.QPushButton("Gather Files")
        self.create_string = QtGui.QPushButton("Add Custom String")

        primvar_node_label = QtGui.QLabel("PrimVar Node Name:")
        self.primvar_node_name = QtGui.QLineEdit()
        self.get_node_name = QtGui.QPushButton("Get It")
        self.get_node_name.setToolTip(
            "Select the PrimVar node and click this "
            "to get the name")
        self.create_node = QtGui.QPushButton("Create PrimVar Node")
        self.create_node.setToolTip("Create a new PrimVar node")

        # Layouts --------------------------------------------------------------
        main_layout = QtGui.QVBoxLayout()
        layout1 = QtGui.QHBoxLayout()
        layout2 = QtGui.QHBoxLayout()
        layout3 = QtGui.QHBoxLayout()
        self.layout4 = QtGui.QVBoxLayout()
        self.layout5 = QtGui.QVBoxLayout()
        layout6 = QtGui.QHBoxLayout()
        for layout in [main_layout, layout1, layout2, layout3, self.layout4,
                       self.layout5, layout6]:
            layout.setContentsMargins(1, 1, 1, 1)
            layout.setSpacing(5)
            layout.setAlignment(QtCore.Qt.AlignTop)
            layout.setAlignment(QtCore.Qt.AlignLeft)

        layout3.setAlignment(QtCore.Qt.AlignRight)
        self.layout4.setAlignment(QtCore.Qt.AlignRight)
        self.layout5.setAlignment(QtCore.Qt.AlignRight)

        for layout in [layout1, layout2, layout3, self.layout4,
                       self.layout5, layout6]:
            main_layout.addLayout(layout)

        self.setLayout(main_layout)

        # Assign widgets to layout ---------------------------------------------
        layout1.addWidget(widget_label)
        layout1.addSpacerItem(QtGui.QSpacerItem(2, 2,
                                                QtGui.QSizePolicy.Expanding))
        layout1.addWidget(self.delete_this)
        layout2.addWidget(attr_name_label)
        layout2.addWidget(self.attr_name)
        layout3.addWidget(self.gather_file)
        layout3.addWidget(self.create_string)
        layout6.addWidget(primvar_node_label)
        layout6.addWidget(self.primvar_node_name)
        layout6.addWidget(self.get_node_name)
        layout6.addWidget(self.create_node)

    def setup_signals(self):
        """
        """
        self.delete_this.clicked.connect(self.delete_widget)
        self.create_string.clicked.connect(self.create_custom_string)
        self.gather_file.clicked.connect(self.get_files)

    def get_files(self):
        """

        :return:
        """
        files = QtGui.QFileDialog.getOpenFileNames(self, "Select Files")
        SELECTED_FILES.append([f for f in files])

    def create_custom_string(self):
        """
        """
        self.layout4.addWidget(QtGui.QLineEdit())

    def delete_widget(self):
        """
        """
        self.deleteLater()
