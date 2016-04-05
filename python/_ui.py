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
import logging
import struct
import colorsys
import colorama

# IMPORT LOCAL MODULES
import PySide.QtCore as QtCore
import PySide.QtGui as QtGui
import _core
try:
    import pymel.core as pm
except ImportError as e:
    logging.error("\n\n\nThis tool was not able to import the 'pymel' "
                  "library.\nThat is required for this tool to "
                  "function.\nPlease contact the developer for assistant.\n "
                  "Contact info: ali.jafargholi@gmail.com\n\n" + (100 * "*") +
                  "\n" + str(e) + "\n" + (100 * "*") + "\n")

# GLOBAL VARIABLE
primVarUi = None

__version__ = "0.1.0"


class PrimVarUi(QtGui.QMainWindow):
    """

    """
    def __init__(self, *args, **kwargs):
        super(PrimVarUi, self).__init__(*args, **kwargs)

        # Window Settings
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowTitle("Primitive Variables(primVar) Manager - v{"
                            "}".format(__version__))
        self.setObjectName("primVarManager")
        self.setFixedWidth(430)
        self.setMinimumHeight(500)
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
        self.central_layout.setSpacing(0)

        # Main widgets ---------------------------------------------------------
        # Widgets
        self.create_widget_button = QtGui.QPushButton("Create PrimVar "
                                                      "Attributes")
        self.manage_widget_button = QtGui.QPushButton("Manage PrimVars")
        label_type = QtGui.QLabel("PrimVar Type:")
        self.primvar_types = QtGui.QComboBox()
        self.primvar_types.addItems(_core.EXISTING_ATTR.keys())
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
        layout1.addWidget(self.manage_widget_button)
        layout2.addWidget(label_type)
        layout2.addWidget(self.primvar_types)
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

        # Ui Setup -------------------------------------------------------------
        self.setup_signals()

    def setup_signals(self):
        """
        """
        self.new_attribute.clicked.connect(self.create_new_attr)

    def create_new_attr(self):
        """
        """
        if self.primvar_types.currentText() == "rmanF":
            new_rmanf_widget = PrmanFPrimVarWidget()
        if self.primvar_types.currentText() == "rmanC":
            new_rmanf_widget = PrmanCPrimVarWidget()
        if self.primvar_types.currentText() == "rmanP":
            new_rmanf_widget = PrmanCPrimVarWidget()
        if self.primvar_types.currentText() == "rmanV":
            new_rmanf_widget = PrmanCPrimVarWidget()
        if self.primvar_types.currentText() == "rmanN":
            new_rmanf_widget = PrmanCPrimVarWidget()
        if self.primvar_types.currentText() == "rmanS":
            new_rmanf_widget = PrmanCPrimVarWidget()
        self.main_layout.addWidget(new_rmanf_widget)

    @staticmethod
    def go_to_wiki():
        """
        Opens the browser link and direct it to the help page for this tool
        """
        link_page = "https://renderman.pixar.com/view/how-to-primitive" \
                    "-variables "
        pm.launch(web=link_page)


class PrmanCPrimVarWidget(QtGui.QFrame):
    def __init__(self, *args, **kwargs):
        super(PrmanCPrimVarWidget, self).__init__(*args, **kwargs)
        self.widget_height = 200
        self.setFixedHeight(self.widget_height)
        self.setFrameStyle(QtGui.QFrame.Panel | QtGui.QFrame.Raised)

        # Widgets --------------------------------------------------------------
        widget_label = QtGui.QLabel("rmanC primVar")
        self.delete_this = QtGui.QPushButton("X")
        attr_name_label = QtGui.QLabel("Attribute Name:")
        self.attr_name = QtGui.QLineEdit()
        color_type_label = QtGui.QLabel("Color Type")
        self.random_color = QtGui.QRadioButton("Random Color")
        self.random_color_shades = QtGui.QRadioButton("Random Color Shades")
        self.color_picker = QtGui.QPushButton()
        self.color_picker.setStyleSheet("background-color: black")
        self.random_grayscale = QtGui.QRadioButton("Random Grayscale")

        min_s_value_label = QtGui.QLabel("Min Saturation:")
        self.min_s_value = QtGui.QSpinBox()
        max_s_value_label = QtGui.QLabel("Max Saturation:")
        self.max_s_value = QtGui.QSpinBox()
        self.max_s_value.setValue(1)
        min_v_value_label = QtGui.QLabel("Min Brightness:")
        self.min_v_value = QtGui.QSpinBox()
        max_v_value_label = QtGui.QLabel("Max Brightness:")
        self.max_v_value = QtGui.QSpinBox()
        self.max_v_value.setValue(1)
        primvar_node_label = QtGui.QLabel("PrimVar Node Name:")
        self.primvar_node_name = QtGui.QLineEdit()
        self.get_node_name = QtGui.QPushButton("Get It")
        self.get_node_name.setToolTip("Select the PrimVar node and click this "
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
            layout.setContentsMargins(2, 2, 2, 2)
            layout.setSpacing(1)
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

        # Ui Setup -------------------------------------------------------------
        self.setup_signals()

    def setup_signals(self):
        """
        """
        self.delete_this.clicked.connect(self.delete_widget)
        self.color_picker.clicked.connect(self.pick_color)

    def delete_widget(self):
        """
        """
        self.deleteLater()

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


class PrmanFPrimVarWidget(QtGui.QFrame):
    def __init__(self, *args, **kwargs):
        super(PrmanFPrimVarWidget, self).__init__(*args, **kwargs)
        self.widget_height = 130
        self.setFixedHeight(self.widget_height)
        self.setFrameStyle(QtGui.QFrame.Panel | QtGui.QFrame.Raised)

        # Widgets --------------------------------------------------------------
        widget_label = QtGui.QLabel("rmanF primVar")
        self.delete_this = QtGui.QPushButton("X")
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
        self.get_node_name = QtGui.QPushButton("Get It")
        self.get_node_name.setToolTip("Select the PrimVar node and click this "
                                      "to get the name")
        self.create_node = QtGui.QPushButton("Create PrimVar Node")
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
            layout.setContentsMargins(2, 2, 2, 2)
            layout.setSpacing(1)
            layout.setAlignment(QtCore.Qt.AlignTop)
            layout.setAlignment(QtCore.Qt.AlignLeft)

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
        layout5.addWidget(primvar_node_label)
        layout5.addWidget(self.primvar_node_name)
        layout5.addWidget(self.get_node_name)
        layout5.addWidget(self.create_node)

        # Ui Setup -------------------------------------------------------------
        self.setup_signals()

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
    import __main__
    help(__main__)


if __name__ == '__main__':
    main()
