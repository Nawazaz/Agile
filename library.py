from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image

class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super(SecondScreen, self).__init__(**kwargs)
        
        layout = FloatLayout()
        background = Image(source='homebg.png', allow_stretch=True, keep_ratio=False)
        layout.add_widget(background)
        
        self.add_widget(layout)
