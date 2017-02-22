import kivy
from kivy.config import Config
Config.set('graphics','resizable',0)
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.modules import inspector
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import *

class ConnectFour(Widget):
    pass

class Column(Widget):
    def build(self):
        with self.canvas:
            Color(1,0,0,1)
            for i in range(6):
                Ellipse(pos=(0,i*74),size=(70,70))
            Translate(xy=self.pos)
class ConnectFourApp(App):
    def build(self):
        a = ConnectFour()
        inspector.create_inspector(Window,a)
        Window.size=(800,600)
        return a

def main():
    ConnectFourApp().run()
