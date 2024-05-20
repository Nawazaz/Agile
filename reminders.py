from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.spinner import Spinner
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
import time
import library
import motivational
import home_page


class TimePickerPopup(Popup):
    def __init__(self, **kwargs):
        super(TimePickerPopup, self).__init__(**kwargs)
        self.title = 'Set Alarm Time'
        self.title_align = 'center'  # Align title to the center
        self.size_hint = (None, None)
        self.size = (400, 300)
        self.background_color = (0, 0, 0, 0)  # Set transparent background color
        
        layout = GridLayout(cols=2, padding=10, spacing=10)
        
        layout.add_widget(Label(text='Hour:', color=(1, 1, 1, 1)))
        self.hour_spinner = Spinner(text='00', values=[f'{i:02}' for i in range(24)])
        layout.add_widget(self.hour_spinner)
        
        layout.add_widget(Label(text='Minute:', color=(1, 1, 1, 1)))
        self.minute_spinner = Spinner(text='00', values=[f'{i:02}' for i in range(60)])
        layout.add_widget(self.minute_spinner)
        
        set_button = Button(text='Set', size_hint_y=None, height=44, background_color=(135/255, 206/255, 250/255, 1))
        set_button.bind(on_press=self.set_time)
        layout.add_widget(set_button)
        
        self.add_widget(layout)
    
    def set_time(self, instance):
        hour = self.hour_spinner.text
        minute = self.minute_spinner.text
        self.dismiss()
        self.on_time_set(hour, minute)    
    
    def on_time_set(self, hour, minute):
        pass  # Override this method to handle the selected time


class RemindersScreen(Screen):
    def __init__(self, **kwargs):
        super(RemindersScreen, self).__init__(**kwargs)

        self.alarm_time_label = Label(text='', size_hint=(None, None), size=(300, 50), pos_hint={'x': 0.5, 'top': 0.8}, font_size = 40, color=(0, 0, 0, 1), font_name="fonts/BreeSerif-Regular.ttf")
        self.update_alarm_time_label()  # Update label text initially

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


        # Add text "Daily Quote Reminder" at the left top
        dailyQuote_label = Label(text='Daily Quote Reminder', size_hint=(None, None), size=(500, 45), pos_hint={'x': 0.3, 'top': 0.9}, font_size=30, color=(0.4, 0.4, 0.4, 1), font_name="fonts/BreeSerif-Regular.ttf")
        layout.add_widget(dailyQuote_label)


        # Create the toggle button for the quote reminder
        #quote_toggle_button = ToggleButton(
        #text='',
        #ize_hint=(None, None),
        #pos_hint={'right': 0.8, 'top': 0.8},  # Adjust position as needed
        #background_normal='Pic/ToggleOff.png',  # Specify the path to the normal image
        #background_down='Pic/ToggleOn.png'  # Specify the path to the down image
        #)
        #layout.add_widget(quote_toggle_button)

        # Add Set Alarm Time button
        set_alarm_button = Button(text='Set Alarm Time', size_hint=(None, None), size=(300, 50), pos_hint={'x': 0.3, 'top': 0.8}, font_size=23, background_color=(0.5, 0.5, 0.5, 0.5), color=(1, 1, 1, 1), font_name="fonts/BreeSerif-Regular.ttf")
        set_alarm_button.bind(on_press=self.open_time_picker)
        layout.add_widget(set_alarm_button)

        layout.add_widget(self.alarm_time_label)  # Add alarm time label
        
        #self.add_widget(layout)
        
        # Schedule the alarm check
        Clock.schedule_interval(self.check_alarm, 60)  # Check every minute

 
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
        self.parent.current = 'main'   

    def open_time_picker(self, instance):
        time_picker = TimePickerPopup()
        time_picker.on_time_set = self.set_alarm_time
        time_picker.open()

    def update_alarm_time_label(self):
        try:
            with open('alarm_time.txt', 'r') as f:
                alarm_time = f.read().strip()
            self.alarm_time_label.text = alarm_time
        except FileNotFoundError:
            self.alarm_time_label.text = 'Alarm not set'

    def set_alarm_time(self, hour, minute):
        # Save the alarm time
        alarm_time = f'{hour}:{minute}'
        with open('alarm_time.txt', 'w') as f:
            f.write(alarm_time)
        print(f'Alarm set for {alarm_time}')
        self.update_alarm_time_label()  # Update the alarm time label when it's set

    def check_alarm(self, dt):
        try:
            with open('alarm_time.txt', 'r') as f:
                alarm_time = f.read().strip()
            current_time = time.strftime('%H:%M')
            if current_time == alarm_time:
                self.show_daily_quote()
        except FileNotFoundError:
            pass

    def show_daily_quote(self):
        # Play alarm sound
        sound = SoundLoader.load('Pic/simple-notification-sound.mp3')
        if sound:
            sound.play()
        
        # Show popup with daily quote
        quote = "It's time to dive into the motivational quotes!"
        popup = Popup(title='Quote Reminder', content=Label(text=quote), size_hint=(None, None), size=(len(quote) * 10, len(quote) * 5), title_align='center')
        popup.open()