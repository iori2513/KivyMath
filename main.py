import kivy
from kivy.config import Config

Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '600')

from kivy.app import App
from kivy.uix.widget import Widget

from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path
from kivy.properties import StringProperty
from kivy.lang import Builder
import random
from direction import direction1, direction2
import importlib





# デフォルトに使用するフォントを変更する
resource_add_path('/System/Library/Fonts')
LabelBase.register(DEFAULT_FONT, 'PingFang.ttc')  # 日本語が使用できるように日本語フォントを指定する


class Direction:
    def __init__(self, id, answer, problem):
        self.id = id
        self.answer = answer
        self.problem = problem

def define():
    monndai_1 = Direction(1, direction1.answer, direction1.sentence)
    monndai_2 = Direction(2, direction2.answer, direction2.sentence)
    monndai_list = [monndai_1, monndai_2]
    monndai = random.choice(monndai_list)
    return (monndai)

x = define()



class ImageWidget(Widget):

    source = StringProperty(x.problem)

    def __init__(self, **kwargs):
        super(ImageWidget, self).__init__(**kwargs)
        pass

    def answer(self):
        self.source = x.answer

    def go_back(self):
        self.source = x.problem

    def new_direction(self):
        importlib.reload(direction1)
        importlib.reload(direction2)
        global x
        x = define()
        self.source = x.problem


class MathApp(App):
    def __init__(self, **kwargs):
        super(MathApp, self).__init__(**kwargs)
        self.title = '算数'


if __name__ == '__main__':
    MathApp().run()
