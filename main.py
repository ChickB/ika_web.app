import re
import random

from kivy.config import Config
Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '480')

from kivy.app import App
from kivy.uix.widget import Widget

from kivy.properties import StringProperty

from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path

from random import randint

# デフォルトに使用するフォントを変更する
resource_add_path('C:\Windows\Fonts')
LabelBase.register(DEFAULT_FONT,'MEIRYO.TTC')#日本語が使用できるように日本語フォントを指定する

s = 'hyousho.txt'
b = 'buki.txt'

with open(s, encoding="utf-8") as f:
    data = f.readlines()

with open(b, encoding="utf-8") as f:
    bu = f.readlines()

class ImageWidget(Widget):
    source = StringProperty('目標を決めよう！！')
    juu = StringProperty('ブキを選べ！！')

    def __init__(self, **kwargs):
        super(ImageWidget, self).__init__(**kwargs)
        pass

    def buttonStarted(self):
        self.juu= random.choice(bu) + 'で'

    def buttonRandom(self):
        self.source = random.choice(data) + 'を狙え'

class bbbApp(App):
    def __init__(self, **kwargs):
        super(bbbApp, self).__init__(**kwargs)
        self.title = 'イカルーレット'

if __name__ == '__main__':
    bbbApp().run()