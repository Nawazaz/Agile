from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import library
import motivational
from kivy.uix.image import AsyncImage
from kivy.uix.button import Button

class HomePage(Screen):
    def __init__(self, **kwargs):
        super(HomePage, self).__init__(**kwargs)
        
        layout = FloatLayout()
        
        # Add background image
        background = Image(source='Pic/homeimg.png', allow_stretch=True, keep_ratio=False)
        layout.add_widget(background)
        
        # Add text "Home" at the top center
        home_label = Image(source='Pic/Logo.png', size_hint=(None, None), size=(300, 150), pos_hint={'left': 2, 'top': 1})  # Black color
        layout.add_widget(home_label)
        
        # Add "Wellness bridge" label on the left image
        wellness_label = Label(text='Wellness\n     Bridge', size_hint=(None, None), size=(300, 50), 
                            pos_hint={'right': 0.87, 'top': 0.6}, font_size=135, 
                            color=(0.071, 0.078, 0.506, 1),  # Navy blue color
                            text_size=(None, None), halign='left', 
                            font_name="fonts/BreeSerif-Regular.ttf")
        layout.add_widget(wellness_label)

        # Add description text below Wellness Bridge
        description_text = Label(text='Wellness Bridge is a revolutionary app designed to\n empower individuals with mental/chronic illnesses\n by providing a supportive community platform\n and comprehensive resources for holistic\n well being.',
                                size_hint=(None, None), size=(800, 100), 
                                pos_hint={'right': 1, 'top': 0.3}, 
                                font_size=24, color=(0, 0, 0, 1),  # Black color
                                text_size=(None, None), halign='left', font_name="fonts/BreeSerif-Regular.ttf")
        layout.add_widget(description_text)

        main_image = Image(source='Pic/hmbg.png', size_hint=(None, None), size=(1000, 1000), pos_hint={'left': 0, 'bottom': 2}, allow_stretch=True)
        layout.add_widget(main_image)

        
        # Create a BoxLayout for Library
        library_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.5, 'top': 0.97})
        
        # Add Library button
        library_button = Button(text='Library', size_hint=(None, None), size=(200, 50), font_size=23, background_color=(0, 0, 0, 0), color=(0, 0, 0, 1), font_name="fonts/BreeSerif-Regular.ttf")  # Transparent background
        library_button.bind(on_press=self.go_to_library)
        library_layout.add_widget(library_button)
        
        layout.add_widget(library_layout)
        
        # Create a BoxLayout for Motivational quotes
        quotes_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(300, 50), pos_hint={'right': 0.68 , 'top': 0.97})
        
        # Add Motivational quotes button
        quotes_button = Button(text='Motivational quotes', size_hint=(None, None), size=(200, 50), font_size=23, background_color=(0, 0, 0, 0), color=(0, 0, 0, 1), font_name="fonts/BreeSerif-Regular.ttf")
        quotes_button.bind(on_press=self.go_to_motivational)
        quotes_layout.add_widget(quotes_button)
        
        layout.add_widget(quotes_layout)
        
        # Add logout button
        logout_button = Button(text='Logout', size_hint=(None, None), size=(100, 50), pos_hint={'right': 0.95, 'top': 0.97}, font_size=18, background_color=(1, 0.5, 0, 1), font_name="fonts/BreeSerif-Regular.ttf")
        logout_button.bind(on_press=self.logout)
        layout.add_widget(logout_button)
        
        self.add_widget(layout)

        
    def go_to_library(self, instance):
        # Switching to the library screen
        library_screen = library.LibraryScreen(name='library')
        self.parent.add_widget(library_screen)
        self.parent.current = 'library'
    
    def go_to_motivational(self, instance):
        # Switching to the motivational screen
        motivational_screen = motivational.MotivationalScreen(name='motivational')
        self.parent.add_widget(motivational_screen)
        self.parent.current = 'motivational'
    
    def logout(self, instance):
        # Switching back to the main screen
        self.parent.current = 'main'