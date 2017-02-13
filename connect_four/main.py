import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.label import Label
from kivy.uix.widget import Widget

class ConnectFour(Widget):
    pass

class Menu(Widget):
    pass

class ConnectFourApp(App):
    def build(self):
        return ConnectFour()

def main():
    Config.set("graphics","width","800")
    Config.set("graphics","height","600")
    ConnectFourApp().run()
