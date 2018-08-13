from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
#from logic import *

class BarbuGame(Widget):
    pass


class BarbuApp(App):
    def build(self):
        return BarbuGame()


if __name__ == '__main__':
    BarbuApp().run()