# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WiSSCI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(875, 654)
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/mechanical-arm.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(30, 30))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(330, 10, 511, 591))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.tabWidget.setPalette(palette)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.Configure_Tab = QtWidgets.QWidget()
        self.Configure_Tab.setObjectName("Configure_Tab")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.Configure_Tab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 481, 471))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.DecodeGrid = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.DecodeGrid.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.DecodeGrid.setContentsMargins(0, 0, 0, 0)
        self.DecodeGrid.setObjectName("DecodeGrid")
        self.Regressor_Combo = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Regressor_Combo.setFont(font)
        self.Regressor_Combo.setObjectName("Regressor_Combo")
        self.Regressor_Combo.addItem("")
        self.DecodeGrid.addWidget(self.Regressor_Combo, 2, 1, 1, 1)
        self.ApplyConfig_Button = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.ApplyConfig_Button.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ApplyConfig_Button.setFont(font)
        self.ApplyConfig_Button.setObjectName("ApplyConfig_Button")
        self.DecodeGrid.addWidget(self.ApplyConfig_Button, 7, 0, 1, 1)
        self.Class_Nums_Line = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Class_Nums_Line.setFont(font)
        self.Class_Nums_Line.setObjectName("Class_Nums_Line")
        self.DecodeGrid.addWidget(self.Class_Nums_Line, 4, 1, 1, 1)
        self.Classifier_Combo = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Classifier_Combo.setFont(font)
        self.Classifier_Combo.setObjectName("Classifier_Combo")
        self.Classifier_Combo.addItem("")
        self.DecodeGrid.addWidget(self.Classifier_Combo, 3, 1, 1, 1)
        self.MAV_Sum_Label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.MAV_Sum_Label.setMinimumSize(QtCore.QSize(0, 40))
        self.MAV_Sum_Label.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.MAV_Sum_Label.setFont(font)
        self.MAV_Sum_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.MAV_Sum_Label.setObjectName("MAV_Sum_Label")
        self.DecodeGrid.addWidget(self.MAV_Sum_Label, 5, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.Parameters_Button = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.Parameters_Button.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Parameters_Button.setFont(font)
        self.Parameters_Button.setObjectName("Parameters_Button")
        self.DecodeGrid.addWidget(self.Parameters_Button, 6, 1, 1, 1)
        self.Classifier_Label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.Classifier_Label.setMinimumSize(QtCore.QSize(0, 40))
        self.Classifier_Label.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Classifier_Label.setFont(font)
        self.Classifier_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Classifier_Label.setObjectName("Classifier_Label")
        self.DecodeGrid.addWidget(self.Classifier_Label, 3, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.Hand_Mode_Label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.Hand_Mode_Label.setMinimumSize(QtCore.QSize(0, 40))
        self.Hand_Mode_Label.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Hand_Mode_Label.setFont(font)
        self.Hand_Mode_Label.setObjectName("Hand_Mode_Label")
        self.DecodeGrid.addWidget(self.Hand_Mode_Label, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.Parameters_Label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.Parameters_Label.setMinimumSize(QtCore.QSize(0, 40))
        self.Parameters_Label.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Parameters_Label.setFont(font)
        self.Parameters_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Parameters_Label.setObjectName("Parameters_Label")
        self.DecodeGrid.addWidget(self.Parameters_Label, 6, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.Hand_Mode_Combo = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Hand_Mode_Combo.setFont(font)
        self.Hand_Mode_Combo.setObjectName("Hand_Mode_Combo")
        self.Hand_Mode_Combo.addItem("")
        self.DecodeGrid.addWidget(self.Hand_Mode_Combo, 0, 1, 1, 1)
        self.Wrist_Label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.Wrist_Label.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Wrist_Label.setFont(font)
        self.Wrist_Label.setObjectName("Wrist_Label")
        self.DecodeGrid.addWidget(self.Wrist_Label, 1, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.Wrist_Combo = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Wrist_Combo.sizePolicy().hasHeightForWidth())
        self.Wrist_Combo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Wrist_Combo.setFont(font)
        self.Wrist_Combo.setObjectName("Wrist_Combo")
        self.Wrist_Combo.addItem("")
        self.DecodeGrid.addWidget(self.Wrist_Combo, 1, 1, 1, 1)
        self.MAV_Sum_Line = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.MAV_Sum_Line.setFont(font)
        self.MAV_Sum_Line.setObjectName("MAV_Sum_Line")
        self.DecodeGrid.addWidget(self.MAV_Sum_Line, 5, 1, 1, 1)
        self.Regressor_Label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.Regressor_Label.setMinimumSize(QtCore.QSize(0, 40))
        self.Regressor_Label.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Regressor_Label.setFont(font)
        self.Regressor_Label.setObjectName("Regressor_Label")
        self.DecodeGrid.addWidget(self.Regressor_Label, 2, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.Class_Nums_Label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.Class_Nums_Label.setMinimumSize(QtCore.QSize(0, 40))
        self.Class_Nums_Label.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Class_Nums_Label.setFont(font)
        self.Class_Nums_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Class_Nums_Label.setObjectName("Class_Nums_Label")
        self.DecodeGrid.addWidget(self.Class_Nums_Label, 4, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.ParamsFile_Label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.ParamsFile_Label.setFont(font)
        self.ParamsFile_Label.setScaledContents(True)
        self.ParamsFile_Label.setWordWrap(True)
        self.ParamsFile_Label.setObjectName("ParamsFile_Label")
        self.DecodeGrid.addWidget(self.ParamsFile_Label, 7, 1, 1, 1)
        self.Hand_Mode_Label.raise_()
        self.Hand_Mode_Combo.raise_()
        self.Wrist_Label.raise_()
        self.Regressor_Label.raise_()
        self.Wrist_Combo.raise_()
        self.Classifier_Label.raise_()
        self.Classifier_Combo.raise_()
        self.Regressor_Combo.raise_()
        self.Parameters_Label.raise_()
        self.Parameters_Button.raise_()
        self.Class_Nums_Line.raise_()
        self.Class_Nums_Label.raise_()
        self.MAV_Sum_Label.raise_()
        self.MAV_Sum_Line.raise_()
        self.ApplyConfig_Button.raise_()
        self.ParamsFile_Label.raise_()
        self.tabWidget.addTab(self.Configure_Tab, "")
        self.NomadTab = QtWidgets.QWidget()
        self.NomadTab.setObjectName("NomadTab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.NomadTab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 501, 561))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.Plot_Layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.Plot_Layout.setContentsMargins(0, 0, 0, 0)
        self.Plot_Layout.setObjectName("Plot_Layout")
        self.Ch01_Plot = PlotWidget(self.verticalLayoutWidget)
        self.Ch01_Plot.setObjectName("Ch01_Plot")
        self.Plot_Layout.addWidget(self.Ch01_Plot)
        self.Ch02_Plot = PlotWidget(self.verticalLayoutWidget)
        self.Ch02_Plot.setObjectName("Ch02_Plot")
        self.Plot_Layout.addWidget(self.Ch02_Plot)
        self.Ch03_Plot = PlotWidget(self.verticalLayoutWidget)
        self.Ch03_Plot.setObjectName("Ch03_Plot")
        self.Plot_Layout.addWidget(self.Ch03_Plot)
        self.Ch04_Plot = PlotWidget(self.verticalLayoutWidget)
        self.Ch04_Plot.setObjectName("Ch04_Plot")
        self.Plot_Layout.addWidget(self.Ch04_Plot)
        self.Ch05_Plot = PlotWidget(self.verticalLayoutWidget)
        self.Ch05_Plot.setObjectName("Ch05_Plot")
        self.Plot_Layout.addWidget(self.Ch05_Plot)
        self.Ch06_Plot = PlotWidget(self.verticalLayoutWidget)
        self.Ch06_Plot.setObjectName("Ch06_Plot")
        self.Plot_Layout.addWidget(self.Ch06_Plot)
        self.Ch07_Plot = PlotWidget(self.verticalLayoutWidget)
        self.Ch07_Plot.setObjectName("Ch07_Plot")
        self.Plot_Layout.addWidget(self.Ch07_Plot)
        self.Ch08_Plot = PlotWidget(self.verticalLayoutWidget)
        self.Ch08_Plot.setObjectName("Ch08_Plot")
        self.Plot_Layout.addWidget(self.Ch08_Plot)
        self.Ch09_Plot = PlotWidget(self.verticalLayoutWidget)
        self.Ch09_Plot.setObjectName("Ch09_Plot")
        self.Plot_Layout.addWidget(self.Ch09_Plot)
        self.Ch10_Plot = PlotWidget(self.verticalLayoutWidget)
        self.Ch10_Plot.setObjectName("Ch10_Plot")
        self.Plot_Layout.addWidget(self.Ch10_Plot)
        self.Ch11_Plot = PlotWidget(self.verticalLayoutWidget)
        self.Ch11_Plot.setObjectName("Ch11_Plot")
        self.Plot_Layout.addWidget(self.Ch11_Plot)
        self.Ch12_Plot = PlotWidget(self.verticalLayoutWidget)
        self.Ch12_Plot.setObjectName("Ch12_Plot")
        self.Plot_Layout.addWidget(self.Ch12_Plot)
        self.tabWidget.addTab(self.NomadTab, "")
        self.DecodeTab = QtWidgets.QWidget()
        self.DecodeTab.setObjectName("DecodeTab")
        self.Recvd_WiSSCI_text = QtWidgets.QTextBrowser(self.DecodeTab)
        self.Recvd_WiSSCI_text.setGeometry(QtCore.QRect(0, 0, 501, 561))
        self.Recvd_WiSSCI_text.setObjectName("Recvd_WiSSCI_text")
        self.tabWidget.addTab(self.DecodeTab, "")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 312, 161))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.StatusGrid = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.StatusGrid.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.StatusGrid.setContentsMargins(0, 0, 0, 0)
        self.StatusGrid.setObjectName("StatusGrid")
        self.ConnectBT_Button = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ConnectBT_Button.sizePolicy().hasHeightForWidth())
        self.ConnectBT_Button.setSizePolicy(sizePolicy)
        self.ConnectBT_Button.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ConnectBT_Button.setFont(font)
        self.ConnectBT_Button.setObjectName("ConnectBT_Button")
        self.StatusGrid.addWidget(self.ConnectBT_Button, 1, 0, 1, 1)
        self.BTStatus_LED = QtWidgets.QLabel(self.gridLayoutWidget)
        self.BTStatus_LED.setMaximumSize(QtCore.QSize(60, 60))
        self.BTStatus_LED.setText("")
        self.BTStatus_LED.setPixmap(QtGui.QPixmap("Icons/led-red-on.png"))
        self.BTStatus_LED.setScaledContents(True)
        self.BTStatus_LED.setObjectName("BTStatus_LED")
        self.StatusGrid.addWidget(self.BTStatus_LED, 1, 1, 1, 1)
        self.ComPort_Combo = QtWidgets.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ComPort_Combo.setFont(font)
        self.ComPort_Combo.setObjectName("ComPort_Combo")
        self.ComPort_Combo.addItem("")
        self.StatusGrid.addWidget(self.ComPort_Combo, 0, 0, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 210, 311, 193))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.DataSrcGrid = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.DataSrcGrid.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.DataSrcGrid.setContentsMargins(0, 0, 0, 0)
        self.DataSrcGrid.setObjectName("DataSrcGrid")
        self.StopStreaming_Button = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StopStreaming_Button.sizePolicy().hasHeightForWidth())
        self.StopStreaming_Button.setSizePolicy(sizePolicy)
        self.StopStreaming_Button.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.StopStreaming_Button.setFont(font)
        self.StopStreaming_Button.setObjectName("StopStreaming_Button")
        self.DataSrcGrid.addWidget(self.StopStreaming_Button, 2, 0, 1, 1)
        self.OfflineData_LED = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.OfflineData_LED.setMaximumSize(QtCore.QSize(60, 60))
        self.OfflineData_LED.setText("")
        self.OfflineData_LED.setPixmap(QtGui.QPixmap("Icons/led-red-on.png"))
        self.OfflineData_LED.setScaledContents(True)
        self.OfflineData_LED.setObjectName("OfflineData_LED")
        self.DataSrcGrid.addWidget(self.OfflineData_LED, 1, 1, 1, 1)
        self.NomadStatus_LED = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.NomadStatus_LED.setMaximumSize(QtCore.QSize(60, 60))
        self.NomadStatus_LED.setText("")
        self.NomadStatus_LED.setPixmap(QtGui.QPixmap("Icons/led-red-on.png"))
        self.NomadStatus_LED.setScaledContents(True)
        self.NomadStatus_LED.setObjectName("NomadStatus_LED")
        self.DataSrcGrid.addWidget(self.NomadStatus_LED, 0, 1, 1, 1)
        self.StartNomad_Button = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StartNomad_Button.sizePolicy().hasHeightForWidth())
        self.StartNomad_Button.setSizePolicy(sizePolicy)
        self.StartNomad_Button.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.StartNomad_Button.setFont(font)
        self.StartNomad_Button.setObjectName("StartNomad_Button")
        self.DataSrcGrid.addWidget(self.StartNomad_Button, 0, 0, 1, 1)
        self.OfflineData_Button = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OfflineData_Button.sizePolicy().hasHeightForWidth())
        self.OfflineData_Button.setSizePolicy(sizePolicy)
        self.OfflineData_Button.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.OfflineData_Button.setFont(font)
        self.OfflineData_Button.setObjectName("OfflineData_Button")
        self.DataSrcGrid.addWidget(self.OfflineData_Button, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 875, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WiSSCI Connect"))
        self.Regressor_Combo.setCurrentText(_translate("MainWindow", "None"))
        self.Regressor_Combo.setItemText(0, _translate("MainWindow", "None"))
        self.ApplyConfig_Button.setText(_translate("MainWindow", "Apply Config"))
        self.Class_Nums_Line.setText(_translate("MainWindow", "1,7,8,9,13"))
        self.Classifier_Combo.setCurrentText(_translate("MainWindow", "LDA"))
        self.Classifier_Combo.setItemText(0, _translate("MainWindow", "LDA"))
        self.MAV_Sum_Label.setText(_translate("MainWindow", "MAV Sum Thresh."))
        self.Parameters_Button.setText(_translate("MainWindow", "Browse"))
        self.Classifier_Label.setText(_translate("MainWindow", "Classifier"))
        self.Hand_Mode_Label.setText(_translate("MainWindow", "Hand Mode"))
        self.Parameters_Label.setText(_translate("MainWindow", "Params (.mat)"))
        self.Hand_Mode_Combo.setCurrentText(_translate("MainWindow", "1 DOF Grip Switch"))
        self.Hand_Mode_Combo.setItemText(0, _translate("MainWindow", "1 DOF Grip Switch"))
        self.Wrist_Label.setText(_translate("MainWindow", "Active Wrist"))
        self.Wrist_Combo.setCurrentText(_translate("MainWindow", "No"))
        self.Wrist_Combo.setItemText(0, _translate("MainWindow", "No"))
        self.MAV_Sum_Line.setText(_translate("MainWindow", "0"))
        self.Regressor_Label.setText(_translate("MainWindow", "Regressor"))
        self.Class_Nums_Label.setText(_translate("MainWindow", "Class #s"))
        self.ParamsFile_Label.setText(_translate("MainWindow", "No params selected"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Configure_Tab), _translate("MainWindow", "Configure Decode"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.NomadTab), _translate("MainWindow", "MAV Graph"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DecodeTab), _translate("MainWindow", "WiSSCI Responses"))
        self.ConnectBT_Button.setText(_translate("MainWindow", "Connect Bluetooth"))
        self.ComPort_Combo.setItemText(0, _translate("MainWindow", "<Select port>"))
        self.StopStreaming_Button.setText(_translate("MainWindow", "Stop Streaming"))
        self.StartNomad_Button.setText(_translate("MainWindow", "Start Nomad"))
        self.OfflineData_Button.setText(_translate("MainWindow", "Start Offline Data"))
from pyqtgraph import PlotWidget
