import kivy
from kivy.config import Config
Config.set('graphics','resizable',0)
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.modules import inspector
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.graphics import *
from kivy.properties import NumericProperty,ListProperty,DictProperty

global connectFourGame

def get_first_available(col):
    """
    Returns the index of the first space in a list that is 0,
    returns -1 if the value isn't found as False can evaluate
    to 0
    """
    for i in range(len(col)):
        if col[i] == 0:
            return i
    return False

def get_n_by_n(a,top_x,top_y,n):
    out = []
    cols = a[top_x:top_x+n]
    for col in cols:
        out.append(col[top_y:top_y+n])

    return out

class Player(object):
    def __init__(self,name,col,point_score):
        self.name = name
        self.col = col
        self.point_score = point_score


class ConnectFour(Widget):
    board = ListProperty([[0]*6 for x in range(7)])
    players = ListProperty([Player("1",(1,0,0),1),Player("2",(1,1,0),-1)])
    cur_player = NumericProperty(0)

    def make_move(self,col_no,col_obj):
        print("make_move: {}".format(col_no))
        space_index = get_first_available(self.board[col_no])
        print(space_index)
        if space_index == False and isinstance(space_index,bool):
            print("Move can't be made")
            return False
        self.board[col_no][space_index] = self.players[
                self.cur_player].point_score
        print("Board after move: {}".format(self.board))

        col_obj.redraw(self.board[col_no],{"1":(1,0,0),"-1":(1,1,0)})
        print(self.check_win())
        if self.check_win():
            Popup(title="Game Finished",content=Label(text="{} won".format(
                self.players[self.cur_player].name,size=(400,400)))).open()
            print("Player {} won".format(self.cur_player))
            return True
        self.cur_player = int(not self.cur_player)
    
    def check_win(self):
        """
        Check for wins by using a 4x4 box and moving that around
        """
        for top_y in range(3):
            for top_x in range(4):
                to_check = get_n_by_n(self.board,top_x,top_y,4)
                row_check = [0]*4
                #Left to right and right to left diagonal check
                diag_check = [0]*2
                #Check columns
                for y,col in enumerate(to_check):
                    #Calculate scores of rows
                    for x,space in enumerate(col):
                        row_check[x] += space
                        if x == y:
                            diag_check[0] += space
                        if x+y == 3:
                            diag_check[1] += space

                    if sum(col) == 4:
                        return self.players[0]
                    elif sum(col) == -4:
                        return self.players[1]

                #Check row_check scores
                for row in row_check:
                    if row == 4:
                        return self.players[0]
                    elif row == -4:
                        return self.players[1]

                for diag in diag_check:
                    if diag == 4:
                        return self.players[0]
                    elif diag == -4:
                        return self.players[1]
        return False
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
                Ellipse(pos=(0,78*i),size=(70,70))

class ConnectFourApp(App):
    def build(self):
        global connectFourGame
        connectFourGame = ConnectFour()
        #inspector.create_inspector(Window,connectFourGame)
        #Window.clearcolor=(1,1,1,1)
        Window.size=(800,500)
        return connectFourGame

def main():
    ConnectFourApp().run()
