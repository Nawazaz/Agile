from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader
from kivy.app import App
from kivy.clock import Clock
import motivational
import home_page
import library
import reminders
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.properties import NumericProperty
 
class PodcastScreen(Screen):
    remaining_time1 = NumericProperty(0)
    remaining_time2 = NumericProperty(0)
    remaining_time3 = NumericProperty(0)
    remaining_time4 = NumericProperty(0)
 
    def __init__(self, **kwargs):
        super(PodcastScreen, self).__init__(**kwargs)
        Clock.schedule_interval(self.update_slider1, 0.1)
        Clock.schedule_interval(self.update_slider2, 0.1)
        Clock.schedule_interval(self.update_slider3, 0.1)
        Clock.schedule_interval(self.update_slider4, 0.1)
        self.layout = FloatLayout()
 
        # Add background image
        background = Image(source='Pic/homebg.png', allow_stretch=True, keep_ratio=False)
        self.layout.add_widget(background)
 
        # Add text "Podcast" at the top center
        motivational_label = Label(text='Podcast', size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.5, 'top': 1}, font_size=30, color=(0, 0, 0, 1), font_name="fonts/BreeSerif-Regular.ttf")
        self.layout.add_widget(motivational_label)
 
        # Add left image
        left_image = Image(source='Pic/homeimg.png', size_hint=(None, None), size=(400, 1080), pos_hint={'left': 1})
        self.layout.add_widget(left_image)
 
        # Add wellness label
        wellness_label = Label(text='Wellness\n     Bridge', size_hint=(None, None), size=(300, 50), pos_hint={'left': 0, 'top': 0.99}, font_size=30, color=(0, 0, 0, 1), text_size=(None, None), halign='left', font_name="fonts/BreeSerif-Regular.ttf")
        self.layout.add_widget(wellness_label)
 
        library_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(300, 50), pos_hint={'left': 1, 'top': 0.6})
 
        # Add Library image
        library_image = Image(source='Pic/book.png', size_hint=(None, None), size=(50, 50))
        library_layout.add_widget(library_image)
 
        # Add Library button
        library_button = Button(text='Library', size_hint=(None, None), size=(200, 50), font_size=23, background_color=(0, 0, 0, 0), color=(0, 0, 0, 1), font_name="fonts/SedanSC-Regular.ttf")
        library_button.bind(on_press=self.go_to_library)
        library_layout.add_widget(library_button)
 
        home_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(300, 50), pos_hint={'left': 1, 'top': 0.67})
 
        # Add Home image
        home_image = Image(source='Pic/homeicon.png', size_hint=(None, None), size=(50, 50))
        home_layout.add_widget(home_image)
 
        # Add Home button
        home_button = Button(text='Home', size_hint=(None, None), size=(200, 50), font_size=23, background_color=(0, 0, 0, 0), color=(0, 0, 0, 1), font_name="fonts/SedanSC-Regular.ttf")
        home_button.bind(on_press=self.go_to_home)
        home_layout.add_widget(home_button)

        motivational_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(300, 50), pos_hint={'left': 1, 'top': 0.53})

        # Add Motivational image
        motivational_image = Image(source='Pic/graduationcap.png', size_hint=(None, None), size=(50, 50))
        motivational_layout.add_widget(motivational_image)

        # Add Motivational button
        motivational_button = Button(text='Motivational \n Quotes', size_hint=(None, None), size=(200, 50), font_size=23, background_color=(0, 0, 0, 0), color=(0, 0, 0, 1), font_name="fonts/SedanSC-Regular.ttf")  # Transparent background
        motivational_button.bind(on_press=self.go_to_motivational)  # Bind the button to a method
        motivational_layout.add_widget(motivational_button)

        reminder_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(300, 50), pos_hint={'left': 1, 'top': 0.46})

        # Add Motivational image
        reminder_image = Image(source='Pic/graduationcap.png', size_hint=(None, None), size=(50, 50))
        reminder_layout.add_widget(reminder_image)

        # Add Motivational button
        reminder_button = Button(text='Reminders', size_hint=(None, None), size=(200, 50), font_size=23, background_color=(0, 0, 0, 0), color=(0, 0, 0, 1), font_name="fonts/SedanSC-Regular.ttf")  # Transparent background
        reminder_button.bind(on_press=self.go_to_reminder)  # Bind the button to a method
        reminder_layout.add_widget(reminder_button)

        # Add logout button
        logout_button = Button(text='Logout', size_hint=(None, None), size=(100, 50), pos_hint={'right': 0.95, 'top': 0.97}, font_size=18, background_color=(1, 0.5, 0, 1), font_name="fonts/BreeSerif-Regular.ttf")
        logout_button.bind(on_press=self.logout)
        self.layout.add_widget(logout_button)
 
        # Add Podcast 1 image
        podcast1_image = Image(source='Pic/pod1.jpg', size_hint=(None, None), size=(300, 300), pos_hint={'center_x': 0.35, 'center_y': 0.8})
        self.layout.add_widget(podcast1_image)
 
        # Add Play/Pause button for Podcast 1
        self.play_button1 = Button(text='Play', size_hint=(None, None), size=(100, 50), pos_hint={'center_x': 0.35, 'center_y': 0.59}, font_size=18, background_color=(0, 0.5, 0, 1), font_name="fonts/BreeSerif-Regular.ttf")
        self.play_button1.bind(on_press=self.toggle_play_pause1)
        self.layout.add_widget(self.play_button1)
 
        self.sound1 = SoundLoader.load('pod/12MM-_Jessica_Morey_6.16.mp3')
 
        # Add Slider for Podcast 1
        self.slider1 = Slider(min=0, max=1, value=0, size_hint=(None, None), size=(350, 50), pos_hint={'center_x': 0.35, 'center_y': 0.63})
        self.layout.add_widget(self.slider1)
        # Add Timer label for Podcast 1
        self.timer_label1 = Label(text="0:00", size_hint=(None, None), size=(100, 50), pos_hint={'center_x': 0.41, 'center_y': 0.60}, color=(0, 0, 0, 1))
        self.layout.add_widget(self.timer_label1)
 
        # Add Podcast 2 image
        podcast2_image = Image(source='Pic/pod2.png', size_hint=(None, None), size=(300, 300), pos_hint={'center_x': 0.7, 'center_y': 0.8})
        self.layout.add_widget(podcast2_image)
 
        # Add Play/Pause button for Podcast 2
        self.play_button2 = Button(text='Play', size_hint=(None, None), size=(100, 50), pos_hint={'center_x': 0.7, 'center_y': 0.59}, font_size=18, background_color=(0, 0.5, 0, 1), font_name="fonts/BreeSerif-Regular.ttf")
        self.play_button2.bind(on_press=self.toggle_play_pause2)
        self.layout.add_widget(self.play_button2)
 
        self.sound2 = SoundLoader.load('TIN_-_Sensory_Diet_-_PODCAST8wwsn.mp3')
 
        # Add Slider for Podcast 2
        self.slider2 = Slider(min=0, max=1, value=0, size_hint=(None, None), size=(350, 50), pos_hint={'center_x': 0.7, 'center_y': 0.63})
        self.layout.add_widget(self.slider2)
        # Add Timer label for Podcast 2
        self.timer_label2 = Label(text="0:00", size_hint=(None, None), size=(100, 50), pos_hint={'center_x': 0.77, 'center_y': 0.60}, color=(0, 0, 0, 1))
        self.layout.add_widget(self.timer_label2)
 
        # Add Podcast 3 image
        podcast3_image = Image(source='Pic/pod3.jpg', size_hint=(None, None), size=(300, 300), pos_hint={'center_x': 0.35, 'center_y': 0.4})
        self.layout.add_widget(podcast3_image)
 
        # Add Play/Pause button for Podcast 3
        self.play_button3 = Button(text='Play', size_hint=(None, None), size=(100, 50), pos_hint={'center_x': 0.35, 'center_y': 0.19}, font_size=18, background_color=(0, 0.5, 0, 1), font_name="fonts/BreeSerif-Regular.ttf")
        self.play_button3.bind(on_press=self.toggle_play_pause3)
        self.layout.add_widget(self.play_button3)
 
        self.sound3 = SoundLoader.load('pod/jenni_bell_b6hym-AI-Generated.mp3')
 
        # Add Slider for Podcast 3
        self.slider3 = Slider(min=0, max=1, value=0, size_hint=(None, None), size=(350, 50), pos_hint={'center_x': 0.35, 'center_y': 0.23})
        self.layout.add_widget(self.slider3)
        # Add Timer label for Podcast 3
        self.timer_label3 = Label(text="0:00", size_hint=(None, None), size=(100, 50), pos_hint={'center_x': 0.41, 'center_y': 0.20}, color=(0, 0, 0, 1))
        self.layout.add_widget(self.timer_label3)
 
        # Add Podcast 4 image
        podcast4_image = Image(source='Pic/pod4.jpg', size_hint=(None, None), size=(300, 300), pos_hint={'center_x': 0.7, 'center_y': 0.4})
        self.layout.add_widget(podcast4_image)
 
        # Add Play/Pause button for Podcast 4
        self.play_button4 = Button(text='Play', size_hint=(None, None), size=(100, 50), pos_hint={'center_x': 0.7, 'center_y': 0.19}, font_size=18, background_color=(0, 0.5, 0, 1), font_name="fonts/BreeSerif-Regular.ttf")
        self.play_button4.bind(on_press=self.toggle_play_pause4)
        self.layout.add_widget(self.play_button4)
 
        self.sound4 = SoundLoader.load('pod/Y6RIrHibNJs2.128.mp3')
 
        # Add Slider for Podcast 4
        self.slider4 = Slider(min=0, max=1, value=0, size_hint=(None, None), size=(350, 50), pos_hint={'center_x': 0.7, 'center_y': 0.23})
        self.layout.add_widget(self.slider4)
        # Add Timer label for Podcast 4
        self.timer_label4 = Label(text="0:00", size_hint=(None, None), size=(100, 50), pos_hint={'center_x': 0.77, 'center_y': 0.20}, color=(0, 0, 0, 1))
        self.layout.add_widget(self.timer_label4)
 
        self.layout.add_widget(library_layout)
        self.layout.add_widget(home_layout)
        self.layout.add_widget(motivational_layout)
        self.layout.add_widget(reminder_layout)
        self.add_widget(self.layout)
 
    def toggle_play_pause1(self, instance):
        if self.sound1:
            if self.sound1.state == 'play':
                self.sound1.stop()
                self.play_button1.text = 'Play'
            else:
                self.sound1.play()
                self.play_button1.text = 'Pause'
 
    def toggle_play_pause2(self, instance):
        if self.sound2:
            if self.sound2.state == 'play':
                self.sound2.stop()
                self.play_button2.text = 'Play'
            else:
                self.sound2.play()
                self.play_button2.text = 'Pause'
 
    def update_slider1(self, dt):
        if self.sound1:
            self.slider1.value = self.sound1.get_pos() / self.sound1.length if self.sound1.length > 0 else 0
            self.remaining_time1 = self.sound1.length - self.sound1.get_pos()
            self.timer_label1.text = self.format_time(self.remaining_time1)
 
    def update_slider2(self, dt):
        if self.sound2:
            self.slider2.value = self.sound2.get_pos() / self.sound2.length if self.sound2.length > 0 else 0
            self.remaining_time2 = self.sound2.length - self.sound2.get_pos()
            self.timer_label2.text = self.format_time(self.remaining_time2)
    def toggle_play_pause3(self, instance):
        if self.sound3:
            if self.sound3.state == 'play':
                self.sound3.stop()
                self.play_button3.text = 'Play'
            else:
                self.sound3.play()
                self.play_button3.text = 'Pause'
   
    def update_slider3(self, dt):
        if self.sound3:
            self.slider3.value = self.sound3.get_pos() / self.sound3.length if self.sound3.length > 0 else 0
            self.remaining_time3 = self.sound3.length - self.sound3.get_pos()
            self.timer_label3.text = self.format_time(self.remaining_time3)
    def toggle_play_pause4(self, instance):
        if self.sound4:
            if self.sound4.state == 'play':
                self.sound4.stop()
                self.play_button4.text = 'Play'
            else:
                self.sound4.play()
                self.play_button4.text = 'Pause'
 
    def update_slider4(self, dt):
        if self.sound4:
            self.slider4.value = self.sound4.get_pos() / self.sound4.length if self.sound4.length > 0 else 0
            self.remaining_time4 = self.sound4.length - self.sound4.get_pos()
            self.timer_label4.text = self.format_time(self.remaining_time4)
    def format_time(self, seconds):
        minutes = int(seconds / 60)
        seconds = int(seconds % 60)
        return "{:02d}:{:02d}".format(minutes, seconds)
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
    def go_to_motivational(self, instance):
        # Switching to the library page screen
        motivational_screen = motivational.MotivationalScreen(name='motivational_page')
        self.parent.add_widget(motivational_screen)
        self.parent.current = 'motivational_page'
    def go_to_reminder(self, instance):
        # Switching to the library page screen
        reminder_screen = reminders.RemindersScreen(name='reminder_page')
        self.parent.add_widget(reminder_screen)
        self.parent.current = 'reminder_page'
    def logout(self, instance):
        self.parent.current = 'main'
 
class MyApp(App):
    def build(self):
        from kivy.uix.screenmanager import ScreenManager
        sm = ScreenManager()
        sm.add_widget(PodcastScreen(name='podcast_screen'))
        return sm
 
if __name__ == '__main__':
    MyApp().run()