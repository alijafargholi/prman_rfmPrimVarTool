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
        self.setFixedWidth(400)
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
        self.new_attribute.clicked.connect(self.create_rmanf)

    def create_rmanf(self):
        """
        """
        new_rmanf_widget = RmanFPrimVarWidget()
        self.main_layout.addWidget(new_rmanf_widget)

    @staticmethod
    def go_to_wiki():
        """
        Opens the browser link and direct it to the help page for this tool
        """
        link_page = "https://renderman.pixar.com/view/how-to-primitive" \
                    "-variables "
        pm.launch(web=link_page)


class RmanFPrimVarWidget(QtGui.QFrame):
    def __init__(self, *args, **kwargs):
        super(RmanFPrimVarWidget, self).__init__(*args, **kwargs)

        # Widgets --------------------------------------------------------------
        widget_label = QtGui.QLabel("rmanF primVar")
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
        self.delete_this = QtGui.QPushButton("Delete This")

        # Layouts --------------------------------------------------------------
        main_layout = QtGui.QVBoxLayout()
        layout1 = QtGui.QHBoxLayout()
        layout2 = QtGui.QHBoxLayout()
        layout3 = QtGui.QHBoxLayout()
        layout4 = QtGui.QHBoxLayout()
        layout5 = QtGui.QHBoxLayout()
        layout6 = QtGui.QHBoxLayout()
        for layout in [main_layout, layout1, layout2, layout3, layout4,
                       layout5, layout6]:
            layout.setContentsMargins(2, 2, 2, 2)
            layout.setSpacing(1)
            layout.setAlignment(QtCore.Qt.AlignTop)
            layout.setAlignment(QtCore.Qt.AlignLeft)

        layout6.setAlignment(QtCore.Qt.AlignRight)

        for layout in [layout1, layout2, layout3, layout4, layout5, layout6]:
            main_layout.addLayout(layout)

        self.setLayout(main_layout)

        # Assign widgets to layout ---------------------------------------------
        layout1.addWidget(widget_label)
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
        layout6.addWidget(self.delete_this)

        # Ui Setup -------------------------------------------------------------
        self.setup_signals()

    def setup_signals(self):
        """
        """
        self.delete_this.clicked.connect(self.close)


def create_ui():
    """
    Create an instance of the GUI
    :return: QWidget
    """
    global primVarUi
    if not primVarUi:
        primVarUi = PrimVarUi()
        # primVarUi = RmanFPrimVarWidget()

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
