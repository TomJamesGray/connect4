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
    def on_touch_down(self,touch):
        if self.collide_point(touch.x,touch.y):
            print("Ye")
            print(self.id)
class ConnectFourApp(App):
    def build(self):
        a = ConnectFour()
        inspector.create_inspector(Window,a)
        Window.size=(800,600)
        return a

def main():
    ConnectFourApp().run()
