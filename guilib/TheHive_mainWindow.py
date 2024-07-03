# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'raw_ui_files/TheHive_mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TheHve_MainWindow(object):
    def setupUi(self, TheHve_MainWindow):
        TheHve_MainWindow.setObjectName("TheHve_MainWindow")
        TheHve_MainWindow.resize(1146, 728)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/mainLogo/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TheHve_MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(TheHve_MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("font: 11pt \"Hack\";")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textBrowser_systemStatus = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_systemStatus.setStyleSheet("font: 14pt \"Hack\";")
        self.textBrowser_systemStatus.setObjectName("textBrowser_systemStatus")
        self.gridLayout_2.addWidget(self.textBrowser_systemStatus, 3, 0, 1, 1)
        self.textBrowser_WelcomeAndToolinfo = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_WelcomeAndToolinfo.setStyleSheet("font: 14pt \"Hack\";")
        self.textBrowser_WelcomeAndToolinfo.setObjectName("textBrowser_WelcomeAndToolinfo")
        self.gridLayout_2.addWidget(self.textBrowser_WelcomeAndToolinfo, 5, 0, 1, 1)
        self.line_coolBar_tab_1 = QtWidgets.QFrame(self.tab)
        self.line_coolBar_tab_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_coolBar_tab_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_coolBar_tab_1.setObjectName("line_coolBar_tab_1")
        self.gridLayout_2.addWidget(self.line_coolBar_tab_1, 4, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        TheHve_MainWindow.setCentralWidget(self.centralwidget)
        self.menubar_menuController = QtWidgets.QMenuBar(TheHve_MainWindow)
        self.menubar_menuController.setGeometry(QtCore.QRect(0, 0, 1146, 24))
        self.menubar_menuController.setObjectName("menubar_menuController")
        self.menuSecurity = QtWidgets.QMenu(self.menubar_menuController)
        self.menuSecurity.setObjectName("menuSecurity")
        self.menuOsintTools = QtWidgets.QMenu(self.menubar_menuController)
        self.menuOsintTools.setObjectName("menuOsintTools")
        self.menuFile_operations = QtWidgets.QMenu(self.menubar_menuController)
        self.menuFile_operations.setObjectName("menuFile_operations")
        self.menuIdentify_Tools = QtWidgets.QMenu(self.menubar_menuController)
        self.menuIdentify_Tools.setObjectName("menuIdentify_Tools")
        self.menuFace_Insight = QtWidgets.QMenu(self.menuIdentify_Tools)
        self.menuFace_Insight.setObjectName("menuFace_Insight")
        self.menuRegion_specific_only = QtWidgets.QMenu(self.menubar_menuController)
        self.menuRegion_specific_only.setObjectName("menuRegion_specific_only")
        self.menuTurkey_Only = QtWidgets.QMenu(self.menuRegion_specific_only)
        self.menuTurkey_Only.setObjectName("menuTurkey_Only")
        self.menuExternel_Madules = QtWidgets.QMenu(self.menubar_menuController)
        self.menuExternel_Madules.setObjectName("menuExternel_Madules")
        self.menuAnalysis = QtWidgets.QMenu(self.menubar_menuController)
        self.menuAnalysis.setObjectName("menuAnalysis")
        TheHve_MainWindow.setMenuBar(self.menubar_menuController)
        self.statusbar = QtWidgets.QStatusBar(TheHve_MainWindow)
        self.statusbar.setObjectName("statusbar")
        TheHve_MainWindow.setStatusBar(self.statusbar)
        self.actionChange_Login_Password = QtWidgets.QAction(TheHve_MainWindow)
        self.actionChange_Login_Password.setObjectName("actionChange_Login_Password")
        self.actioniban_Parser = QtWidgets.QAction(TheHve_MainWindow)
        self.actioniban_Parser.setObjectName("actioniban_Parser")
        self.actionreverse_ip_lookup = QtWidgets.QAction(TheHve_MainWindow)
        self.actionreverse_ip_lookup.setObjectName("actionreverse_ip_lookup")
        self.actionVideo_frame_extractor = QtWidgets.QAction(TheHve_MainWindow)
        self.actionVideo_frame_extractor.setObjectName("actionVideo_frame_extractor")
        self.actionSound_Converter = QtWidgets.QAction(TheHve_MainWindow)
        self.actionSound_Converter.setObjectName("actionSound_Converter")
        self.actionPhone_number_parser = QtWidgets.QAction(TheHve_MainWindow)
        self.actionPhone_number_parser.setObjectName("actionPhone_number_parser")
        self.actionVoice_verification = QtWidgets.QAction(TheHve_MainWindow)
        self.actionVoice_verification.setObjectName("actionVoice_verification")
        self.actionFace_Detection = QtWidgets.QAction(TheHve_MainWindow)
        self.actionFace_Detection.setObjectName("actionFace_Detection")
        self.actionFace_Verification = QtWidgets.QAction(TheHve_MainWindow)
        self.actionFace_Verification.setObjectName("actionFace_Verification")
        self.actionFace_Recognition = QtWidgets.QAction(TheHve_MainWindow)
        self.actionFace_Recognition.setObjectName("actionFace_Recognition")
        self.actionTC_Verification = QtWidgets.QAction(TheHve_MainWindow)
        self.actionTC_Verification.setObjectName("actionTC_Verification")
        self.actionTC_Calculator = QtWidgets.QAction(TheHve_MainWindow)
        self.actionTC_Calculator.setObjectName("actionTC_Calculator")
        self.actionimport_module = QtWidgets.QAction(TheHve_MainWindow)
        self.actionimport_module.setObjectName("actionimport_module")
        self.actionBin_Lookup = QtWidgets.QAction(TheHve_MainWindow)
        self.actionBin_Lookup.setObjectName("actionBin_Lookup")
        self.actionAndroid_Static_Analysis = QtWidgets.QAction(TheHve_MainWindow)
        self.actionAndroid_Static_Analysis.setObjectName("actionAndroid_Static_Analysis")
        self.menuSecurity.addAction(self.actionChange_Login_Password)
        self.menuOsintTools.addAction(self.actioniban_Parser)
        self.menuOsintTools.addAction(self.actionreverse_ip_lookup)
        self.menuOsintTools.addAction(self.actionPhone_number_parser)
        self.menuOsintTools.addAction(self.actionBin_Lookup)
        self.menuFile_operations.addAction(self.actionVideo_frame_extractor)
        self.menuFile_operations.addAction(self.actionSound_Converter)
        self.menuFace_Insight.addAction(self.actionFace_Detection)
        self.menuFace_Insight.addAction(self.actionFace_Verification)
        self.menuFace_Insight.addAction(self.actionFace_Recognition)
        self.menuIdentify_Tools.addAction(self.actionVoice_verification)
        self.menuIdentify_Tools.addAction(self.menuFace_Insight.menuAction())
        self.menuTurkey_Only.addAction(self.actionTC_Verification)
        self.menuTurkey_Only.addAction(self.actionTC_Calculator)
        self.menuRegion_specific_only.addAction(self.menuTurkey_Only.menuAction())
        self.menuExternel_Madules.addAction(self.actionimport_module)
        self.menuAnalysis.addAction(self.actionAndroid_Static_Analysis)
        self.menubar_menuController.addAction(self.menuSecurity.menuAction())
        self.menubar_menuController.addAction(self.menuOsintTools.menuAction())
        self.menubar_menuController.addAction(self.menuFile_operations.menuAction())
        self.menubar_menuController.addAction(self.menuIdentify_Tools.menuAction())
        self.menubar_menuController.addAction(self.menuRegion_specific_only.menuAction())
        self.menubar_menuController.addAction(self.menuExternel_Madules.menuAction())
        self.menubar_menuController.addAction(self.menuAnalysis.menuAction())

        self.retranslateUi(TheHve_MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TheHve_MainWindow)

    def retranslateUi(self, TheHve_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        TheHve_MainWindow.setWindowTitle(_translate("TheHve_MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("TheHve_MainWindow", "Welcome"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("TheHve_MainWindow", "Tab 2"))
        self.menuSecurity.setTitle(_translate("TheHve_MainWindow", "Security"))
        self.menuOsintTools.setTitle(_translate("TheHve_MainWindow", "Osint Tools"))
        self.menuFile_operations.setTitle(_translate("TheHve_MainWindow", "File Operations"))
        self.menuIdentify_Tools.setTitle(_translate("TheHve_MainWindow", "Identify Tools"))
        self.menuFace_Insight.setTitle(_translate("TheHve_MainWindow", "Face Insight"))
        self.menuRegion_specific_only.setTitle(_translate("TheHve_MainWindow", "Region specific only"))
        self.menuTurkey_Only.setTitle(_translate("TheHve_MainWindow", "Türkey Only"))
        self.menuExternel_Madules.setTitle(_translate("TheHve_MainWindow", "Externel Madules"))
        self.menuAnalysis.setTitle(_translate("TheHve_MainWindow", "Analysis"))
        self.actionChange_Login_Password.setText(_translate("TheHve_MainWindow", "Change Login Password"))
        self.actioniban_Parser.setText(_translate("TheHve_MainWindow", "Iban parser"))
        self.actionreverse_ip_lookup.setText(_translate("TheHve_MainWindow", "Reverse ip lookup"))
        self.actionVideo_frame_extractor.setText(_translate("TheHve_MainWindow", "Video frame extractor"))
        self.actionSound_Converter.setText(_translate("TheHve_MainWindow", "Sound Converter"))
        self.actionPhone_number_parser.setText(_translate("TheHve_MainWindow", "Phone number parser"))
        self.actionVoice_verification.setText(_translate("TheHve_MainWindow", "Voice verification"))
        self.actionFace_Detection.setText(_translate("TheHve_MainWindow", "Face Detection ( image file )"))
        self.actionFace_Verification.setText(_translate("TheHve_MainWindow", "Face Verification ( image file )"))
        self.actionFace_Recognition.setText(_translate("TheHve_MainWindow", "Face Recognition ( image file )"))
        self.actionTC_Verification.setText(_translate("TheHve_MainWindow", "TC Verification"))
        self.actionTC_Calculator.setText(_translate("TheHve_MainWindow", "TC Calculator"))
        self.actionimport_module.setText(_translate("TheHve_MainWindow", "import module"))
        self.actionBin_Lookup.setText(_translate("TheHve_MainWindow", "Bin lookup"))
        self.actionAndroid_Static_Analysis.setText(_translate("TheHve_MainWindow", "Android Static Analysis"))
import main_icon_files_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TheHve_MainWindow = QtWidgets.QMainWindow()
    ui = Ui_TheHve_MainWindow()
    ui.setupUi(TheHve_MainWindow)
    TheHve_MainWindow.show()
    sys.exit(app.exec_())
