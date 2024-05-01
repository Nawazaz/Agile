from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image

class MotivationalScreen(Screen):
    def __init__(self, **kwargs):
        super(MotivationalScreen, self).__init__(**kwargs)
        
        layout = FloatLayout()
        
        # Add background image
        background = Image(source='homebg.png', allow_stretch=True, keep_ratio=False)
        layout.add_widget(background)

        # Add text "Motivational Quotes" at the top center
        motivational_label = Label(text='Motivational Quotes', size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.5, 'top': 1}, font_size=30, color=(0, 0, 0, 1))
        layout.add_widget(motivational_label)

        left_image = Image(source='homeimg.png', size_hint=(None, None), size=(400, 1080), pos_hint={'left': 1})
        layout.add_widget(left_image)

        wellness_label = Label(text='Wellness\nBridge', size_hint=(None, None), size=(300, 50), pos_hint={'left': 0, 'top': 1}, font_size=24, color=(0, 0, 0, 1), text_size=(None, None), halign='left')  # Black color
        layout.add_widget(wellness_label)
        
        # Add some motivational quotes
        quote1 = Label(text='The only way to do great work is to love what you do.', size_hint=(None, None), size=(400, 50), pos_hint={'center_x': 0.5, 'top': 0.8}, font_size=18, color=(0, 0, 0, 1))
        layout.add_widget(quote1)

        quote2 = Label(text='Believe you can and you\'re halfway there.', size_hint=(None, None), size=(400, 50), pos_hint={'center_x': 0.5, 'top': 0.7}, font_size=18, color=(0, 0, 0, 1))
        layout.add_widget(quote2)

        quote3 = Label(text='Success is not final, failure is not fatal: It is the courage to continue that counts.', size_hint=(None, None), size=(400, 50), pos_hint={'center_x': 0.5, 'top': 0.6}, font_size=18, color=(0, 0, 0, 1))
        layout.add_widget(quote3)

        quote4 = Label(text='It does not matter how slowly you go as long as you do not stop.', size_hint=(None, None), size=(400, 50), pos_hint={'center_x': 0.5, 'top': 0.5}, font_size=18, color=(0, 0, 0, 1))
        layout.add_widget(quote4)
        
        self.add_widget(layout)
