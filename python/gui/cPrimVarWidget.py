#! /usr/bin/env python
# This free software incorporates by reference the text of the WTFPL, Version 2

"""
Primitive Variable C Widget.

.. module:: `CprimVarWidgets`
   :platform: Unix, Windows,
   :synopsis: This is the widget for Primitive Variable C.

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


class CprimVarWidgets(QtGui.QFrame):
    def __init__(self, *args, **kwargs):
        super(CprimVarWidgets, self).__init__(*args, **kwargs)
        self.setup_ui()
        self.setup_signals()

    def setup_ui(self):
        self.widget_height = 210
        self.setFixedHeight(self.widget_height)
        self.setFrameStyle(QtGui.QFrame.Panel | QtGui.QFrame.Raised)

        # Widgets --------------------------------------------------------------
        widget_label = QtGui.QLabel("rmanC primVar")
        widget_label.setObjectName("widgetTitle")
        self.delete_this = QtGui.QPushButton()
        self.delete_this.setFixedHeight(25)
        self.delete_this.setFixedWidth(25)
        self.delete_this.setObjectName("close")
        attr_name_label = QtGui.QLabel("Attribute Name:")
        self.attr_name = QtGui.QLineEdit()
        color_type_label = QtGui.QLabel("Color Type")
        self.random_color = QtGui.QRadioButton("Random Color")
        self.random_color.setChecked(True)
        self.random_color_shades = QtGui.QRadioButton("Random Color Shades")
        self.color_picker = QtGui.QPushButton()
        self.color_picker.setStyleSheet("background-color: black")
        self.random_grayscale = QtGui.QRadioButton("Random Grayscale")

        min_s_value_label = QtGui.QLabel("Min Saturation:")
        self.min_s_value = QtGui.QDoubleSpinBox()
        max_s_value_label = QtGui.QLabel("Max Saturation:")
        self.max_s_value = QtGui.QDoubleSpinBox()
        self.max_s_value.setValue(1)
        min_v_value_label = QtGui.QLabel("Min Brightness:")
        self.min_v_value = QtGui.QDoubleSpinBox()
        max_v_value_label = QtGui.QLabel("Max Brightness:")
        self.max_v_value = QtGui.QDoubleSpinBox()
        self.max_v_value.setValue(1)
        primvar_node_label = QtGui.QLabel("PrimVar Node Name:")
        self.primvar_node_name = QtGui.QLineEdit()
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
        layout3 = QtGui.QGridLayout()
        layout4 = QtGui.QHBoxLayout()
        for layout in [main_layout, layout1, layout2, layout3, layout4]:
            layout.setContentsMargins(1, 1, 1, 1)
            layout.setSpacing(5)
            layout.setAlignment(QtCore.Qt.AlignTop)
            layout.setAlignment(QtCore.Qt.AlignLeft)

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
        layout3.addWidget(color_type_label, 0, 0)
        layout3.addWidget(self.random_color, 0, 1)
        layout3.addWidget(self.random_color_shades, 1, 1)
        layout3.addWidget(self.color_picker, 1, 2)
        layout3.addWidget(self.random_grayscale, 2, 1)
        layout3.addWidget(min_s_value_label, 3, 1)
        layout3.addWidget(self.min_s_value, 3, 2)
        layout3.addWidget(max_s_value_label, 3, 3)
        layout3.addWidget(self.max_s_value, 3, 4)
        layout3.addWidget(min_v_value_label, 4, 1)
        layout3.addWidget(self.min_v_value, 4, 2)
        layout3.addWidget(max_v_value_label, 4, 3)
        layout3.addWidget(self.max_v_value, 4, 4)
        layout4.addWidget(primvar_node_label)
        layout4.addWidget(self.primvar_node_name)
        layout4.addWidget(self.get_node_name)
        layout4.addWidget(self.create_node)

    def setup_signals(self):
        """
        """
        self.delete_this.clicked.connect(self.delete_widget)
        self.color_picker.clicked.connect(self.pick_color)

    def pick_color(self):
        """
        """
        new_color = QtGui.QColorDialog.getColor()
        self.color_picker.setStyleSheet("background-color: {}".format(
            new_color.name()))
        # rgb_str = new_color.name().split("#")[-1]
        # hsl_color = struct.unpack('BBB', rgb_str.decode('hex'))
        # print hsl_color
        # print colorsys.hls_to_rgb(hsl_color[0], hsl_color[1], hsl_color[2])

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
        fPrimVarWidgetUi = CprimVarWidgets()
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
    fPrimVarWidgetUi = CprimVarWidgets()
    fPrimVarWidgetUi.show()
    fPrimVarWidgetUi.raise_()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
