# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'raw_ui_files/HtsAnalaysisScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HTSanalaysis(object):
    def setupUi(self, HTSanalaysis):
        HTSanalaysis.setObjectName("HTSanalaysis")
        HTSanalaysis.resize(868, 642)
        self.gridLayout_2 = QtWidgets.QGridLayout(HTSanalaysis)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(HTSanalaysis)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1_general = QtWidgets.QWidget()
        self.tab_1_general.setObjectName("tab_1_general")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_1_general)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget = QtWidgets.QWidget(self.tab_1_general)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.textBrowser_targetFileSize = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_targetFileSize.setMinimumSize(QtCore.QSize(550, 31))
        self.textBrowser_targetFileSize.setMaximumSize(QtCore.QSize(550, 31))
        self.textBrowser_targetFileSize.setObjectName("textBrowser_targetFileSize")
        self.gridLayout.addWidget(self.textBrowser_targetFileSize, 1, 1, 1, 1)
        self.pushButton_selectFile = QtWidgets.QPushButton(self.widget)
        self.pushButton_selectFile.setObjectName("pushButton_selectFile")
        self.gridLayout.addWidget(self.pushButton_selectFile, 0, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.pushButton_stopAnalays = QtWidgets.QPushButton(self.widget)
        self.pushButton_stopAnalays.setObjectName("pushButton_stopAnalays")
        self.gridLayout.addWidget(self.pushButton_stopAnalays, 2, 3, 1, 1)
        self.textBrowser_targetFilePathShow = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_targetFilePathShow.setMinimumSize(QtCore.QSize(550, 31))
        self.textBrowser_targetFilePathShow.setMaximumSize(QtCore.QSize(550, 31))
        self.textBrowser_targetFilePathShow.setObjectName("textBrowser_targetFilePathShow")
        self.gridLayout.addWidget(self.textBrowser_targetFilePathShow, 0, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 2, 4, 1)
        self.pushButton_startAnalays = QtWidgets.QPushButton(self.widget)
        self.pushButton_startAnalays.setObjectName("pushButton_startAnalays")
        self.gridLayout.addWidget(self.pushButton_startAnalays, 1, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.textBrowser_targetFileFormatStatus = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_targetFileFormatStatus.setMinimumSize(QtCore.QSize(550, 31))
        self.textBrowser_targetFileFormatStatus.setMaximumSize(QtCore.QSize(550, 31))
        self.textBrowser_targetFileFormatStatus.setObjectName("textBrowser_targetFileFormatStatus")
        self.gridLayout.addWidget(self.textBrowser_targetFileFormatStatus, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 1, 1, 1)
        self.textBrowser_targetFileSha1Hash = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_targetFileSha1Hash.setMinimumSize(QtCore.QSize(550, 31))
        self.textBrowser_targetFileSha1Hash.setMaximumSize(QtCore.QSize(550, 31))
        self.textBrowser_targetFileSha1Hash.setObjectName("textBrowser_targetFileSha1Hash")
        self.gridLayout.addWidget(self.textBrowser_targetFileSha1Hash, 3, 1, 1, 1)
        self.pushButton_clearAll = QtWidgets.QPushButton(self.widget)
        self.pushButton_clearAll.setObjectName("pushButton_clearAll")
        self.gridLayout.addWidget(self.pushButton_clearAll, 3, 3, 1, 1)
        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)
        self.textBrowser_logConsole_tab1 = QtWidgets.QTextBrowser(self.tab_1_general)
        self.textBrowser_logConsole_tab1.setMinimumSize(QtCore.QSize(0, 381))
        self.textBrowser_logConsole_tab1.setObjectName("textBrowser_logConsole_tab1")
        self.gridLayout_3.addWidget(self.textBrowser_logConsole_tab1, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_1_general, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(HTSanalaysis)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(HTSanalaysis)

    def retranslateUi(self, HTSanalaysis):
        _translate = QtCore.QCoreApplication.translate
        HTSanalaysis.setWindowTitle(_translate("HTSanalaysis", "Form"))
        self.label.setText(_translate("HTSanalaysis", "Dosya Yolu:"))
        self.pushButton_selectFile.setText(_translate("HTSanalaysis", "Dosya Seç"))
        self.label_2.setText(_translate("HTSanalaysis", "Boyutu:"))
        self.pushButton_stopAnalays.setText(_translate("HTSanalaysis", "Analizi Durdur"))
        self.pushButton_startAnalays.setText(_translate("HTSanalaysis", "Analizi Başlat"))
        self.label_4.setText(_translate("HTSanalaysis", "sha1 has\'i"))
        self.label_3.setText(_translate("HTSanalaysis", "Formatı:"))
        self.pushButton_clearAll.setText(_translate("HTSanalaysis", "Temizle"))
        self.textBrowser_logConsole_tab1.setHtml(_translate("HTSanalaysis", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">LOG CONSOLE:</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1_general), _translate("HTSanalaysis", "Dosya Bilgileri"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("HTSanalaysis", "Analiz Ekranı"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("HTSanalaysis", "Harita Ekranı"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HTSanalaysis = QtWidgets.QWidget()
    ui = Ui_HTSanalaysis()
    ui.setupUi(HTSanalaysis)
    HTSanalaysis.show()
    sys.exit(app.exec_())
