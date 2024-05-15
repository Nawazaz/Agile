from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
import home_page
import library
import motivational
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import webbrowser





class PodcastScreen(Screen):
    
    def __init__(self, **kwargs):
        super(PodcastScreen, self).__init__(**kwargs)
        
        self.layout = FloatLayout()
        
        # Add background image
        background = Image(source='Pic/homebg.png', allow_stretch=True, keep_ratio=False)
        self.layout.add_widget(background)

        # Add text "Motivational Quotes" at the top center
        motivational_label = Label(text='Podcast', size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.5, 'top': 1}, font_size=30, color=(0, 0, 0, 1), font_name="fonts/BreeSerif-Regular.ttf")
        self.layout.add_widget(motivational_label)
        
        # Add left image
        left_image = Image(source='Pic/homeimg.png', size_hint=(None, None), size=(400, 1080), pos_hint={'left': 1})
        self.layout.add_widget(left_image)
        
        # Add wellness label
        wellness_label = Label(text='Wellness\n     Bridge', size_hint=(None, None), size=(300, 50), pos_hint={'left': 0, 'top': 0.99}, font_size=30, color=(0, 0, 0, 1), text_size=(None, None), halign='left', font_name="fonts/BreeSerif-Regular.ttf")  # Black color
        self.layout.add_widget(wellness_label)

        library_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(300, 50), pos_hint={'left': 1, 'top': 0.6})

        # Add Library image
        library_image = Image(source='Pic/book.png', size_hint=(None, None), size=(50, 50))
        library_layout.add_widget(library_image)

        # Add Library button
        library_button = Button(text='Library', size_hint=(None, None), size=(200, 50), font_size=23, background_color=(0, 0, 0, 0), color=(0, 0, 0, 1), font_name="fonts/SedanSC-Regular.ttf")  # Transparent background
        library_button.bind(on_press=self.go_to_library)
        library_layout.add_widget(library_button)

        Home_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(300, 50), pos_hint={'left': 1, 'top': 0.67})

        # Add Library image
        Home_image = Image(source='Pic/homeicon.png', size_hint=(None, None), size=(50, 50))
        Home_layout.add_widget(Home_image)

        # Add Library button
        Home_button = Button(text='Home', size_hint=(None, None), size=(200, 50), font_size=23, background_color=(0, 0, 0, 0), color=(0, 0, 0, 1), font_name="fonts/SedanSC-Regular.ttf")  # Transparent background
        Home_button.bind(on_press=self.go_to_home)
        Home_layout.add_widget(Home_button)

        # Add logout button
        logout_button = Button(text='Logout', size_hint=(None, None), size=(100, 50), pos_hint={'right': 0.95, 'top': 0.97}, font_size=18, background_color=(1, 0.5, 0, 1), font_name="fonts/BreeSerif-Regular.ttf")
        logout_button.bind(on_press=self.logout)
        self.layout.add_widget(logout_button)

        self.layout.add_widget(library_layout)
        self.layout.add_widget(Home_layout)
        self.add_widget(self.layout)
        
        # Add podcast image

        layout = FloatLayout()
        image = Image(source='Pic/we-can-do-hard-things-642a28f5bd0e1.jpg', size_hint=(None,None), size=(300,400),pos_hint={'center_x': 0.42, 'top': 0.97})
        layout.add_widget(image)
        self.add_widget(layout)
        
         # Add podcast link button
        create_url_button = Button(text='listen now', size_hint=(None, None), size=(25, 25), pos_hint={'left': 0.95, 'top': 0.97}, font_size=18, background_color=(1, 0.5, 0, 1), font_name="fonts/BreeSerif-Regular.ttf")
        create_url_button.bind(on_press=self.create_url_button)
        self.create_url_button("listen now", "https://podcasts.apple.com/us/podcast/we-can-do-hard-things/id1564530722")
        
    def create_url_button(self, text, url):
        # Create a button with the specified text
        url_button = Button(
        text=text,
        size_hint=(0.1, 0.05),  # Smaller button size
        pos_hint={'right': 0.45, 'top': 0.45},
        background_color=(0.6313725490196078, 0.8509803921568627, 0.5254901960784314, 1),  # Light green color
        background_normal='',  # Use the background color instead of an image
        color=(0, 0, 0, 1)  # Text color (black in this case)
)
        # Bind the button to a lambda function that calls open_url with the URL
        url_button.bind(on_press=lambda instance: self.open_url(url))
        
        # Add the button to the layout
        self.add_widget(url_button)
    
    def open_url(self, url):
        # Function to open a URL in the default web browser
        webbrowser.open(url)
        
    def go_to_home(self, instance):
        # Switching to the home page screen
        home_screen = home_page.HomePage(name='home_page')
        self.parent.add_widget(home_screen)
        self.parent.current = 'home_page'
    
    def go_to_library(self, instance):
        # Switching to the library page screen
        library_screen = library.SecondScreen(name='library_page')
        self.parent.add_widget(library_screen)
        self.parent.current = 'library_page'
    
    def logout(self, instance):
        self.parent.current= 'main'

            
        
        
if __name__ == '__main__':
    PodcastScreen().run()
        

        