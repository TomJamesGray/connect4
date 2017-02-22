import kivy
from kivy.config import Config
Config.set('graphics','resizable',0)
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.modules import inspector

class ConnectFour(Widget):
    pass

class Menu(Widget):
    pass

class ConnectFourApp(App):
    def build(self):
        a = ConnectFour()
        inspector.create_inspector(Window,a)
        return a

def main():
    ConnectFourApp().run()
