#! /usr/bin/env python
# This free software incorporates by reference the text of the WTFPL, Version 2

"""
Primitive Variable Normal Widget.

.. module:: `SprimVarWidgets`
   :platform: Unix, Windows,
   :synopsis: This is the widget for Primitive Variable N.

.. moduleauthor:: Ali Jafargholi <ali.jafargholi@gmail.com>
"""

# IMPORT LOCAL MODULES
import PySide.QtCore as QtCore
import PySide.QtGui as QtGui


class SprimVarWidgets(QtGui.QFrame):
    def __init__(self, *args, **kwargs):
        super(SprimVarWidgets, self).__init__(*args, **kwargs)

        self._attr_type = "rmanS"
        self._new_strings = ''

        self.setup_ui()
        self.setup_signals()

    @property
    def attr_type(self):
        """ Returns the attribute type.

        :return: (string) attribute type. example: rmanS
        """
        return self._attr_type

    @property
    def new_strings(self):
        """

        :return:
        """
        return self._new_strings

    @new_strings.setter
    def new_strings(self, value):
        """

        :param value:
        :return:
        """
        self._new_strings = value

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

        # Layouts --------------------------------------------------------------
        main_layout = QtGui.QVBoxLayout()
        layout1 = QtGui.QHBoxLayout()
        layout2 = QtGui.QHBoxLayout()
        layout3 = QtGui.QHBoxLayout()
        for layout in [main_layout, layout1, layout2, layout3]:
            layout.setContentsMargins(1, 1, 1, 1)
            layout.setSpacing(5)
            layout.setAlignment(QtCore.Qt.AlignTop)
            layout.setAlignment(QtCore.Qt.AlignLeft)

        layout3.setAlignment(QtCore.Qt.AlignRight)

        for layout in [layout1, layout2, layout3]:
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

    def setup_signals(self):
        """
        """
        self.gather_file.clicked.connect(self.get_files)

    def get_files(self):
        """

        :return:
        """
        self.new_strings = QtGui.QFileDialog.getOpenFileNames()
