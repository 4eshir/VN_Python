import sys
from common.constants import System, ScreenSize, ButtonType
from wrapper.Button import UiButton

from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QSizePolicy
from PySide6.QtCore import QCoreApplication

from ui_templates_py.ui_mainwindow import Ui_MainWindow
from configuration import MenuConfig, OptionsConfig
from configuration.BaseAppConfig import GameWindowConfig
from configuration.DefaultAppFunctions import DefaultMainMenuFunctions


class MainWindow(QMainWindow):
    def __init__(self, mConfig, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow(mConfig, self)

    def createUi(self, mConfig):
        self.ui = Ui_MainWindow(mConfig, self)
        self.ui.setupUi(self)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QApplication()

    btn1 = QPushButton()
    sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
    sizePolicy1.setHorizontalStretch(1)
    sizePolicy1.setHeightForWidth(btn1.sizePolicy().hasHeightForWidth())

    btn1.setObjectName(u"pushButton")
    btn1.setSizePolicy(sizePolicy1)
    btn1.setText(QCoreApplication.translate("MainWindow", u"Новая игра", None))

    btn2 = QPushButton()
    sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
    sizePolicy1.setHorizontalStretch(1)
    sizePolicy1.setHeightForWidth(btn2.sizePolicy().hasHeightForWidth())

    btn2.setObjectName(u"pushButton2")
    btn2.setSizePolicy(sizePolicy1)
    btn2.setText(QCoreApplication.translate("MainWindow", u"Опции", None))

    btn3 = QPushButton()
    sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
    sizePolicy1.setHorizontalStretch(1)
    sizePolicy1.setHeightForWidth(btn3.sizePolicy().hasHeightForWidth())

    btn3.setObjectName(u"pushButton2")
    btn3.setSizePolicy(sizePolicy1)
    btn3.setText(QCoreApplication.translate("MainWindow", u"Выйти", None))

    mmConfig = MenuConfig.MainMenuConfig(ScreenSize.HEIGHT_1080, ScreenSize.WIDTH_1920)
    optConfig = OptionsConfig.OptionsConfig()

    window = MainWindow(mmConfig)

    mmConfig.rowHeights = [20, 60, 20]
    mmConfig.colWidth = [30, 40, 30]

    uBtn1 = UiButton(btn1, None)
    uBtn2 = UiButton(btn2, lambda: DefaultMainMenuFunctions.Options(window, optConfig))
    uBtn3 = UiButton(btn3, lambda: DefaultMainMenuFunctions.QuitGame(window))

    mmConfig.menuButtons = [uBtn1, uBtn2, uBtn3]
    mmConfig.buttonHeights = [30, 30, 20]
    mmConfig.buttonSpacer = [10, 10]
    mmConfig.countColGrid = 3
    mmConfig.countRowGrid = 3
    mmConfig.menuPositionRow = 1
    mmConfig.menuPositionCol = 1

    window.config = mmConfig

    window.createUi(mmConfig)


    window.show()


    sys.exit(app.exec())