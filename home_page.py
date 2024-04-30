from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class HomePage(Screen):
    def __init__(self, **kwargs):
        super(HomePage, self).__init__(**kwargs)
        
        layout = FloatLayout()
        
        # Add background image
        background = Image(source='homebg.png', allow_stretch=True, keep_ratio=False)
        layout.add_widget(background)

        # Add left image
        left_image = Image(source='homeimg.png', size_hint=(None, None), size=(400, 1080), pos_hint={'left': 1})
        layout.add_widget(left_image)
        
        # Add right image
        right_image = Image(source='homeimg.png', size_hint=(None, None), size=(400, 1080), pos_hint={'right': 1})
        layout.add_widget(right_image)
        
        # Add text "Home" at the top center
        home_label = Label(text='Home', size_hint=(None, None), size=(100, 50), pos_hint={'center_x': 0.5, 'top': 1}, font_size=30, color=(0, 0, 0, 1))  # Black color
        layout.add_widget(home_label)
        
        # Add "Wellness bridge" label on the left image
        wellness_label = Label(text='Wellness\nBridge', size_hint=(None, None), size=(300, 50), pos_hint={'left': 0, 'top': 1}, font_size=24, color=(0, 0, 0, 1), text_size=(None, None), halign='left')  # Black color
        layout.add_widget(wellness_label)
        
        # Create a BoxLayout for Library
        library_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(300, 50), pos_hint={'left': 1, 'top': 0.6})
        
        # Add Library image
        library_image = Image(source='book.png', size_hint=(None, None), size=(50, 50))
        library_layout.add_widget(library_image)
        
        # Add Library button
        library_button = Button(text='Library', size_hint=(None, None), size=(200, 50), font_size=18, background_color=(0, 0, 0, 0), color=(0, 0, 0, 1))  # Transparent background
        library_button.bind(on_press=self.open_library)
        library_layout.add_widget(library_button)
        
        layout.add_widget(library_layout)
        
        # Create a BoxLayout for Motivational quotes
        quotes_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(300, 50), pos_hint={'left': 1, 'top': 0.5})
        
        # Add Motivational quotes image
        quotes_image = Image(source='graduationcap.png', size_hint=(None, None), size=(50, 50))
        quotes_layout.add_widget(quotes_image)
        
        # Add Motivational quotes button
        quotes_button = Button(text='Motivational\nquotes', size_hint=(None, None), size=(200, 50), font_size=18, background_color=(0, 0, 0, 0), color=(0, 0, 0, 1))  # Transparent background
        quotes_button.bind(on_press=self.open_motivational_quotes)
        quotes_layout.add_widget(quotes_button)
        
        layout.add_widget(quotes_layout)
        
        self.add_widget(layout)
    
    def open_library(self, instance):
        # Open the Library screen
        # You need to define the navigation to the library screen
        pass
    
    def open_motivational_quotes(self, instance):
        # Open the Motivational Quotes screen
        # You need to define the navigation to the motivational quotes screen
        pass
