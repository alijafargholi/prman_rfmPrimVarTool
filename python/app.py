# IMPORT STANDARD MODULES
import sys
import os
import random
import logging
from functools import partial
import webbrowser

# IMPORT LOCAL MODULES
import PySide.QtCore as QtCore
import PySide.QtGui as QtGui
from utils import core
from gui.mainWindow import Ui_primvarManager
from gui.rmanCwidget import Ui_Form as cWidget
from gui.rmanFwidget import Ui_Form as fWidget
from gui.rmanNwidget import Ui_Form as nWidget
from gui.rmanSwidget import Ui_Form as sWidget
from gui.rmanPwidget import Ui_Form as pWidget
from gui.rmanVwidget import Ui_Form as vWidget

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


class PrimVarApp(QtGui.QMainWindow, Ui_primvarManager):
    """

    """
    def __init__(self, *args, **kwargs):
        super(PrimVarApp, self).__init__(*args, **kwargs)

        self._attributes = {"rmanc": {"function": self.rmanf, "attrs": []},
                            "rmanf": {"function": self.rmanf, "attrs": []},
                            "rmans": {"function": self.rmans, "attrs": []},
                            "rmanv": {"function": self.rmanf, "attrs": []},
                            "rmanp": {"function": self.rmanf, "attrs": []},
                            "rmann": {"function": self.rmanf, "attrs": []}}

        self.setupUi(self)
        self.init_ui()
        self.setup_signals()

    def init_ui(self):
        """

        :return:
        """
        self.rmanCLayout.setAlignment(QtCore.Qt.AlignTop)
        self.rmanFLayout.setAlignment(QtCore.Qt.AlignTop)
        self.rmanSLayout.setAlignment(QtCore.Qt.AlignTop)
        self.rmanVLayout.setAlignment(QtCore.Qt.AlignTop)
        self.rmanPLayout.setAlignment(QtCore.Qt.AlignTop)
        self.rmanNLayout.setAlignment(QtCore.Qt.AlignTop)

    def setup_signals(self):
        """

        :return:
        """
        self.action_close_ui.triggered.connect(close_ui)
        self.action_clear.triggered.connect(self.clear)
        self.action_pxar_Documenation.triggered.connect(self.go_to_wiki)
        self.assign.clicked.connect(self.assign_attributes)
        self.createRmanC.clicked.connect(self.create_rman_c)
        self.createRmanF.clicked.connect(self.create_rman_f)
        self.createRmanS.clicked.connect(self.create_rman_s)
        self.createRmanV.clicked.connect(self.create_rman_v)
        self.createRmanP.clicked.connect(self.create_rman_p)
        self.createRmanN.clicked.connect(self.create_rman_n)

    def assign_attributes(self):
        """

        :return:
        """
        # Getting the shape nodes of selected objects
        shapes = list(core.get_shapes(core.unpack(pm.ls(sl=True))))
        print shapes
        # If nothing is selected, warn the user
        if not shapes:
            warning_message = "\n" + ("*" * 80) + "\n\t\t\tNo Object is " \
                                                  "selected.\n\n" + ("*" * 80) \
                              + "\n"
            logging.warning(warning_message)
            return

        for attr_type in self._attributes.keys():
            for new_attr in self._attributes[attr_type]["attrs"]:
                self._attributes[attr_type]["function"](shapes, new_attr)

        close_ui()

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

    def rmanf(self, shapes, attr):
        """

        :param shapes:
        :param attr:
        """

        attribute_name = "rmanF" + attr.attr_name.text()

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

        if attr.primvar_node_name.text():
            self.setup_primvar_node(attr.primvar_node_name.text(),
                                    attribute_name,
                                    "float")

    def rmans(self, shapes, attr):
        """

        :param shapes:
        :param attr:
        """
        attribute_name = "rmanS" + attr.attr_name.text()

        for shape in shapes:
            core.add_attr(shape, attribute_name, dataType="string")
            core.set_attr(shape, attribute_name,
                          str(random.choice(attr.new_strings)))

    def create_rman_c(self):
        """

        :return:
        """
        rmanc = PrimVarCWidget()
        rmanc.get_node_name.clicked.connect(partial(self.get_selected_name,
                                                    rmanc.primvar_node_name))
        rmanc.create_node.clicked.connect(partial(self.create_primvar_node,
                                                  rmanc.primvar_node_name))
        rmanc.delete_this.clicked.connect(partial(self.delete_widget, rmanc,
                                                  "rmanc"))
        self.rmanCLayout.addWidget(rmanc)
        self._attributes["rmanc"]["attrs"].append(rmanc)

    def create_rman_f(self):
        """

        :return:
        """
        rmanf = PrimVarFWidget()
        rmanf.get_node_name.clicked.connect(partial(self.get_selected_name,
                                                    rmanf.primvar_node_name))
        rmanf.create_node.clicked.connect(partial(self.create_primvar_node,
                                                  rmanf.primvar_node_name))
        rmanf.delete_this.clicked.connect(partial(self.delete_widget, rmanf,
                                                  "rmanf"))
        self.rmanFLayout.addWidget(rmanf)
        self._attributes["rmanf"]["attrs"].append(rmanf)

    def create_rman_s(self):
        """

        :return:
        """
        rmans = PrimVarSWidget()
        rmans.gather_files.clicked.connect(partial(self.get_files, rmans))
        rmans.clear_files.clicked.connect(partial(self.clear_files, rmans))
        rmans.delete_this.clicked.connect(partial(self.delete_widget, rmans,
                                                  "rmans"))
        self.rmanSLayout.addWidget(rmans)
        self._attributes["rmans"]["attrs"].append(rmans)

    def create_rman_v(self):
        """

        :return:
        """
        rmanv = PrimVarVWidget()
        rmanv.get_node_name.clicked.connect(partial(self.get_selected_name,
                                                    rmanv.primvar_node_name))

        rmanv.create_node.clicked.connect(partial(self.create_primvar_node,
                                                  rmanv.primvar_node_name))
        rmanv.delete_this.clicked.connect(partial(self.delete_widget, rmanv,
                                                  "rmanv"))
        self.rmanVLayout.addWidget(rmanv)
        self._attributes["rmanv"]["attrs"].append(rmanv)

    def create_rman_p(self):
        """

        :return:
        """
        rmanp = PrimVarPWidget()
        rmanp.get_node_name.clicked.connect(partial(self.get_selected_name,
                                                    rmanp.primvar_node_name))
        rmanp.create_node.clicked.connect(partial(self.create_primvar_node,
                                                  rmanp.primvar_node_name))
        rmanp.delete_this.clicked.connect(partial(self.delete_widget, rmanp,
                                                  "rmanp"))
        self.rmanPLayout.addWidget(rmanp)
        self._attributes["rmanp"]["attrs"].append(rmanp)

    def create_rman_n(self):
        """

        :return:
        """
        rmann = PrimVarNWidget()
        rmann.get_node_name.clicked.connect(partial(self.get_selected_name,
                                                    rmann.primvar_node_name))
        rmann.create_node.clicked.connect(partial(self.create_primvar_node,
                                                  rmann.primvar_node_name))
        rmann.delete_this.clicked.connect(partial(self.delete_widget, rmann,
                                                  "rmann"))
        self.rmanNLayout.addWidget(rmann)
        self._attributes["rmann"]["attrs"].append(rmann)

    @staticmethod
    def clear_files(rmans_widget):
        """

        :param rmans_widget:
        """
        # Clear the exiting label
        for label in rmans_widget.existing_labels:
            label.deleteLater()
        rmans_widget.existing_labels = []
        print "Cleared --> ", rmans_widget.existing_labels

    def get_files(self, rmans_widget):
        """

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

    @staticmethod
    def create_primvar_node(widget_primvar_name):
        """ Create a new primvar node and set the name of the new node to the
            "Node Name" of the widget.

        :param widget_primvar_name:
        """
        new_node = pm.createNode("PxrPrimvar")
        widget_primvar_name.setText(str(new_node.name()))

    def get_selected_name(self, widget_primvar_name):
        """ Will get the name of the selected node and set it as a text to the
            given field.

        :widget_primvar_name: the field that the name is going to be set to.
        """
        try:
            widget_primvar_name.setText(str(pm.ls(sl=True)[0].name()))
        except IndexError:
            self.warning(message="It seems no node is selected.\n")

    def delete_widget(self, widget, attr_type):
        """

        :param widget:
        :param attr_type:
        """
        widget.deleteLater()
        self._attributes[attr_type]["attrs"].remove(widget)

    def clear(self):
        """
        """

        for attr_type in self._attributes.keys():
            for attr_widget in self._attributes[attr_type]["attrs"]:
                attr_widget.deleteLater()
            self._attributes[attr_type]["attrs"] = []

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
    def go_to_wiki():
        """
        Opens the browser link and direct it to the help page for this tool
        """
        url_page = "https://renderman.pixar.com/view/how-to-primitive-variables"
        webbrowser.open_new(url=url_page)


class PrimVarCWidget(QtGui.QFrame, cWidget):
    """

    """
    def __init__(self, *args, **kwargs):
        super(PrimVarCWidget, self).__init__(*args, **kwargs)

        self.setupUi(self)
        self.setFrameStyle(QtGui.QFrame.Panel | QtGui.QFrame.Raised)
        self.mainLayout.setAlignment(QtCore.Qt.AlignTop)


class PrimVarFWidget(QtGui.QFrame, fWidget):
    """

    """
    def __init__(self, *args, **kwargs):
        super(PrimVarFWidget, self).__init__(*args, **kwargs)

        self.setupUi(self)
        self.setFrameStyle(QtGui.QFrame.Panel | QtGui.QFrame.Raised)
        self.mainLayout.setAlignment(QtCore.Qt.AlignTop)
        self.type_int.toggled.connect(self.go_integer)
        self.type_float.toggled.connect(self.go_float)

    def go_integer(self, enabled):
        """ Change the stepping of the spin box, form 0.1 to 1.

        :param enabled: (boolean) if the Integer radio is checked.
        """
        if enabled:
            self.min_value.setSingleStep(1)
            self.max_value.setSingleStep(1)

    def go_float(self, enabled):
        """ Change the stepping of the spin box, form 1 to 0.1.

            :param enabled: (boolean) if the Float radio is checked.
        """

        if enabled:
            self.min_value.setSingleStep(0.1)
            self.max_value.setSingleStep(0.1)


class PrimVarSWidget(QtGui.QFrame, sWidget):
    """

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

    @property
    def existing_labels(self):
        """

        :return:
        """
        return self._existing_labels

    @existing_labels.setter
    def existing_labels(self, value):
        """

        :param value:
        """
        self._existing_labels = value

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
        """
        self._new_strings = value


class PrimVarNWidget(QtGui.QFrame, nWidget):
    """

    """
    def __init__(self, *args, **kwargs):
        super(PrimVarNWidget, self).__init__(*args, **kwargs)

        self.setupUi(self)
        self.setFrameStyle(QtGui.QFrame.Panel | QtGui.QFrame.Raised)
        self.mainLayout.setAlignment(QtCore.Qt.AlignTop)


class PrimVarPWidget(QtGui.QFrame, pWidget):
    """

    """
    def __init__(self, *args, **kwargs):
        super(PrimVarPWidget, self).__init__(*args, **kwargs)

        self.setupUi(self)
        self.setFrameStyle(QtGui.QFrame.Panel | QtGui.QFrame.Raised)
        self.mainLayout.setAlignment(QtCore.Qt.AlignTop)


class PrimVarVWidget(QtGui.QFrame, vWidget):
    """

    """
    def __init__(self, *args, **kwargs):
        super(PrimVarVWidget, self).__init__(*args, **kwargs)

        self.setupUi(self)
        self.setFrameStyle(QtGui.QFrame.Panel | QtGui.QFrame.Raised)
        self.mainLayout.setAlignment(QtCore.Qt.AlignTop)


def create_ui():
    """
    Create an instance of the GUI
    :return: QWidget
    """
    global primVarAppUi

    if not primVarAppUi:
        primVarAppUi = PrimVarApp()

    primVarAppUi.show()


def close_ui():
    """
    Clese the existing Ui
    :return: None
    """
    global primVarAppUi
    if primVarAppUi:
        primVarAppUi.deleteLater()
        primVarAppUi = None


def main():
    """
    If the application is ran in terminal, create a stand alone app and raise
    the window
    :return: QWidget
    """
    global primVarAppUi

    app = QtGui.QApplication(sys.argv)
    primVarAppUi = PrimVarApp()
    primVarAppUi.show()
    primVarAppUi.raise_()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
