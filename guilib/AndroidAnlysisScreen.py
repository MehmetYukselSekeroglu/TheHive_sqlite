# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'raw_ui_files/AndroidAnlysisScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AndroidAnlysisWidget(object):
    def setupUi(self, AndroidAnlysisWidget):
        AndroidAnlysisWidget.setObjectName("AndroidAnlysisWidget")
        AndroidAnlysisWidget.resize(1529, 834)
        self.gridLayout = QtWidgets.QGridLayout(AndroidAnlysisWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(AndroidAnlysisWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.tab)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.checkBox_sendVT = QtWidgets.QCheckBox(self.widget_2)
        self.checkBox_sendVT.setObjectName("checkBox_sendVT")
        self.gridLayout_3.addWidget(self.checkBox_sendVT, 2, 5, 1, 1)
        self.pushButton_saveReport = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_saveReport.setObjectName("pushButton_saveReport")
        self.gridLayout_3.addWidget(self.pushButton_saveReport, 2, 2, 1, 1)
        self.pushButton_startAnlysis = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_startAnlysis.setObjectName("pushButton_startAnlysis")
        self.gridLayout_3.addWidget(self.pushButton_startAnlysis, 2, 3, 1, 1)
        self.pushButton_selectFile = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_selectFile.setObjectName("pushButton_selectFile")
        self.gridLayout_3.addWidget(self.pushButton_selectFile, 2, 1, 1, 1)
        self.textBrowser_logConsole = QtWidgets.QTextBrowser(self.widget_2)
        self.textBrowser_logConsole.setStyleSheet("font: 12pt \"Hack\";")
        self.textBrowser_logConsole.setObjectName("textBrowser_logConsole")
        self.gridLayout_3.addWidget(self.textBrowser_logConsole, 5, 0, 1, 7)
        self.line_2 = QtWidgets.QFrame(self.widget_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_3.addWidget(self.line_2, 3, 0, 1, 7)
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 4, 0, 1, 1)
        self.lineEdit_showTargetPath = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_showTargetPath.setObjectName("lineEdit_showTargetPath")
        self.gridLayout_3.addWidget(self.lineEdit_showTargetPath, 1, 1, 1, 5)
        self.pushButton_stopAnlysis = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_stopAnlysis.setObjectName("pushButton_stopAnlysis")
        self.gridLayout_3.addWidget(self.pushButton_stopAnlysis, 2, 4, 1, 1)
        self.label_showApkTemplate = QtWidgets.QLabel(self.widget_2)
        self.label_showApkTemplate.setText("")
        self.label_showApkTemplate.setObjectName("label_showApkTemplate")
        self.gridLayout_3.addWidget(self.label_showApkTemplate, 0, 6, 3, 1)
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 1, 1, 2)
        self.gridLayout_2.addWidget(self.widget_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setMaximumSize(QtCore.QSize(16777215, 21))
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(AndroidAnlysisWidget)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AndroidAnlysisWidget)

    def retranslateUi(self, AndroidAnlysisWidget):
        _translate = QtCore.QCoreApplication.translate
        AndroidAnlysisWidget.setWindowTitle(_translate("AndroidAnlysisWidget", "Form"))
        self.checkBox_sendVT.setText(_translate("AndroidAnlysisWidget", "Send to VirusTotal"))
        self.pushButton_saveReport.setText(_translate("AndroidAnlysisWidget", "Save Report"))
        self.pushButton_startAnlysis.setText(_translate("AndroidAnlysisWidget", "Start Anlysis"))
        self.pushButton_selectFile.setText(_translate("AndroidAnlysisWidget", "Select File"))
        self.label_3.setText(_translate("AndroidAnlysisWidget", "Result & Log Console:"))
        self.pushButton_stopAnlysis.setText(_translate("AndroidAnlysisWidget", "Stop Anlysis"))
        self.label_2.setText(_translate("AndroidAnlysisWidget", "Target File:"))
        self.label.setText(_translate("AndroidAnlysisWidget", "<html><head/><body><p align=\"center\">Android Anlysis Toolkit</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("AndroidAnlysisWidget", "Anlysis Page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("AndroidAnlysisWidget", "Tech Information"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AndroidAnlysisWidget = QtWidgets.QWidget()
    ui = Ui_AndroidAnlysisWidget()
    ui.setupUi(AndroidAnlysisWidget)
    AndroidAnlysisWidget.show()
    sys.exit(app.exec_())
