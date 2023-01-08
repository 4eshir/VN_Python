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

        #---------------------------


class OptionsConstructor:
    ...