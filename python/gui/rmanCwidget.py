# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/rmanCwidget.ui'
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
        Form.resize(498, 248)
        Form.setMaximumSize(QtCore.QSize(16777215, 250))
        self.mainLayout = QtGui.QVBoxLayout(Form)
        # self.mainLayout.setMargin(1)
        self.mainLayout.setObjectName(_fromUtf8("mainLayout"))
        self.delete_this = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.delete_this.sizePolicy().hasHeightForWidth())
        self.delete_this.setSizePolicy(sizePolicy)
        self.delete_this.setMinimumSize(QtCore.QSize(20, 20))
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
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.random_color = QtGui.QRadioButton(Form)
        self.random_color.setChecked(True)
        self.random_color.setObjectName(_fromUtf8("random_color"))
        self.gridLayout.addWidget(self.random_color, 0, 1, 1, 1)
        self.random_color_shades = QtGui.QRadioButton(Form)
        self.random_color_shades.setObjectName(_fromUtf8("random_color_shades"))
        self.gridLayout.addWidget(self.random_color_shades, 1, 1, 1, 1)
        self.random_grayscale = QtGui.QRadioButton(Form)
        self.random_grayscale.setObjectName(_fromUtf8("random_grayscale"))
        self.gridLayout.addWidget(self.random_grayscale, 2, 1, 1, 1)
        self.color_picker = QtGui.QPushButton(Form)
        self.color_picker.setText(_fromUtf8(""))
        self.color_picker.setObjectName(_fromUtf8("color_picker"))
        self.gridLayout.addWidget(self.color_picker, 1, 2, 1, 1)
        self.mainLayout.addLayout(self.gridLayout)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.min_s_value = QtGui.QDoubleSpinBox(Form)
        self.min_s_value.setSingleStep(0.1)
        self.min_s_value.setObjectName(_fromUtf8("min_s_value"))
        self.gridLayout_2.addWidget(self.min_s_value, 0, 1, 1, 1)
        self.max_s_value = QtGui.QDoubleSpinBox(Form)
        self.max_s_value.setSingleStep(0.1)
        self.max_s_value.setProperty("value", 1.0)
        self.max_s_value.setObjectName(_fromUtf8("max_s_value"))
        self.gridLayout_2.addWidget(self.max_s_value, 0, 2, 1, 1)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.min_b_value = QtGui.QDoubleSpinBox(Form)
        self.min_b_value.setSingleStep(0.1)
        self.min_b_value.setObjectName(_fromUtf8("min_b_value"))
        self.gridLayout_2.addWidget(self.min_b_value, 1, 1, 1, 1)
        self.max_b_value = QtGui.QDoubleSpinBox(Form)
        self.max_b_value.setSingleStep(0.1)
        self.max_b_value.setProperty("value", 1.0)
        self.max_b_value.setObjectName(_fromUtf8("max_b_value"))
        self.gridLayout_2.addWidget(self.max_b_value, 1, 2, 1, 1)
        self.mainLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
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
        self.delete_this.setText(_translate("Form", "X", None))
        self.label.setText(_translate("Form", "Attribute Name:", None))
        self.label_2.setText(_translate("Form", "Color Type:", None))
        self.random_color.setText(_translate("Form", "Random Color", None))
        self.random_color_shades.setText(_translate("Form", "Random Shade of Color", None))
        self.random_grayscale.setText(_translate("Form", "Random Grayscale", None))
        self.label_3.setText(_translate("Form", "Min/Max Saturation:", None))
        self.label_4.setText(_translate("Form", "Min/Max Brightness:", None))
        self.label_5.setText(_translate("Form", "PrimVar Node Name:", None))
        self.get_node_name.setText(_translate("Form", "Get it", None))
        self.create_node.setText(_translate("Form", "Create PrimVar Node", None))

