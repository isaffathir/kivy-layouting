from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

class Home(MDScreen):
    def __init__(self, **kw):
        Builder.load_file("kv/home.kv")
        super().__init__(**kw)
        