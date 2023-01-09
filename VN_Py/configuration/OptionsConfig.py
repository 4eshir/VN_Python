from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QVBoxLayout, QSpacerItem,
    QWidget)

from configuration.BaseAppConfig import GameWindowConfig
from common.constants import ScreenSize


class OptionsConfig(GameWindowConfig):
    def __init__(self, height, width):
        super().__init__(height, width)
        #--GUI-объекты для главного меню--


        #---------------------------------

        #--Настраиваемые параметры--

        #--Разрешение экрана--
        self.ScreenResolution = [
            width,
            height
        ]
        #---------------------

        self.countRowGrid = 1  # количество строк grid-а
        self.countColGrid = 1  # количество столбцов grid-а

        self.rowHeights = []  # высота строк grid-а в %
        self.colWidth = []  # ширина столбцов grid-а в %

        #---------------------------


class OptionsConstructor:
    @staticmethod
    def createBaseGrid(window):
        window.centralwidget = QWidget(MainWindow)
        window.centralwidget.setObjectName(u"centralwidget")
        window.gridLayout_2 = QGridLayout(window.centralwidget)
        window.gridLayout_2.setObjectName(u"gridLayout_2")
        window.gridLayout = QGridLayout()
        window.gridLayout.setObjectName(u"gridLayout")
        window.label_5 = QLabel(window.centralwidget)
        window.label_5.setObjectName(u"label_5")

        window.gridLayout.addWidget(window.label_5, 0, 2, 1, 1)

        window.label_3 = QLabel(window.centralwidget)
        window.label_3.setObjectName(u"label_3")

        window.gridLayout.addWidget(window.label_3, 1, 0, 1, 1)

        window.label = QLabel(window.centralwidget)
        window.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Century Gothic"])
        font.setPointSize(22)
        font.setBold(True)
        window.label.setFont(font)

        window.gridLayout.addWidget(window.label, 0, 1, 1, 1)

        window.label_2 = QLabel(window.centralwidget)
        window.label_2.setObjectName(u"label_2")

        window.gridLayout.addWidget(window.label_2, 0, 0, 1, 1)

        window.label_4 = QLabel(window.centralwidget)
        window.label_4.setObjectName(u"label_4")

        window.gridLayout.addWidget(window.label_4, 2, 0, 1, 1)

        window.scrollArea = QScrollArea(window.centralwidget)
        window.scrollArea.setObjectName(u"scrollArea")
        window.scrollArea.setWidgetResizable(True)
        window.scrollAreaWidgetContents = QWidget()
        window.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        window.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 546, 320))
        window.verticalLayout_2 = QVBoxLayout(window.scrollAreaWidgetContents)
        window.verticalLayout_2.setObjectName(u"verticalLayout_2")
        window.verticalLayout = QVBoxLayout()
        window.verticalLayout.setObjectName(u"verticalLayout")
        window.verticalLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        window.horizontalLayout = QHBoxLayout()
        window.horizontalLayout.setObjectName(u"horizontalLayout")
        window.horizontalLayout.setContentsMargins(15, 10, 15, 10)
        window.label_7 = QLabel(window.scrollAreaWidgetContents)
        window.label_7.setObjectName(u"label_7")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(window.label_7.sizePolicy().hasHeightForWidth())
        window.label_7.setSizePolicy(sizePolicy)

        window.horizontalLayout.addWidget(window.label_7)

        window.comboBox = QComboBox(window.scrollAreaWidgetContents)
        window.comboBox.addItem("")
        window.comboBox.setObjectName(u"comboBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(window.comboBox.sizePolicy().hasHeightForWidth())
        window.comboBox.setSizePolicy(sizePolicy1)

        window.horizontalLayout.addWidget(window.comboBox)

        window.horizontalLayout.setStretch(0, 2)
        window.horizontalLayout.setStretch(1, 3)

        window.verticalLayout.addLayout(window.horizontalLayout)

        window.horizontalLayout_2 = QHBoxLayout()
        window.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        window.horizontalLayout_2.setContentsMargins(15, 10, 15, 10)
        window.label_8 = QLabel(window.scrollAreaWidgetContents)
        window.label_8.setObjectName(u"label_8")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(window.label_8.sizePolicy().hasHeightForWidth())
        window.label_8.setSizePolicy(sizePolicy2)

        window.horizontalLayout_2.addWidget(window.label_8)

        window.checkBox = QCheckBox(window.scrollAreaWidgetContents)
        window.checkBox.setObjectName(u"checkBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Ignored)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(window.checkBox.sizePolicy().hasHeightForWidth())
        window.checkBox.setSizePolicy(sizePolicy3)

        window.horizontalLayout_2.addWidget(window.checkBox)

        window.horizontalLayout_2.setStretch(0, 2)
        window.horizontalLayout_2.setStretch(1, 3)

        window.verticalLayout.addLayout(window.horizontalLayout_2)

        window.horizontalLayout_3 = QHBoxLayout()
        window.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        window.horizontalLayout_3.setContentsMargins(15, -1, 15, -1)
        window.label_9 = QLabel(window.scrollAreaWidgetContents)
        window.label_9.setObjectName(u"label_9")

        window.horizontalLayout_3.addWidget(self.label_9)

        window.horizontalSlider = QSlider(window.scrollAreaWidgetContents)
        window.horizontalSlider.setObjectName(u"horizontalSlider")
        window.horizontalSlider.setMaximum(100)
        window.horizontalSlider.setValue(50)
        window.horizontalSlider.setOrientation(Qt.Horizontal)

        window.horizontalLayout_3.addWidget(self.horizontalSlider)

        window.horizontalLayout_3.setStretch(0, 2)
        window.horizontalLayout_3.setStretch(1, 3)

        window.verticalLayout.addLayout(self.horizontalLayout_3)

        window.horizontalLayout_5 = QHBoxLayout()
        window.horizontalLayout_5.setObjectName(u"horizontalLayout_5")

        window.verticalLayout.addLayout(window.horizontalLayout_5)

        window.verticalLayout.setStretch(0, 1)
        window.verticalLayout.setStretch(1, 1)
        window.verticalLayout.setStretch(2, 1)
        window.verticalLayout.setStretch(3, 4)

        window.verticalLayout_2.addLayout(window.verticalLayout)

        window.scrollArea.setWidget(window.scrollAreaWidgetContents)

        window.gridLayout.addWidget(window.scrollArea, 1, 1, 1, 1)

        window.label_6 = QLabel(window.centralwidget)
        window.label_6.setObjectName(u"label_6")

        window.gridLayout.addWidget(window.label_6, 3, 0, 1, 1)

        window.horizontalLayout_4 = QHBoxLayout()
        window.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        window.horizontalLayout_4.setContentsMargins(200, -1, -1, -1)
        window.pushButton_2 = QPushButton(window.centralwidget)
        window.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(window.pushButton_2.sizePolicy().hasHeightForWidth())
        window.pushButton_2.setSizePolicy(sizePolicy4)

        window.horizontalLayout_4.addWidget(window.pushButton_2)

        window.pushButton = QPushButton(window.centralwidget)
        window.pushButton.setObjectName(u"pushButton")
        sizePolicy4.setHeightForWidth(window.pushButton.sizePolicy().hasHeightForWidth())
        window.pushButton.setSizePolicy(sizePolicy4)

        window.horizontalLayout_4.addWidget(window.pushButton)

        window.gridLayout.addLayout(window.horizontalLayout_4, 2, 1, 1, 1)

        window.gridLayout.setRowStretch(0, 2)
        window.gridLayout.setRowStretch(1, 8)
        window.gridLayout.setRowStretch(2, 1)
        window.gridLayout.setRowStretch(3, 2)
        window.gridLayout.setColumnStretch(0, 1)
        window.gridLayout.setColumnStretch(1, 5)
        window.gridLayout.setColumnStretch(2, 1)

        window.gridLayout_2.addLayout(window.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(window.centralwidget)
        window.menubar = QMenuBar(MainWindow)
        window.menubar.setObjectName(u"menubar")
        window.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(window.menubar)
        window.statusbar = QStatusBar(MainWindow)
        window.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(window.statusbar)

        window.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_5.setText("")
        self.label_3.setText("")
        self.label.setText(
            QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label_2.setText("")
        self.label_4.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u0420\u0430\u0437\u0440\u0435\u0448\u0435\u043d\u0438\u0435 \u044d\u043a\u0440\u0430\u043d\u0430",
                                                        None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"1920x1080", None))

        self.label_8.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u041f\u043e\u043b\u043d\u043e\u044d\u043a\u0440\u0430\u043d\u043d\u044b\u0439 \u0440\u0435\u0436\u0438\u043c",
                                                        None))
        self.checkBox.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u0423\u0440\u043e\u0432\u0435\u043d\u044c \u0437\u0432\u0443\u043a\u0430",
                                                        None))
        self.label_6.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow",
                                                             u"\u0412\u044b\u0439\u0442\u0438 \u0431\u0435\u0437 \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f",
                                                             None))
        self.pushButton.setText(
            QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi


