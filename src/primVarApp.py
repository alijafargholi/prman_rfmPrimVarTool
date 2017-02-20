# IMPORT STANDARD MODULES
import sys
import os
import random
import colorsys
import logging
from functools import partial
import webbrowser

# IMPORT LOCAL MODULES
from gui.Qt import QtWidgets as QtGui
from gui.Qt.QtGui import QRegExpValidator

from gui.Qt import QtCore

from utils import core
from gui.mainWindow import Ui_primvarManager
from gui.rmanCwidget import Ui_Form as cWidget
from gui.rmanFwidget import Ui_Form as fWidget
from gui.rmanNwidget import Ui_Form as nWidget
from gui.rmanSwidget import Ui_Form as sWidget
from gui.rmanPwidget import Ui_Form as pWidget
from gui.rmanVwidget import Ui_Form as vWidget
# from gui.images import images_rc

try:
    import pymel.core as pm
except ImportError as e:
    logging.error("\n\n\nThis tool was not able to import the 'pymel' "
                  "library.\nThat is required for this tool to "
                  "function.\nPlease contact the developer for assistant.\n "
                  "Contact info: ali.jafargholi@gmail.com\n\n" + (80 * "*") +
                  "\n" + str(e) + "\n" + (80 * "*") + "\n")

# GLOBAL VARIABLE
primVarAppUi = None
__version__ = "0.2.0"


