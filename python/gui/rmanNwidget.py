# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/rmanNwidget.ui'
#
# Created by: PySide UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

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
        Form.resize(498, 181)
        Form.setMaximumSize(QtCore.QSize(16777215, 195))
        self.mainLayout = QtGui.QVBoxLayout(Form)
        # self.mainLayout.setMargin(2)
        self.mainLayout.setSpacing(2)
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
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.min_x_value = QtGui.QDoubleSpinBox(Form)
        self.min_x_value.setSingleStep(0.1)
        self.min_x_value.setObjectName(_fromUtf8("min_x_value"))
        self.horizontalLayout_3.addWidget(self.min_x_value)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_3.addWidget(self.label_7)
        self.min_y_value = QtGui.QDoubleSpinBox(Form)
        self.min_y_value.setSingleStep(0.1)
        self.min_y_value.setObjectName(_fromUtf8("min_y_value"))
        self.horizontalLayout_3.addWidget(self.min_y_value)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.label_8 = QtGui.QLabel(Form)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_3.addWidget(self.label_8)
        self.min_z_value = QtGui.QDoubleSpinBox(Form)
        self.min_z_value.setSingleStep(0.1)
        self.min_z_value.setObjectName(_fromUtf8("min_z_value"))
        self.horizontalLayout_3.addWidget(self.min_z_value)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 1, 1, 1)
        self.label_10 = QtGui.QLabel(Form)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.variation = QtGui.QRadioButton(Form)
        self.variation.setChecked(True)
        self.variation.setObjectName(_fromUtf8("variation"))
        self.horizontalLayout_5.addWidget(self.variation)
        self.uniform = QtGui.QRadioButton(Form)
        self.uniform.setObjectName(_fromUtf8("uniform"))
        self.horizontalLayout_5.addWidget(self.uniform)
        self.type = QtGui.QComboBox(Form)
        self.type.setObjectName(_fromUtf8("type"))
        self.type.addItem(_fromUtf8(""))
        self.type.addItem(_fromUtf8(""))
        self.horizontalLayout_5.addWidget(self.type)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.max_x_value = QtGui.QDoubleSpinBox(Form)
        self.max_x_value.setSingleStep(0.1)
        self.max_x_value.setProperty("value", 1.0)
        self.max_x_value.setObjectName(_fromUtf8("max_x_value"))
        self.horizontalLayout_4.addWidget(self.max_x_value)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_4.addWidget(self.label_6)
        self.max_y_value = QtGui.QDoubleSpinBox(Form)
        self.max_y_value.setSingleStep(0.1)
        self.max_y_value.setProperty("value", 1.0)
        self.max_y_value.setObjectName(_fromUtf8("max_y_value"))
        self.horizontalLayout_4.addWidget(self.max_y_value)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.label_9 = QtGui.QLabel(Form)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_4.addWidget(self.label_9)
        self.max_z_value = QtGui.QDoubleSpinBox(Form)
        self.max_z_value.setSingleStep(0.1)
        self.max_z_value.setProperty("value", 1.0)
        self.max_z_value.setObjectName(_fromUtf8("max_z_value"))
        self.horizontalLayout_4.addWidget(self.max_z_value)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 1, 1, 1)
        self.mainLayout.addLayout(self.gridLayout)
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
        self.label_3.setText(_translate("Form", "X min:", None))
        self.label_7.setText(_translate("Form", "Y min:", None))
        self.label_8.setText(_translate("Form", "Z min:", None))
        self.label_10.setText(_translate("Form", "Result Type:", None))
        self.variation.setText(_translate("Form", "Variant", None))
        self.uniform.setText(_translate("Form", "Uniform", None))
        self.type.setItemText(0, _translate("Form", "float", None))
        self.type.setItemText(1, _translate("Form", "integer", None))
        self.label_2.setText(_translate("Form", "Value Range:", None))
        self.label_4.setText(_translate("Form", "X Max:", None))
        self.label_6.setText(_translate("Form", "Y Max:", None))
        self.label_9.setText(_translate("Form", "Z Max:", None))
        self.label_5.setText(_translate("Form", "PrimVar Node Name:", None))
        self.get_node_name.setText(_translate("Form", "Get it", None))
        self.create_node.setText(_translate("Form", "Create PrimVar Node", None))

