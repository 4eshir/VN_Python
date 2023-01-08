from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QVBoxLayout, QSpacerItem,
    QWidget)

from configuration.BaseAppConfig import GameWindowConfig
from configuration.DefaultAppFunctions import DefaultMainMenuFunctions
from common.constants import System, ScreenSize, ButtonType


class MainMenuConfig(GameWindowConfig):
    def __init__(self, height, width):
        super().__init__(height, width)
        #--GUI-объекты для главного меню--

        #self.baseGrid = QGridLayout() # основной grid окна
        #self.fillerLabel = QLabel() # пустой label для создания grid-а требуемой размерности
        #self.menuLayout = QVBoxLayout() # вертикальный layout для главного меню
        self.menuButtons = [] # список кнопок меню QPushButton

        # ---------------------------------

        #--Настраиваемые параметры--

        self.countRowGrid = 1 # количество строк grid-а
        self.countColGrid = 1 # количество столбцов grid-а

        self.rowHeights = [] # высота строк grid-а в %
        self.colWidth = [] # ширина столбцов grid-а в %

        self.menuPositionRow = 0  # расположение главного меню - номер строки
        self.menuPositionCol = 0 # расположение главного меню - номер столбца

        # меню - номер столбца

        self.buttonHeights = [] # размеры кнопок в %
        self.buttonSpacer = [] # расстояние между кнопками в %

        # ---------------------------

    def setupConfig(self, cRow, cCol, rHeights, cWidth, menuX, menuY, bHeights, bUpDown, bLeftRight):
        self.countRowGrid = cRow
        self.countColGrid = cCol
        self.rowHeights = rHeights
        self.colWidth = cWidth
        self.menuPositionX = menuX
        self.menuPositionY = menuY
        self.buttonHeights = bHeights
        self.buttonUpDownMargins = bUpDown
        self.buttonLeftRightMargins = bLeftRight


class MainMenuConstructor:

    @staticmethod
    def createBaseGrid(window):
        #--Layout_2 для ресайза Layout при ресайзе MainWindow--
        window.gridLayout_2 = QGridLayout(window.centralwidget)
        window.gridLayout_2.setObjectName(u"gridLayout_2")
        window.gridLayout = QGridLayout()
        window.gridLayout.setSpacing(0)
        window.gridLayout.setObjectName(u"gridLayout")
        # ------------------------------------------------------

        #--Пустые Label для отрисовки Grid требуемой размерности
        window.label_1 = QLabel(window.centralwidget)
        window.label_1.setObjectName(u"label_1")

        window.gridLayout.addWidget(window.label_1, 0, 0, 1, 1)

        window.label_2 = QLabel(window.centralwidget)
        window.label_2.setObjectName(u"label_2")

        window.gridLayout.addWidget(window.label_2, window.config.countRowGrid - 1, window.config.countColGrid - 1, 1, 1)
        #------------------------------------------------------


        #--Выставление ширины и высоты столбцов и строк соответственно--
        for i in range(len(window.config.rowHeights)):
            window.gridLayout.setRowStretch(i, window.config.rowHeights[i])

        for i in range(len(window.config.colWidth)):
            window.gridLayout.setColumnStretch(i, window.config.colWidth[i])
        #---------------------------------------------------------------

        window.gridLayout_2.addLayout(window.gridLayout, 0, 0, 1, 1)


    @staticmethod
    def createMenuButtons(window):
        window.verticalLayout = QVBoxLayout()
        window.verticalLayout.setObjectName(u"verticalLayout")
        window.verticalLayout.setContentsMargins(20, 20, 20, 20)

        #--Добавление кнопок из массива menuButtons--
        for i in range(len(window.config.menuButtons)):
            window.verticalLayout.addWidget(window.config.menuButtons[i].button)
            if i < len(window.config.menuButtons) - 1:
                verticalSpacer = QSpacerItem(10, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
                window.verticalLayout.addItem(verticalSpacer)
        #--------------------------------------------


        #--Настройка высоты кнопок и отуступов между ними--
        btnCount = 0
        spcCount = 0
        for i in range(window.verticalLayout.count()):
            if i % 2 == 0:
                window.verticalLayout.setStretch(i, window.config.buttonHeights[btnCount])
                btnCount += 1
            else:
                window.verticalLayout.setStretch(i, window.config.buttonSpacer[spcCount])
                spcCount += 1
        # --------------------------------------------------

        MainMenuConstructor.connectButtonSignal(window)

        window.gridLayout.addLayout(window.verticalLayout, window.config.menuPositionRow, window.config.menuPositionCol, 1, 1)

    @staticmethod
    def connectButtonSignal(window):
        for i in range(len(window.config.menuButtons)):
            print(window.config.menuButtons[i].connect)
            window.config.menuButtons[i].button.clicked.connect(window.config.menuButtons[i].connect)