# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\really-not-useless-assistant\client_apps\gui\form.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(412, 311)
        Form.setStyleSheet("QWidget {\n"
"background: #f6f6f6;\n"
"}\n"
"\n"
"*[cssClass=\"section-title\"] {\n"
"font-size: 12px;\n"
"font-weight: bold;\n"
"color: brown;\n"
"}\n"
"\n"
"QLabel[cssCalss=\"label-stopped\"] {\n"
"color: red;\n"
"}\n"
"QLabel[cssCalss=\"label-started\"] {\n"
"color: green;\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_Main = QtWidgets.QGridLayout()
        self.gridLayout_Main.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_Main.setObjectName("gridLayout_Main")
        self.verticalLayout_Header = QtWidgets.QVBoxLayout()
        self.verticalLayout_Header.setObjectName("verticalLayout_Header")
        self.label_AppName = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_AppName.setFont(font)
        self.label_AppName.setStyleSheet("color: rgb(195, 82, 25);\n"
"font-size: 20px;")
        self.label_AppName.setObjectName("label_AppName")
        self.verticalLayout_Header.addWidget(self.label_AppName)
        self.label = QtWidgets.QLabel(Form)
        self.label.setStyleSheet("color: darkgrey")
        self.label.setObjectName("label")
        self.verticalLayout_Header.addWidget(self.label)
        self.gridLayout_Main.addLayout(self.verticalLayout_Header, 0, 0, 1, 1)
        self.verticalLayout_Body = QtWidgets.QVBoxLayout()
        self.verticalLayout_Body.setObjectName("verticalLayout_Body")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_3.setObjectName("label_3")
        self.verticalLayout_Body.addWidget(self.label_3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.label_VoiceListenerStatus = QtWidgets.QLabel(Form)
        self.label_VoiceListenerStatus.setObjectName("label_VoiceListenerStatus")
        self.horizontalLayout_5.addWidget(self.label_VoiceListenerStatus)
        self.horizontalLayout_5.setStretch(1, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.button_VoiceListenerStart = QtWidgets.QPushButton(Form)
        self.button_VoiceListenerStart.setStyleSheet("")
        self.button_VoiceListenerStart.setObjectName("button_VoiceListenerStart")
        self.horizontalLayout_6.addWidget(self.button_VoiceListenerStart)
        self.button_VoiceListenerStop = QtWidgets.QPushButton(Form)
        self.button_VoiceListenerStop.setObjectName("button_VoiceListenerStop")
        self.horizontalLayout_6.addWidget(self.button_VoiceListenerStop)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.verticalLayout_Body.addLayout(self.verticalLayout_3)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_Body.addWidget(self.label_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.label_VoiceSynthesisStatus = QtWidgets.QLabel(Form)
        self.label_VoiceSynthesisStatus.setObjectName("label_labelVoiceSynthesisStatus")
        self.horizontalLayout_2.addWidget(self.label_VoiceSynthesisStatus)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_VoiceSynthesisStart = QtWidgets.QPushButton(Form)
        self.button_VoiceSynthesisStart.setObjectName("button_VoiceSynthesisStart")
        self.horizontalLayout.addWidget(self.button_VoiceSynthesisStart)
        self.button_VoiceSynthesisStop = QtWidgets.QPushButton(Form)
        self.button_VoiceSynthesisStop.setObjectName("button_VoiceSynthesisStop")
        self.horizontalLayout.addWidget(self.button_VoiceSynthesisStop)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_Body.addLayout(self.verticalLayout)
        self.gridLayout_Main.addLayout(self.verticalLayout_Body, 1, 0, 1, 1)
        self.gridLayout_Main.setRowStretch(1, 1)
        self.gridLayout.addLayout(self.gridLayout_Main, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "RNU-Assistant"))
        self.label_AppName.setText(_translate("Form", "RNU-Assistant"))
        self.label.setText(_translate("Form", "Device control panel"))
        self.label_3.setText(_translate("Form", "Voice listener"))
        self.label_3.setProperty("cssClass", _translate("Form", "section-title"))
        self.label_8.setText(_translate("Form", "Status:"))
        self.label_VoiceListenerStatus.setText(_translate("Form", "Stopped"))
        self.label_VoiceListenerStatus.setProperty("cssClass", _translate("Form", "label-stopped"))
        self.button_VoiceListenerStart.setText(_translate("Form", "Start"))
        self.button_VoiceListenerStop.setText(_translate("Form", "Stop"))
        self.label_2.setText(_translate("Form", "Voice synthesis"))
        self.label_2.setProperty("cssClass", _translate("Form", "section-title"))
        self.label_4.setText(_translate("Form", "Status:"))
        self.label_VoiceSynthesisStatus.setText(_translate("Form", "Stopped"))
        self.label_VoiceSynthesisStatus.setProperty("cssClass", _translate("Form", "label-stopped"))
        self.button_VoiceSynthesisStart.setText(_translate("Form", "Start"))
        self.button_VoiceSynthesisStop.setText(_translate("Form", "Stop"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
