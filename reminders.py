from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import library
import motivational
import home_page
 
class RemindersScreen(Screen):
    def __init__(self, **kwargs):
        super(RemindersScreen, self).__init__(**kwargs)
 
        layout = FloatLayout()
 
        # Add background image
        background = Image(source='Pic/homebg.png', allow_stretch=True, keep_ratio=False)
        layout.add_widget(background)
 
        left_image = Image(source='Pic/homeimg.png', size_hint=(None, None), size=(400, 1080), pos_hint={'left': 1})
        layout.add_widget(left_image)
 
        # Add text "Reminders" at the top center
        reminders_label = Label(text='Reminders', size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.5, 'top': 1}, font_size=30, color=(0, 0, 0, 1), font_name="fonts/BreeSerif-Regular.ttf")
        layout.add_widget(reminders_label)
 
        # Add Wellness Bridge label
        wellness_label = Label(text='Wellness\n     Bridge', size_hint=(None, None), size=(300, 50), pos_hint={'left': 0, 'top': 0.99}, font_size=30, color=(0, 0, 0, 1), text_size=(None, None), halign='left', font_name="fonts/BreeSerif-Regular.ttf")
        layout.add_widget(wellness_label)
 
        # Add Home layout
        Home_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(300, 50), pos_hint={'left': 1, 'top': 0.67})
 
        # Add Home image
        Home_image = Image(source='Pic/homeicon.png', size_hint=(None, None), size=(50, 50))
        Home_layout.add_widget(Home_image)
 
        # Add Home button
        Home_button = Button(text='Home', size_hint=(None, None), size=(200, 50), font_size=23, background_color=(0, 0, 0, 0), color=(0, 0, 0, 1), font_name="fonts/SedanSC-Regular.ttf")  # Transparent background
        Home_button.bind(on_press=self.go_to_home)
        Home_layout.add_widget(Home_button)
 
        layout.add_widget(Home_layout)
 
        # Add Library layout
        library_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(300, 50), pos_hint={'left': 1, 'top': 0.6})
 
        # Add Library image
        library_image = Image(source='Pic/book.png', size_hint=(None, None), size=(50, 50))
        library_layout.add_widget(library_image)
 
        # Add Library button
        library_button = Button(text='Library', size_hint=(None, None), size=(200, 50), font_size=23, background_color=(0, 0, 0, 0), color=(0, 0, 0, 1), font_name="fonts/SedanSC-Regular.ttf")  # Transparent background
        library_button.bind(on_press=self.go_to_library)
        library_layout.add_widget(library_button)
 
        layout.add_widget(library_layout)
 
        # Add logout button
        logout_button = Button(text='Logout', size_hint=(None, None), size=(100, 50), pos_hint={'right': 0.95, 'top': 0.97}, font_size=18, background_color=(1, 0.5, 0, 1), font_name="fonts/BreeSerif-Regular.ttf")
        logout_button.bind(on_press=self.logout)
        layout.add_widget(logout_button)
 
        self.add_widget(layout)
 
    def go_to_home(self, instance):
        # Switching to the home page screen
        home_screen = home_page.HomePage(name='home_page')
        self.parent.add_widget(home_screen)
        self.parent.current = 'home_page'
 
    def go_to_library(self, instance):
        # Switching to the library page screen
        library_screen = library.LibraryScreen(name='library_page')
        self.parent.add_widget(library_screen)
        self.parent.current = 'library_page'
 
    def logout(self, instance):
        # Switching back to the main screen
        self.parent.current = 'main'