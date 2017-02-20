# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/rmanFwidget.ui'
#
# Created by: PySide UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from Qt import QtWidgets as QtGui
from Qt import QtCore

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(531, 130)
        Form.setMaximumSize(QtCore.QSize(16777215, 130))
        self.mainLayout = QtGui.QVBoxLayout(Form)
        # self.mainLayout.setMargin(1)
        self.mainLayout.setObjectName(_fromUtf8("mainLayout"))
        self.delete_this = QtGui.QPushButton(Form)
        self.delete_this.setMinimumSize(QtCore.QSize(25, 25))
        self.delete_this.setMaximumSize(QtCore.QSize(25, 25))
        self.delete_this.setText(_fromUtf8(""))
        self.delete_this.setObjectName(_fromUtf8("delete_this"))
        self.mainLayout.addWidget(self.delete_this)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.attr_name = QtGui.QLineEdit(Form)
        self.attr_name.setMaximumSize(QtCore.QSize(270, 16777215))
        self.attr_name.setObjectName(_fromUtf8("attr_name"))
        self.horizontalLayout.addWidget(self.attr_name)
        self.mainLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.type_float = QtGui.QRadioButton(Form)
        self.type_float.setChecked(True)
        self.type_float.setObjectName(_fromUtf8("type_float"))
        self.horizontalLayout_3.addWidget(self.type_float)
        self.type_int = QtGui.QRadioButton(Form)
        self.type_int.setObjectName(_fromUtf8("type_int"))
        self.horizontalLayout_3.addWidget(self.type_int)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.min_value = QtGui.QDoubleSpinBox(Form)
        self.min_value.setMinimum(-10000.0)
        self.min_value.setSingleStep(0.1)
        self.min_value.setObjectName(_fromUtf8("min_value"))
        self.horizontalLayout_3.addWidget(self.min_value)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.max_value = QtGui.QDoubleSpinBox(Form)
        self.max_value.setMinimum(-100000000.0)
        self.max_value.setMaximum(99990000.0)
        self.max_value.setSingleStep(0.1)
        self.max_value.setProperty("value", 1.0)
        self.max_value.setObjectName(_fromUtf8("max_value"))
        self.horizontalLayout_3.addWidget(self.max_value)
        self.mainLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_2.addWidget(self.label_5)
        self.primvar_node_name = QtGui.QLineEdit(Form)
        self.primvar_node_name.setMinimumSize(QtCore.QSize(110, 0))
        self.primvar_node_name.setObjectName(_fromUtf8("primvar_node_name"))
        self.horizontalLayout_2.addWidget(self.primvar_node_name)
        self.get_node_name = QtGui.QPushButton(Form)
        self.get_node_name.setObjectName(_fromUtf8("get_node_name"))
        self.horizontalLayout_2.addWidget(self.get_node_name)
        self.create_node = QtGui.QPushButton(Form)
        self.create_node.setObjectName(_fromUtf8("create_node"))
        self.horizontalLayout_2.addWidget(self.create_node)
        self.mainLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Attribute Name:", None))
        self.label_2.setText(_translate("Form", "Value Type:", None))
        self.type_float.setText(_translate("Form", "Float", None))
        self.type_int.setText(_translate("Form", "Integer", None))
        self.label_3.setText(_translate("Form", "Min:", None))
        self.label_4.setText(_translate("Form", "Max:", None))
        self.label_5.setText(_translate("Form", "PrimVar Node Name:", None))
        self.get_node_name.setText(_translate("Form", "Get it", None))
        self.create_node.setText(_translate("Form", "Create PrimVar Node", None))