class PrimVarApp(QtGui.QMainWindow, Ui_primvarManager):
    """
    Main logic for connecting the UI and core functionality
    """

    def __init__(self, *args, **kwargs):
        super(PrimVarApp, self).__init__(*args, **kwargs)

        # Creating a list to store the new widgets and corresponding
        self.created_attributes = []

        self.setupUi(self)
        self.init_ui()
        self.setup_signals()
        self.setup_stylesheet()

    def init_ui(self):
        """
        Setting up some of the UI look and feel
        """

        self.setWindowTitle("PrimVar Manager - {}".format(__version__))

        layouts_list = [self.rmanCLayout, self.rmanFLayout,
                        self.rmanSLayout, self.rmanVLayout, self.rmanPLayout,
                        self.rmanNLayout]

        for layout in layouts_list:
            layout.setAlignment(QtCore.Qt.AlignTop)
            layout.setSpacing(0)
            layout.setContentsMargins(0, 0, 0, 0)

    def setup_signals(self):
        """
        Connecting the UI signals to the functions
        """

        self.action_close_ui.triggered.connect(close_ui)
        self.action_clear.triggered.connect(self.clear)
        self.action_pxar_Documenation.triggered.connect(self.go_to_wiki)
        self.action_tool_Documentation.triggered.connect(self.go_to_doc)
        self.assign.clicked.connect(self.assign_attributes)
        self.createRmanC.clicked.connect(self.create_rman_c)
        self.createRmanF.clicked.connect(self.create_rman_f)
        self.createRmanS.clicked.connect(self.create_rman_s)
        self.createRmanV.clicked.connect(self.create_rman_v)
        self.createRmanP.clicked.connect(self.create_rman_p)
        self.createRmanN.clicked.connect(self.create_rman_n)

    def assign_attributes(self):
        """
        Gathering the selected object(s)'s shape and assigning the PrimVar
        attributes to them
        """

        # Getting the shape nodes of selected objects
        shapes = list(core.get_shapes(core.unpack(pm.ls(sl=True))))

        # If nothing is selected, warn the user and abort the assign process
        if not shapes:
            warning_message = "\n" + ("*" * 80) + "\n\t\t\tNo Object is " \
                                                  "selected.\n\n" + ("*" * 80) \
                              + "\n"
            logging.warning(warning_message)
            self.warning("No object is selected.")
            return

        # Go through all the attributes and assign them to the shapes
        for new_attr in self.created_attributes:
            if type(new_attr) == PrimVarCWidget:
                self.primvar_c(shapes, new_attr)
            if type(new_attr) == PrimVarSWidget:
                self.primvar_s(shapes, new_attr)
            if type(new_attr) == PrimVarFWidget:
                self.primvar_f(shapes, new_attr)
            if type(new_attr) == PrimVarVWidget:
                self.primvar_v(shapes, new_attr)
            if type(new_attr) == PrimVarPWidget:
                self.primvar_p(shapes, new_attr)
            if type(new_attr) == PrimVarNWidget:
                self.primvar_n(shapes, new_attr)

        # If all not attributes are assigned, abort the window closing
        if not self.created_attributes:
            # Finally close the UI
            close_ui()

        # TODO: Figuring out why this loop fails?!!!!
        # For some reason, when I loop over the list of widgets to create the
        # attributes, the loop wouldn't go though all the items. I'm forcing
        # here to go through loop as long as it meets the requirements. (I
        # have look into this later) (The problem happens lines 99-112)
        if self.created_attributes:
            for left_over in self.created_attributes:
                if type(left_over) == PrimVarSWidget:
                    if left_over.file_node_name.text():
                        self.assign_attributes()
                else:
                    if left_over.attr_name.text():
                        self.assign_attributes()

    @staticmethod
    def setup_primvar_node(node_name, attr_name, attr_type):
        """
        Assign the PrimVar attribute name to the PxrPrimVar node and set its
        type to the corresponding type.

        :param node_name: (str) Name of the PxrPrimVar node
        :param attr_name: (str) Attribute's name
        :param attr_type: (str) Type of the attribute. ex: float, color,...
        """

        try:
            core.set_attr(pm.PyNode(node_name), "varname", attr_name)
            core.set_attr(pm.PyNode(node_name), "type", attr_type)
        except Exception as e:
            logging.warning(str(e))

    @staticmethod
    def clear_files(rmans_widget):
        """
        Remove all the existing files from the given rmans PrimVar widget.

        :param rmans_widget: (QtGui.QWidget)
        """

        # Clear the exiting label
        for label in rmans_widget.existing_labels:
            label.deleteLater()

        rmans_widget.existing_labels = []

    @staticmethod
    def create_node(widget_primvar_name, node_type="PxrPrimvar"):
        """
        Create a new primvar node and set the name of the new node to the
        "Node Name" of the widget.

        :param widget_primvar_name: (QtGui.QLineEdit) Widget to be set once
        the new PxrPrimvar is created
        :param node_type: (str) Type of nore to be created, ex:
        """

        new_node = pm.createNode(node_type)
        widget_primvar_name.setText(str(new_node.name()))

    @staticmethod
    def warning(message):
        """ Popping up a UI showing the warning message.

        :param message: (str) warning message to display.
        :return: (QtGui.QMessageBox) QWidget
        """

        warning_box = QtGui.QMessageBox()
        warning_box.setText(message)
        warning_box.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        warning_box.exec_()

    @staticmethod
    def validate(attr_object):
        """ It validates whether or not the widgets's attribute's name is set

        :param attr_object: (QtGui.QFrame) The attributes Widget
        :return: (boolean) It returns True if the object is valid,
        False otherwise
        """

        # If there missing information for assigning the attribute, abort the
        #  assignment and warn the user
        if not attr_object.attr_name.text():
            logging.warning('A "PrimVar"  attribute was failed to be assigned '
                            'because of lack of enough information.')
            return False
        else:
            return True

    @staticmethod
    def go_to_wiki():
        """
        Opens the browser link and direct it to the help page on RenderMan.
        """

        url_page = "https://renderman.pixar.com/view/how-to-primitive-variables"
        webbrowser.open_new(url=url_page)

    @staticmethod
    def go_to_doc():
        """
        Opens the browser link and direct it to the local documentation page
        for this tool.
        """

        url_page = "http://alijafargholi.github.io/prman_rfmPrimVarTool/"
        webbrowser.open_new(url=url_page)

    def primvar_s(self, shapes, attr):
        """
        Assigning the rmans Primvar attributes to the given shape nodes

        :param shapes: (list of PyNode shapes) Shape nodes to be assigned.
        :param attr: (QtGui.QFrame) The QtGui Frame corresponding to the
        'rmans' attribute, for extracting the new attributes information.
        """

        # If there missing information for assigning the attribute, abort the
        #  assignment and warn the user
        if not attr.file_node_name.text() or not attr.new_strings:
            logging.warning('An "String PrimVar" failed, because of lack of '
                            'enough information')
            return

        # Make sure there is a file name
        if not attr.file_node_name.text():
            logging.warning('The "File" is required.')
            return

        if type(pm.PyNode(attr.file_node_name.text())) == \
                pm.nodetypes.PxrTexture:
            texture_attr_name = 'filename'
        elif type(pm.PyNode(attr.file_node_name.text())) == pm.nodetypes.File:
            texture_attr_name = 'fileTextureName'
        else:
            logging.warning('Selected texture read file node should be either '
                            'File type or PxrTexture type.')
            return

        # Create the new attribute name
        attribute_name = "rmanS" + attr.file_node_name.text() + "_" + \
                         texture_attr_name

        # Pick a random sting from the list and assign it to the shape
        for shape in shapes:
            core.add_attr(shape, attribute_name, dataType="string")
            core.set_attr(shape, attribute_name,
                          str(random.choice(attr.new_strings)))

        # Deleting the UI
        self.delete_widget(attr)

    def primvar_f(self, shapes, attr):
        """
        Assigning the rmanf Primvar attributes to the given shape nodes

        :param shapes: (list of PyNode shapes) Shape nodes to be assigned.
        :param attr: (QtGui.QFrame) The QtGui Frame corresponding to the
        'rmanf' attribute, for extracting the new attributes information.
        """

        # Validating the information
        if not self.validate(attr):
            return

        # Creating the new name for the attribute
        attribute_name = "rmanF" + attr.attr_name.text()

        # Assigning a random number to the shapes based on the given attributes
        for shape_node in shapes:
            core.add_attr(shape_node, attribute_name, attributeType='double')
            if attr.type_float.isChecked():
                core.set_attr(shape_node, attribute_name, random.uniform(
                    attr.min_value.value(),
                    attr.max_value.value()))
            else:
                core.set_attr(shape_node, attribute_name, random.randint(
                    attr.min_value.value(),
                    attr.max_value.value()))

        # If a PrimVar node is given and the node exists, setup the values for
        # that node
        if attr.primvar_node_name.text() and pm.objExists(
                attr.primvar_node_name.text()):
            self.setup_primvar_node(attr.primvar_node_name.text(),
                                    attr.attr_name.text(),
                                    "float")

        # Deleting the UI
        self.delete_widget(attr)

    def primvar_c(self, shapes, attr):
        """
        Assigning the rmanc Primvar attributes to the given shape nodes

        :param shapes: (list of PyNode shapes) Shape nodes to be assigned.
        :param attr: (QtGui.QFrame) The QtGui Frame corresponding to the
        'rmanc' attribute, for extracting the new attributes information.
        """

        # Validating the information
        if not self.validate(attr):
            return

        # Creating a new attribute name
        attribute_name = "rmanC" + attr.attr_name.text()

        # Creating the color attribute shapes
        for shape in shapes:
            core.add_attr(shape, attribute_name, attributeType='float3',
                          usedAsColor=True)
            core.add_attr(shape, attr.attr_name.text()+"r",
                          attributeType='float',
                          parent=attribute_name)
            core.add_attr(shape, attr.attr_name.text()+"g",
                          attributeType='float',
                          parent=attribute_name)
            core.add_attr(shape, attr.attr_name.text()+"b",
                          attributeType='float',
                          parent=attribute_name)
            # If random color is selected!
            if attr.random_color.isChecked():
                core.set_attr(shape, attribute_name,
                              core.get_random_color_shade(
                                  min_s=attr.min_s_value.value(),
                                  max_s=attr.max_s_value.value(),
                                  min_v=attr.min_v_value.value(),
                                  max_v=attr.max_v_value.value(),
                                  hue=random.randint(0, 360)))

            # If random color shade is selected!
            elif attr.random_color_shades.isChecked():
                core.set_attr(shape, attribute_name,
                              core.get_random_color_shade(
                                  min_s=attr.min_s_value.value(),
                                  max_s=attr.max_s_value.value(),
                                  min_v=attr.min_v_value.value(),
                                  max_v=attr.max_v_value.value(),
                                  hue=attr.core_color))

            # If random grayscale is selected!
            else:
                # Saturation --> 0
                # Hue --> doesn't matter
                # Value --> between given min and max
                core.set_attr(shape, attribute_name,
                              core.get_random_color_shade(
                                  max_s=0,
                                  min_v=attr.min_v_value.value(),
                                  max_v=attr.max_v_value.value()))

        # If a PrimVar node is given and the node exists, setup the values for
        # that node
        if attr.primvar_node_name.text() and pm.objExists(
                attr.primvar_node_name.text()):
            self.setup_primvar_node(attr.primvar_node_name.text(),
                                    attr.attr_name.text(),
                                    "color")

        # Deleting the UI
        self.delete_widget(attr)

    def primvar_v(self, shapes, attr):
        """
        Assigning the rmanv Primvar attributes to the given shape nodes.

        :param shapes: (list of PyNode shapes) Shape nodes to be assigned.
        :param attr: (QtGui.QFrame) The QtGui Frame corresponding to the
        'rmanv' attribute, for extracting the new attributes information.
        """

        # Validating the information
        if not self.validate(attr):
            return

        # Creating the new name for the attribute
        attribute_name = "rmanV" + attr.attr_name.text()

        # Assigning a random vector to the shapes based on the given attributes
        for shape in shapes:
            # Create the attribute
            core.add_attr(shape, attribute_name, attributeType='float3')
            core.add_attr(shape, attr.attr_name.text() + "x",
                          attributeType='float', parent=attribute_name)
            core.add_attr(shape, attr.attr_name.text() + "y",
                          attributeType='float', parent=attribute_name)
            core.add_attr(shape, attr.attr_name.text() + "z",
                          attributeType='float', parent=attribute_name)
            # Setting the attribute
            core.set_attr(shape,
                          attribute_name,
                          core.get_random_vector(attr.min_x_value.value(),
                                                 attr.max_x_value.value(),
                                                 attr.min_y_value.value(),
                                                 attr.max_y_value.value(),
                                                 attr.min_z_value.value(),
                                                 attr.max_z_value.value(),
                                                 attr.variation.isChecked(),
                                                 str(attr.type.currentText())))

        # If a PrimVar node is given and the node exists, setup the values for
        # that node
        if attr.primvar_node_name.text() and pm.objExists(
                attr.primvar_node_name.text()):
            self.setup_primvar_node(attr.primvar_node_name.text(),
                                    attr.attr_name.text(),
                                    "vector")

        # Deleting the UI
        self.delete_widget(attr)

    def primvar_p(self, shapes, attr):
        """
        Assigning the rmanp Primvar attributes to the given shape nodes.

        :param shapes: (list of PyNode shapes) Shape nodes to be assigned.
        :param attr: (QtGui.QFrame) The QtGui Frame corresponding to the
        'rmanp' attribute, for extracting the new attributes information.
        """

        # Validating the information
        if not self.validate(attr):
            return

        # Creating the new name for the attribute
        attribute_name = "rmanP" + attr.attr_name.text()

        # Assigning a random vector to the shapes based on the given attributes
        for shape in shapes:
            # Create the attribute
            core.add_attr(shape, attribute_name, attributeType='float3')
            core.add_attr(shape, attr.attr_name.text() + "x",
                          attributeType='float', parent=attribute_name)
            core.add_attr(shape, attr.attr_name.text() + "y",
                          attributeType='float', parent=attribute_name)
            core.add_attr(shape, attr.attr_name.text() + "z",
                          attributeType='float', parent=attribute_name)
            # Setting the attribute
            core.set_attr(shape,
                          attribute_name,
                          core.get_random_vector(attr.min_x_value.value(),
                                                 attr.max_x_value.value(),
                                                 attr.min_y_value.value(),
                                                 attr.max_y_value.value(),
                                                 attr.min_z_value.value(),
                                                 attr.max_z_value.value(),
                                                 attr.variation.isChecked(),
                                                 str(attr.type.currentText())))

        # If a PrimVar node is given and the node exists, setup the values for
        # that node
        if attr.primvar_node_name.text() and pm.objExists(
                attr.primvar_node_name.text()):
            self.setup_primvar_node(attr.primvar_node_name.text(),
                                    attr.attr_name.text(),
                                    "point")

        # Deleting the UI
        self.delete_widget(attr)

    def primvar_n(self, shapes, attr):
        """
        Assigning the rmann Primvar attributes to the given shape nodes.

        :param shapes: (list of PyNode shapes) Shape nodes to be assigned.
        :param attr: (QtGui.QFrame) The QtGui Frame corresponding to the
        'rmann' attribute, for extracting the new attributes information.
        """

        # Validating the information
        if not self.validate(attr):
            return

        # Creating the new name for the attribute
        attribute_name = "rmann" + attr.attr_name.text()

        # Assigning a random vector to the shapes based on the given attributes
        for shape in shapes:
            # Create the attribute
            core.add_attr(shape, attribute_name, attributeType='float3')
            core.add_attr(shape, attr.attr_name.text() + "r",
                          attributeType='float', parent=attribute_name)
            core.add_attr(shape, attr.attr_name.text() + "g",
                          attributeType='float', parent=attribute_name)
            core.add_attr(shape, attr.attr_name.text() + "b",
                          attributeType='float', parent=attribute_name)
            # Setting the attribute
            core.set_attr(shape,
                          attribute_name,
                          core.get_random_vector(attr.min_x_value.value(),
                                                 attr.max_x_value.value(),
                                                 attr.min_y_value.value(),
                                                 attr.max_y_value.value(),
                                                 attr.min_z_value.value(),
                                                 attr.max_z_value.value(),
                                                 attr.variation.isChecked(),
                                                 str(attr.type.currentText())))

        # If a PrimVar node is given and the node exists, setup the values for
        # that node
        if attr.primvar_node_name.text() and pm.objExists(
                attr.primvar_node_name.text()):
            self.setup_primvar_node(attr.primvar_node_name.text(),
                                    attr.attr_name.text(),
                                    "normal")

        # Deleting the UI
        self.delete_widget(attr)

    def create_rman_c(self):
        """
        Create and assigning signals to the corresponding widgets of the newly
        created widget, and added to the list of rmanc attribute
        """

        # Create a new instance of rmanc widget
        rmanc = PrimVarCWidget()

        # Connecting the signals to the functions
        rmanc.get_node_name.clicked.connect(partial(self.get_selected_name,
                                                    rmanc.primvar_node_name))
        rmanc.create_node.clicked.connect(partial(self.create_node,
                                                  rmanc.primvar_node_name))
        rmanc.delete_this.clicked.connect(partial(self.delete_widget, rmanc))

        # Adding the newly created widgets to the rmanc layout
        self.rmanCLayout.addWidget(rmanc)

        # Finally store it to the list
        self.created_attributes.append(rmanc)

    def create_rman_f(self):
        """
        Create amd assigning signals to the corresponding widgets of the newly
        created widget, and added to the list of rmanf attribute
        """

        # Create a new instance of rmanf widget
        rmanf = PrimVarFWidget()

        # Connecting the signals to the functions
        rmanf.get_node_name.clicked.connect(partial(self.get_selected_name,
                                                    rmanf.primvar_node_name))
        rmanf.create_node.clicked.connect(partial(self.create_node,
                                                  rmanf.primvar_node_name))
        rmanf.delete_this.clicked.connect(partial(self.delete_widget, rmanf))

        # Adding the newly created widgets to the rmanf layout
        self.rmanFLayout.addWidget(rmanf)

        # Finally store it to the list
        self.created_attributes.append(rmanf)

    def create_rman_s(self):
        """
        Create and assigning signals to the corresponding widgets of the newly
        created widget, and added to the list of rmanf attribute
        """

        # Create a new instance of rmans widget
        rmans = PrimVarSWidget()

        # Connecting the signals to the functions
        rmans.gather_files.clicked.connect(partial(self.get_files, rmans))
        rmans.clear_files.clicked.connect(partial(self.clear_files, rmans))
        rmans.delete_this.clicked.connect(partial(self.delete_widget, rmans))
        rmans.create_node.clicked.connect(partial(self.create_node,
                                                  rmans.file_node_name,
                                                  "file"))
        rmans.get_node_name.clicked.connect(partial(self.get_selected_name,
                                                    rmans.file_node_name))

        # Adding the newly created widgets to the rmans layout
        self.rmanSLayout.addWidget(rmans)

        # Finally store it to the list
        self.created_attributes.append(rmans)

    def create_rman_v(self):
        """
        Create and assigning signals to the corresponding widgets of the newly
        created widget, and added to the list of rmanv attribute
        """

        # Create a new instance of rmans widget
        rmanv = PrimVarVWidget()

        # Connecting the signals to the functions
        rmanv.get_node_name.clicked.connect(partial(self.get_selected_name,
                                                    rmanv.primvar_node_name))
        rmanv.create_node.clicked.connect(partial(self.create_node,
                                                  rmanv.primvar_node_name))
        rmanv.delete_this.clicked.connect(partial(self.delete_widget, rmanv))

        # Adding the newly created widgets to the rmanv layout
        self.rmanVLayout.addWidget(rmanv)

        # Finally store it to the list
        self.created_attributes.append(rmanv)

    def create_rman_p(self):
        """
        Create and assigning signals to the corresponding widgets of the newly
        created widget, and added to the list of rmanp attribute
        """

        # Create a new instance of rmanp widget
        rmanp = PrimVarPWidget()

        # Connecting the signals to the functions
        rmanp.get_node_name.clicked.connect(partial(self.get_selected_name,
                                                    rmanp.primvar_node_name))
        rmanp.create_node.clicked.connect(partial(self.create_node,
                                                  rmanp.primvar_node_name))
        rmanp.delete_this.clicked.connect(partial(self.delete_widget, rmanp))

        # Adding the newly created widgets to the rmanp layout
        self.rmanPLayout.addWidget(rmanp)

        # Finally store it to the list
        self.created_attributes.append(rmanp)

    def create_rman_n(self):
        """
        Create and assigning signals to the corresponding widgets of the newly
        created widget, and added to the list of rmann attribute
        """

        # Create a new instance of rmann widget
        rmann = PrimVarNWidget()

        # Connecting the signals to the functions
        rmann.get_node_name.clicked.connect(partial(self.get_selected_name,
                                                    rmann.primvar_node_name))
        rmann.create_node.clicked.connect(partial(self.create_node,
                                                  rmann.primvar_node_name))
        rmann.delete_this.clicked.connect(partial(self.delete_widget, rmann))

        # Adding the newly created widgets to the rmann layout
        self.rmanNLayout.addWidget(rmann)

        # Finally store it to the list
        self.created_attributes.append(rmann)

    def get_files(self, rmans_widget):
        """
        It'll open a QtGui file browser and store the values in a list and
        show them on the rmanS widgets

        :param rmans_widget:
        """

        string_list = QtGui.QFileDialog.getOpenFileNames()
        string_list = [str(value) for value in string_list[0]]

        rmans_widget.new_strings = sorted(list(set(string_list +
                                                   rmans_widget.new_strings)))

        # Clear the exiting label
        self.clear_files(rmans_widget)

        # Create a label from each string and add them to the widget
        for string in rmans_widget.new_strings:
            new_label = QtGui.QLabel(string)
            rmans_widget.existing_labels.append(new_label)
            rmans_widget.stringListLayout.addWidget(new_label)

    def get_selected_name(self, widget_primvar_name):
        """
        Get the name of the selected node and set it as a text to the
        given field.

        :widget_primvar_name: the field that the name is going to be set to.
        """

        try:
            widget_primvar_name.setText(str(pm.ls(sl=True)[0].name()))
        except IndexError:
            self.warning(message="It seems no node is selected.\n")

    def delete_widget(self, widget):
        """
        Delete the given widgets and remove it from the list of existing
        widgets.

        :param widget: (QtGui.QWidget) the widget that needs to be
        deleted/removed
        """

        widget.deleteLater()
        self.created_attributes.remove(widget)

    def clear(self):
        """
        Delete all the Primvar widgets from the Ui and remove them from the
        list
        """

        for widget in self.created_attributes:
            widget.deleteLater()
            self.created_attributes.remove(widget)

    def setup_stylesheet(self):
        """
        Assign the stylesheet to the UI
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


class PrimVarCWidget(QtGui.QFrame, cWidget):
    """
    Create a Primvar C Widgets
    """

    def __init__(self, *args, **kwargs):
        super(PrimVarCWidget, self).__init__(*args, **kwargs)

        self.setupUi(self)
        self.setup_signals()

        self.setFrameStyle(QtGui.QFrame.Panel | QtGui.QFrame.Raised)
        self.mainLayout.setAlignment(QtCore.Qt.AlignTop)
        self.color_picker.setDisabled(True)

        # Adding regular expression, making sure no illegal value is entered
        reg_ex = QtCore.QRegExp("[a-z-A-Z_0-9]+")

        attr_validator = QRegExpValidator(reg_ex, self.attr_name)
        self.attr_name.setValidator(attr_validator)

        # Initializing the color value
        self._core_color = 0

    @property
    def core_color(self):
        """
        Property of the color value that would be use for random shade of
        color option.

        :return: (int) Integer representing the Hue value of the selected color
        """

        return self._core_color

    @core_color.setter
    def core_color(self, value):
        """
        Setter for the core_color value

        :param value: (int) Hue value for shade of color option
        """

        # This is the value coming from QtGui in hex
        value = value.lstrip('#')
        lv = len(value)
        # Converting the hex to RGB value (0-1)
        rgb = [x / 255.0 for x in tuple(int(value[i:i + lv // 3], 16) for i
                                        in range(0, lv, lv // 3))]
        # Converting the RGB value to hsv. Since we just need the Hue,
        # we just return the first element. Since the hue is between 0 and 1,
        #  we multiply that by 360 to get the Hue in degree
        self._core_color = colorsys.rgb_to_hsv(rgb[0], rgb[1], rgb[2])[0] * 360

    def setup_signals(self):
        """
        Connecting signals of the Primvar C widget
        """

        self.color_picker.clicked.connect(self.pick_color)
        self.random_color.toggled.connect(self.random_color_selected)
        self.random_color_shades.toggled.connect(
            self.random_color_shades_selected)
        self.random_grayscale.toggled.connect(self.random_grayscale_selected)

    def random_color_selected(self, enabled):
        """
        Disabling not needed widgets when choosing the random color selected.
        """

        if enabled:
            self.color_picker.setDisabled(True)
            self.min_s_value.setDisabled(False)
            self.max_s_value.setDisabled(False)

    def random_color_shades_selected(self, enabled):
        """
        Disabling not needed widgets when choosing the random shade of color
        option.
        """

        if enabled:
            self.color_picker.setDisabled(False)
            self.min_v_value.setDisabled(False)
            self.max_v_value.setDisabled(False)

    def random_grayscale_selected(self, enabled):
        """
        Disabling not needed widgets when choosing the random grayscale
        options.
        """

        if enabled:
            self.color_picker.setDisabled(True)
            self.min_s_value.setDisabled(True)
            self.max_s_value.setDisabled(True)

    def pick_color(self):
        """
        Open up the QtGui.QColorDialog for choosing the color for random
        shade of color option, and storing in core_color variable
        """

        new_color = QtGui.QColorDialog.getColor().name()
        self.color_picker.setStyleSheet("background-color: {}".format(
            new_color))
        self.core_color = new_color


class PrimVarFWidget(QtGui.QFrame, fWidget):
    """
    Create a Primvar F Widgets
    """

    def __init__(self, *args, **kwargs):
        super(PrimVarFWidget, self).__init__(*args, **kwargs)

        self.setupUi(self)
        self.setFrameStyle(QtGui.QFrame.Panel | QtGui.QFrame.Raised)
        self.mainLayout.setAlignment(QtCore.Qt.AlignTop)
        self.type_int.toggled.connect(self.go_integer)
        self.type_float.toggled.connect(self.go_float)

        # Adding regular expression, making sure no illegal value is entered
        reg_ex = QtCore.QRegExp("[a-z-A-Z_0-9]+")
        attr_validator = QRegExpValidator(reg_ex, self.attr_name)
        self.attr_name.setValidator(attr_validator)

    def go_integer(self, enabled):
        """
        Change the stepping of the spin box, form 0.1 to 1 when choosing the
        integer option.

        :param enabled: (boolean) if the Integer radio is checked.
        """

        if enabled:
            self.min_value.setSingleStep(1)
            self.max_value.setSingleStep(1)

    def go_float(self, enabled):
        """
        Change the stepping of the spin box, form 1 to 0.1, when choosing the
        float options.

        :param enabled: (boolean) if the Float radio is checked.
        """

        if enabled:
            self.min_value.setSingleStep(0.1)
            self.max_value.setSingleStep(0.1)


class PrimVarSWidget(QtGui.QFrame, sWidget):
    """
    Create a Primvar S Widgets
    """

    def __init__(self, *args, **kwargs):
        super(PrimVarSWidget, self).__init__(*args, **kwargs)

        self._new_strings = []
        self._existing_labels = []

        self.setupUi(self)
        self.setFrameStyle(QtGui.QFrame.Panel | QtGui.QFrame.Raised)
        self.mainLayout.setAlignment(QtCore.Qt.AlignTop)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setSpacing(1)

        # Adding regular expression, making sure no illegal value is entered
        reg_ex = QtCore.QRegExp("[a-z-A-Z_0-9]+")
        attr_validator = QRegExpValidator(reg_ex, self.file_node_name)
        self.file_node_name.setValidator(attr_validator)

    @property
    def existing_labels(self):
        """
        Property of the existing_labels that would store the selected strings.

        :return: (list) returns the value of the existing_labels
        """

        return self._existing_labels

    @existing_labels.setter
    def existing_labels(self, value):
        """
        Setter of the existing_labels variable.

        :param value: (list) list of new strings.
        """

        self._existing_labels = value

    @property
    def new_strings(self):
        """
        Property of the new_strings.

        :return: (list) new_strings
        """
        return self._new_strings

    @new_strings.setter
    def new_strings(self, value):
        """
        Setter of the new_strings variable.

        :param value: (list) list of new strings.
        """

        self._new_strings = value


class PrimVarNWidget(QtGui.QFrame, nWidget):
    """
    Create a Primvar N Widgets
    """

    def __init__(self, *args, **kwargs):
        super(PrimVarNWidget, self).__init__(*args, **kwargs)

        self.setupUi(self)
        self.setup_signals()
        self.setFrameStyle(QtGui.QFrame.Panel | QtGui.QFrame.Raised)
        self.mainLayout.setAlignment(QtCore.Qt.AlignTop)

        # Adding regular expression, making sure no illegal value is entered
        reg_ex = QtCore.QRegExp("[a-z-A-Z_0-9]+")
        attr_validator = QRegExpValidator(reg_ex, self.attr_name)
        self.attr_name.setValidator(attr_validator)

    def setup_signals(self):
        """
        Connecting signals of the Primvar V widget
        """

        self.variation.toggled.connect(self.uniform_selected)
        self.uniform.toggled.connect(self.variation_selected)

    def variation_selected(self, enabled):
        """
        Disabling not needed widgets when choosing the Variant type.

        :param enabled: (boolean) Status of the type
        """

        if enabled:
            self.min_y_value.setDisabled(True)
            self.max_y_value.setDisabled(True)
            self.min_z_value.setDisabled(True)
            self.max_z_value.setDisabled(True)

    def uniform_selected(self, enabled):
        """
        Disabling not needed widgets when choosing the Uniform type.

        :param enabled: (boolean) Status of the type
        """

        if enabled:
            self.min_y_value.setDisabled(False)
            self.max_y_value.setDisabled(False)
            self.min_z_value.setDisabled(False)
            self.max_z_value.setDisabled(False)


class PrimVarPWidget(QtGui.QFrame, pWidget):
    """
    Create a Primvar P Widgets
    """

    def __init__(self, *args, **kwargs):
        super(PrimVarPWidget, self).__init__(*args, **kwargs)

        self.setupUi(self)
        self.setup_signals()
        self.setFrameStyle(QtGui.QFrame.Panel | QtGui.QFrame.Raised)
        self.mainLayout.setAlignment(QtCore.Qt.AlignTop)

        # Adding regular expression, making sure no illegal value is entered
        reg_ex = QtCore.QRegExp("[a-z-A-Z_0-9]+")
        attr_validator = QRegExpValidator(reg_ex, self.attr_name)
        self.attr_name.setValidator(attr_validator)

    def setup_signals(self):
        """
        Connecting signals of the Primvar P widget
        """

        self.variation.toggled.connect(self.uniform_selected)
        self.uniform.toggled.connect(self.variation_selected)

    def variation_selected(self, enabled):
        """
        Disabling not needed widgets when choosing the Variant type.

        :param enabled: (boolean) Status of the type
        """

        if enabled:
            self.min_y_value.setDisabled(True)
            self.max_y_value.setDisabled(True)
            self.min_z_value.setDisabled(True)
            self.max_z_value.setDisabled(True)

    def uniform_selected(self, enabled):
        """
        Disabling not needed widgets when choosing the Uniform type.

        :param enabled: (boolean) Status of the type
        """

        if enabled:
            self.min_y_value.setDisabled(False)
            self.max_y_value.setDisabled(False)
            self.min_z_value.setDisabled(False)
            self.max_z_value.setDisabled(False)


class PrimVarVWidget(QtGui.QFrame, vWidget):
    """
    Create a Primvar V Widgets
    """

    def __init__(self, *args, **kwargs):
        super(PrimVarVWidget, self).__init__(*args, **kwargs)

        self.setupUi(self)
        self.setup_signals()
        self.setFrameStyle(QtGui.QFrame.Panel | QtGui.QFrame.Raised)
        self.mainLayout.setAlignment(QtCore.Qt.AlignTop)

        # Adding regular expression, making sure no illegal value is entered
        reg_ex = QtCore.QRegExp("[a-z-A-Z_0-9]+")
        attr_validator = QRegExpValidator(reg_ex, self.attr_name)
        self.attr_name.setValidator(attr_validator)

    def setup_signals(self):
        """
        Connecting signals of the Primvar V widget
        """

        self.variation.toggled.connect(self.uniform_selected)
        self.uniform.toggled.connect(self.variation_selected)

    def variation_selected(self, enabled):
        """
        Disabling not needed widgets when choosing the Variant type.

        :param enabled: (boolean) Status of the type
        """

        if enabled:
            self.min_y_value.setDisabled(True)
            self.max_y_value.setDisabled(True)
            self.min_z_value.setDisabled(True)
            self.max_z_value.setDisabled(True)

    def uniform_selected(self, enabled):
        """
        Disabling not needed widgets when choosing the Uniform type.

        :param enabled: (boolean) Status of the type
        """

        if enabled:
            self.min_y_value.setDisabled(False)
            self.max_y_value.setDisabled(False)
            self.min_z_value.setDisabled(False)
            self.max_z_value.setDisabled(False)


def create_ui():
    """
    Create an instance of the Primvar Manager GUI

    :return: QWidget
    """

    global primVarAppUi

    if not primVarAppUi:
        primVarAppUi = PrimVarApp()

    primVarAppUi.show()


def close_ui():
    """
    Close the existing Primvar Manager Ui
    """

    global primVarAppUi
    if primVarAppUi:
        primVarAppUi.deleteLater()
        primVarAppUi = None


def main():
    """
    If the application is ran in terminal, show the documentation of the tool

    :return: (str) help documents of the
    """

    import __main__
    print help(__main__)
if __name__ == '__main__':
    main()
