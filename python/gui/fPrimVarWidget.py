#! /usr/bin/env python
# This free software incorporates by reference the text of the WTFPL, Version 2

"""
Primitive Variable F Widget.

.. module:: `FprimVarWidgets`
   :platform: Unix, Windows,
   :synopsis: This is the widget for Primitive Variable F.

.. moduleauthor:: Ali Jafargholi <ali.jafargholi@gmail.com>
"""

# IMPORT LOCAL MODULES
import PySide.QtCore as QtCore
import PySide.QtGui as QtGui


class FprimVarWidgets(QtGui.QFrame):
    def __init__(self, *args, **kwargs):
        super(FprimVarWidgets, self).__init__(*args, **kwargs)

        self._attr_type = "rmanF"

        self.init_ui()

    @property
    def attr_type(self):
        """ Returns the attribute type.

        :return: (string) attribute type. example: rmanf
        """
        return self._attr_type

    def init_ui(self):
        """
        """
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
        attr_type_label = QtGui.QLabel("Value Type:")
        self.type_int = QtGui.QRadioButton("Integer")
        self.type_float = QtGui.QRadioButton("Float")
        self.type_float.setChecked(True)
        min_value_label = QtGui.QLabel("Min:")
        self.min_value = QtGui.QDoubleSpinBox()
        self.min_value.setSingleStep(0.1)
        self.min_value.setValue(0)
        max_value_label = QtGui.QLabel("Max:")
        self.max_value = QtGui.QDoubleSpinBox()
        self.max_value.setSingleStep(0.1)
        self.max_value.setValue(1)
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
        layout3 = QtGui.QGridLayout()
        layout4 = QtGui.QHBoxLayout()
        for layout in [main_layout, layout1, layout2, layout3, layout4]:
            layout.setContentsMargins(1, 1, 1, 1)
            layout.setSpacing(5)
            layout.setAlignment(QtCore.Qt.AlignTop)

        for layout in [layout1, layout2, layout3, layout4]:
            main_layout.addLayout(layout)

        self.setLayout(main_layout)

        # Assign widgets to layout ---------------------------------------------
        layout1.addWidget(widget_label)
        layout1.addSpacerItem(QtGui.QSpacerItem(2, 2,
                                                QtGui.QSizePolicy.Expanding))
        layout1.addWidget(self.delete_this)
        layout2.addWidget(attr_name_label)
        layout2.addWidget(self.attr_name)

        layout3.addWidget(attr_type_label, 0, 0)
        layout3.addWidget(self.type_float, 0, 1)
        layout3.addWidget(self.type_int, 0, 2)

        layout3.addWidget(min_value_label, 1, 1)
        layout3.addWidget(self.min_value, 1, 2)
        layout3.addWidget(max_value_label, 1, 3)
        layout3.addWidget(self.max_value, 1, 4)

        layout4.addWidget(primvar_node_label)
        layout4.addWidget(self.primvar_node_name)
        layout4.addWidget(self.get_node_name)
        layout4.addWidget(self.create_node)
