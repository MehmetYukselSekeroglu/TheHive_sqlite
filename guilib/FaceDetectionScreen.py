# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'raw_ui_files/FaceDetectionScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FaceDetectionOnly(object):
    def setupUi(self, FaceDetectionOnly):
        FaceDetectionOnly.setObjectName("FaceDetectionOnly")
        FaceDetectionOnly.resize(1288, 482)
        FaceDetectionOnly.setStyleSheet("font: 11pt \"Hack\";")
        self.gridLayout = QtWidgets.QGridLayout(FaceDetectionOnly)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget_tabController = QtWidgets.QTabWidget(FaceDetectionOnly)
        self.tabWidget_tabController.setObjectName("tabWidget_tabController")
        self.tab_1_detectionMain = QtWidgets.QWidget()
        self.tab_1_detectionMain.setObjectName("tab_1_detectionMain")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_1_detectionMain)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.widget_2 = QtWidgets.QWidget(self.tab_1_detectionMain)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.line_2 = QtWidgets.QFrame(self.widget_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_6.addWidget(self.line_2, 0, 0, 2, 3)
        self.line_3 = QtWidgets.QFrame(self.widget_2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_6.addWidget(self.line_3, 3, 0, 1, 3)
        self.line_4 = QtWidgets.QFrame(self.widget_2)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_6.addWidget(self.line_4, 5, 0, 1, 3)
        self.textBrowser_logConsole = QtWidgets.QTextBrowser(self.widget_2)
        self.textBrowser_logConsole.setStyleSheet("font: 11pt \"Hack\";")
        self.textBrowser_logConsole.setObjectName("textBrowser_logConsole")
        self.gridLayout_6.addWidget(self.textBrowser_logConsole, 4, 0, 1, 3)
        self.pushButton_selectImage = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_selectImage.setStyleSheet("font: 11pt \"Hack\";")
        self.pushButton_selectImage.setObjectName("pushButton_selectImage")
        self.gridLayout_6.addWidget(self.pushButton_selectImage, 2, 0, 1, 1)
        self.pushButton_runDetection = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_runDetection.setStyleSheet("font: 11pt \"Hack\";")
        self.pushButton_runDetection.setObjectName("pushButton_runDetection")
        self.gridLayout_6.addWidget(self.pushButton_runDetection, 2, 1, 1, 1)
        self.pushButton_clearLogConsole = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_clearLogConsole.setStyleSheet("font: 11pt \"Hack\";")
        self.pushButton_clearLogConsole.setObjectName("pushButton_clearLogConsole")
        self.gridLayout_6.addWidget(self.pushButton_clearLogConsole, 2, 2, 1, 1)
        self.gridLayout_4.addWidget(self.widget_2, 0, 2, 1, 1)
        self.widget = QtWidgets.QWidget(self.tab_1_detectionMain)
        self.widget.setObjectName("widget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_showImage = QtWidgets.QLabel(self.widget)
        self.label_showImage.setText("")
        self.label_showImage.setObjectName("label_showImage")
        self.gridLayout_5.addWidget(self.label_showImage, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.widget, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.tab_1_detectionMain)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_4.addWidget(self.line, 0, 1, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.tab_1_detectionMain)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_4.addWidget(self.line_5, 0, 3, 1, 1)
        self.tabWidget_tabController.addTab(self.tab_1_detectionMain, "")
        self.tab_2_showAdvancedResults = QtWidgets.QWidget()
        self.tab_2_showAdvancedResults.setObjectName("tab_2_showAdvancedResults")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2_showAdvancedResults)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textBrowser_allDataFromDetections = QtWidgets.QTextBrowser(self.tab_2_showAdvancedResults)
        self.textBrowser_allDataFromDetections.setStyleSheet("font: 12pt \"Hack\";")
        self.textBrowser_allDataFromDetections.setObjectName("textBrowser_allDataFromDetections")
        self.gridLayout_2.addWidget(self.textBrowser_allDataFromDetections, 0, 0, 1, 1)
        self.tabWidget_tabController.addTab(self.tab_2_showAdvancedResults, "")
        self.gridLayout.addWidget(self.tabWidget_tabController, 0, 0, 1, 1)

        self.retranslateUi(FaceDetectionOnly)
        self.tabWidget_tabController.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(FaceDetectionOnly)

    def retranslateUi(self, FaceDetectionOnly):
        _translate = QtCore.QCoreApplication.translate
        FaceDetectionOnly.setWindowTitle(_translate("FaceDetectionOnly", "Form"))
        self.textBrowser_logConsole.setHtml(_translate("FaceDetectionOnly", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Hack\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cantarell\'; font-weight:600;\">LOG CONSOLE:</span></p></body></html>"))
        self.pushButton_selectImage.setText(_translate("FaceDetectionOnly", "Select Image"))
        self.pushButton_runDetection.setText(_translate("FaceDetectionOnly", "Run Detection"))
        self.pushButton_clearLogConsole.setText(_translate("FaceDetectionOnly", "Clear"))
        self.tabWidget_tabController.setTabText(self.tabWidget_tabController.indexOf(self.tab_1_detectionMain), _translate("FaceDetectionOnly", "Detection"))
        self.textBrowser_allDataFromDetections.setHtml(_translate("FaceDetectionOnly", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Hack\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:600;\">SON TESPİTE AİT TÜM VERİLER:</span></p></body></html>"))
        self.tabWidget_tabController.setTabText(self.tabWidget_tabController.indexOf(self.tab_2_showAdvancedResults), _translate("FaceDetectionOnly", "Advanced Results"))
import main_icon_files_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FaceDetectionOnly = QtWidgets.QWidget()
    ui = Ui_FaceDetectionOnly()
    ui.setupUi(FaceDetectionOnly)
    FaceDetectionOnly.show()
    sys.exit(app.exec_())
