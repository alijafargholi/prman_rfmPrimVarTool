# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/rmanSwidget.ui'
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
        Form.resize(550, 249)
        self.mainLayout = QtGui.QVBoxLayout(Form)
        # self.mainLayout.setMargin(0)
        self.mainLayout.setSpacing(1)
        self.mainLayout.setObjectName(_fromUtf8("mainLayout"))
        self.frame = QtGui.QFrame(Form)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        # self.verticalLayout.setMargin(2)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.delete_this = QtGui.QPushButton(self.frame)
        self.delete_this.setMinimumSize(QtCore.QSize(25, 25))
        self.delete_this.setMaximumSize(QtCore.QSize(25, 25))
        self.delete_this.setText(_fromUtf8(""))
        self.delete_this.setObjectName(_fromUtf8("delete_this"))
        self.verticalLayout.addWidget(self.delete_this)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.attr_name = QtGui.QLineEdit(self.frame)
        self.attr_name.setMaximumSize(QtCore.QSize(270, 16777215))
        self.attr_name.setObjectName(_fromUtf8("attr_name"))
        self.horizontalLayout.addWidget(self.attr_name)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_3.addWidget(self.label_5)
        self.file_node_name = QtGui.QLineEdit(self.frame)
        self.file_node_name.setMinimumSize(QtCore.QSize(110, 0))
        self.file_node_name.setObjectName(_fromUtf8("file_node_name"))
        self.horizontalLayout_3.addWidget(self.file_node_name)
        self.get_node_name = QtGui.QPushButton(self.frame)
        self.get_node_name.setObjectName(_fromUtf8("get_node_name"))
        self.horizontalLayout_3.addWidget(self.get_node_name)
        self.create_node = QtGui.QPushButton(self.frame)
        self.create_node.setObjectName(_fromUtf8("create_node"))
        self.horizontalLayout_3.addWidget(self.create_node)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.clear_files = QtGui.QPushButton(self.frame)
        self.clear_files.setObjectName(_fromUtf8("clear_files"))
        self.horizontalLayout_2.addWidget(self.clear_files)
        self.gather_files = QtGui.QPushButton(self.frame)
        self.gather_files.setObjectName(_fromUtf8("gather_files"))
        self.horizontalLayout_2.addWidget(self.gather_files)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.scrollArea = QtGui.QScrollArea(self.frame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 534, 134))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.stringListLayout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        # self.stringListLayout.setMargin(1)
        self.stringListLayout.setObjectName(_fromUtf8("stringListLayout"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.mainLayout.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Attribute Name:", None))
        self.label_5.setText(_translate("Form", "TextureFile Node Name:", None))
        self.get_node_name.setText(_translate("Form", "Get it", None))
        self.create_node.setText(_translate("Form", "Create Texture File Node", None))
        self.clear_files.setText(_translate("Form", "Clear", None))
        self.gather_files.setText(_translate("Form", "Gather FIles", None))

