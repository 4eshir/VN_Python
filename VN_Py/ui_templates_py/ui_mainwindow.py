from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

from PySide6 import QtCore
from PySide6 import QtGui

from common.constants import System
from configuration.MenuConfig import MainMenuConfig, MainMenuConstructor
from configuration.BaseAppConfig import GameWindowConfig


from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def __init__(self, mConfig, mWindow):
        self.config = mConfig
        self.uiWindow = mWindow

    def setupUi(self, MainWindow):
        if not self.uiWindow.objectName():
            self.uiWindow.setObjectName(u"MainWindow")
        self.uiWindow.resize(self.config.windowWidth, self.config.windowHeight)
        self.uiWindow.setStyleSheet(
            "#centralwidget {border-image: url(" + System.APP_PATH + "/" + self.config.backPath + ") 0 0 0 0 stretch stretch}"
        )

        self.centralwidget = QWidget(self.uiWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)

        self.uiWindow.label_m = QLabel(self.centralwidget)
        self.uiWindow.label_m.setObjectName(u"label_m")
        self.gridLayout = QGridLayout()
        self.gridLayout.addWidget(self.uiWindow.label_m, 0, 0, 1, 1)

        self.uiWindow.setCentralWidget(self.centralwidget)

        self.createMainMenu()
        self.retranslateUi()

        QMetaObject.connectSlotsByName(self.uiWindow)
    # setupUi

    def retranslateUi(self):
        self.uiWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
    # retranslateUi


    def createMainMenu(self):
        MainMenuConstructor.createBaseGrid(self) # ???????????????? ?????????????????? grid-??
        MainMenuConstructor.createMenuButtons(self) # ???????????????? ???????????? ???????????????? ????????


