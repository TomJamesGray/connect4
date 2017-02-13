import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget

class ConnectFour(Widget):
    pass

class ConnectFourApp(App):
    def build(self):
        return ConnectFour()

def main():
    ConnectFourApp().run()
