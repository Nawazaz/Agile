import requests
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import home_page
import library
#import serial
import time
from kivy.clock import mainthread
from kivy.graphics import Color, Rectangle
from kivy.properties import NumericProperty

class MotivationalScreen(Screen):
    countdown = NumericProperty(20)  # Initial countdown value

    def __init__(self, **kwargs):
        super(MotivationalScreen, self).__init__(**kwargs)
        
        self.layout = FloatLayout()
        
        # Add background image
        background = Image(source='Pic/homebg.png', allow_stretch=True, keep_ratio=False)
        self.layout.add_widget(background)

        # Add text "Motivational Quotes" at the top center
        motivational_label = Label(text='Motivational Quotes', size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.5, 'top': 1}, font_size=30, color=(0, 0, 0, 1), font_name="fonts/BreeSerif-Regular.ttf")
        self.layout.add_widget(motivational_label)

        left_image = Image(source='Pic/homeimg.png', size_hint=(None, None), size=(400, 1080), pos_hint={'left': 1})
        self.layout.add_widget(left_image)

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
        #self.ser = serial.Serial('COM3', 9600)  # Change 'COM3' to your Arduino's serial port
        self.update_quotes()
        # Other initialization code...
        self.timer_label = Label(text=str(self.countdown), size_hint=(None, None), size=(50, 50), pos_hint={'right': 1, 'top': 1}, color=(0, 0, 0, 1))
        self.layout.add_widget(self.timer_label)
        self.start_timer()

    @mainthread
    def update_quotes(self, dt=None):
        try:
            response = requests.get("https://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en&key=1")
            if response.status_code == 200:
                quote_data = response.json()
                quote_text = quote_data["quoteText"]
                quote_author = quote_data["quoteAuthor"]

                # Display the fetched quote
                self.display_quote(quote_text, quote_author)
                self.send_to_arduino(quote_text, quote_author)
        except Exception as e:
            print("Error fetching quote:", e)
            self.update_quotes()

        # Schedule the next update after 60 seconds
        #Clock.schedule_once(self.update_quotes, 20)

    #def send_to_arduino(self, quote_text, quote_author):
        #message = f'"{quote_text}" - {quote_author}\n'
        #print("Sending to Arduino:", message)
        #self.ser.write(message.encode())

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
    def display_quote(self, quote_text, quote_author):
        # Clear previous quotes
        self.clear_previous_quotes()

        # Define the size of the quote box with additional padding
        quote_box_size = (600, 500)  # Adjust as needed
        padding_left_right = 20
        padding_top = 50

        # Create a BoxLayout for the quote box
        quote_box = BoxLayout(orientation='vertical', size_hint=(None, None), size=quote_box_size, pos_hint={'center_x': 0.5, 'center_y': 0.5}, padding=(padding_left_right, padding_top))

        # Add a black transparent background behind the quote
        with quote_box.canvas.before:
            Color(0, 0, 0, 0.5)  # Black with 50% opacity
            self.quote_rect = Rectangle(pos=quote_box.pos, size=quote_box.size)

        # Create Label for quote text with adjusted padding
        quote_label = Label(text=f'"{quote_text}"', font_size=36, color=(1, 1, 1, 1), halign='center', valign='middle', font_name="fonts/PoetsenOne-Regular.ttf", padding=(padding_left_right, 0))
        quote_label.bind(size=quote_label.setter('text_size'))  # Allow text wrapping
        quote_label.size_hint_y = None
        quote_label.height = dp(400)  # Set a fixed height for text wrapping

        # Create Label for quote author
        author_label = Label(text=f"- {quote_author}", font_size=20, color=(1, 1, 1, 0.7), halign='right')

        # Add labels to quote box
        quote_box.add_widget(quote_label)
        quote_box.add_widget(author_label)

        # Add quote box to layout
        self.layout.add_widget(quote_box)

        # Update the position and size of the rectangle when the quote_box changes
        quote_box.bind(pos=self.update_rect, size=self.update_rect)


    def clear_previous_quotes(self):
        # Remove previous quote boxes
        for widget in self.layout.children[:]:
            if isinstance(widget, BoxLayout) and any(isinstance(child, Label) and child.text.startswith('"') for child in widget.children):
                self.layout.remove_widget(widget)


    def update_rect(self, instance, value):
        self.quote_rect.pos = instance.pos
        self.quote_rect.size = instance.size



    @mainthread
    def update_timer_label(self):
        self.timer_label.text = str(self.countdown)

    def start_timer(self):
        Clock.schedule_interval(self.update_timer, 1)  # Update timer every second

    def update_timer(self, dt):
        if self.countdown > 0:
            self.countdown -= 1
            self.update_timer_label()
        else:
            self.countdown = 20  # Reset countdown after 20 seconds
            self.update_timer_label()
            self.update_quotes()  # Fetch new quote
    def logout(self, instance):
        # Switching back to the main screen
        self.parent.current = 'main'

# Usage example
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MotivationalScreen(name='motivational_screen'))
        return sm

if __name__ == '__main__':
    MyApp().run()