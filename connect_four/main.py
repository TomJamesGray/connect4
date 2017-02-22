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
from kivy.properties import NumericProperty,ListProperty,DictProperty

global connectFourGame

class Player(object):
    def __init__(self,name,col,point_score):
        self.name = name
        self.col = col
        self.point_score = point_score


class ConnectFour(Widget):
    board = ListProperty([[0]*6 for x in range(7)])
    players = ListProperty([Player("1",(1,0,0),1),Player("2",(1,1,0),-1)])
    cur_player = NumericProperty(0)
    def get_first_space(col):
        """
        Returns the index of the first space in a list that is 0
        """
        for i in range(len(col)):
            if col[i] == 0:
                return i
        return False

    def make_move(self,col_no,col_obj):
        print("make_move: {}".format(col_no))
        self.board[col_no][ConnectFour.get_first_space(
            self.board[col_no])] = self.players[self.cur_player].point_score
        print("Board after move: {}".format(self.board))

        col_obj.redraw(self.board[col_no],{"1":(1,0,0),"-1":(1,1,0)})
        self.cur_player = int(not self.cur_player)
    pass

class Column(Widget):
    col_no = NumericProperty(None)
    
    def on_touch_down(self,touch):
        global connectFourGame
        if self.collide_point(touch.x,touch.y):
            print("Move on Column: {}".format(self.col_no))
            print(self)
            connectFourGame.make_move(self.col_no,self)

    def redraw(self,col_vals,cols):
        self.canvas.clear()
        with self.canvas:
            for i,space in enumerate(col_vals):
                if space == 0:
                    Color(1,1,1)
                else:
                    Color(*(cols[str(space)]))
                Ellipse(pos=(0,74*i),size=(70,70))

class ConnectFourApp(App):
    def build(self):
        global connectFourGame
        connectFourGame = ConnectFour()
        inspector.create_inspector(Window,connectFourGame)
        Window.size=(800,600)
        return connectFourGame

def main():
    ConnectFourApp().run()
