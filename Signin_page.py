from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.app import App
import sqlite3
import home_page

acc_name = ''

class NewPage(Screen):
    pass

class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super(SecondScreen, self).__init__(**kwargs)
        layout = FloatLayout()

        background = Image(source='Pic/bg.jpg', allow_stretch=True, keep_ratio=False)
        layout.add_widget(background)

        wellness_bridge_label = Label(text='Wellness Bridge', pos_hint={'x': 0.04, 'top': 0.99}, size_hint=(None, None), size=(200, 50), font_name="fonts/BreeSerif-Regular.ttf", italic=True, font_size=40, color=(0.071, 0.078, 0.506, 1))
        layout.add_widget(wellness_bridge_label)

        center_image = Image(source='Pic/left.jpg', allow_stretch=True, keep_ratio=False, size_hint=(None, None), size=(400, 400), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(center_image)

        self.username_input = TextInput(hint_text='Username', multiline=False, size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.5, 'center_y': 0.6})
        self.password_input = TextInput(hint_text='Password', multiline=False, password=True, size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        login_button = Button(text='Login', size_hint=(None, None), size=(100, 50), pos_hint={'center_x': 0.5, 'center_y': 0.43}, font_name="fonts/BreeSerif-Regular.ttf")
        login_button.bind(on_press=self.login_action)
        layout.add_widget(self.username_input)
        layout.add_widget(self.password_input)
        layout.add_widget(login_button)

        self.add_widget(layout)

    def login_action(self, instance):
        username = self.username_input.text
        password = self.password_input.text
        conn = sqlite3.connect('example.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE name = ? AND password = ?", (username, password))
        data = cursor.fetchone()  
        conn.close()

        if data:
            print("Authentication successful. User:", username)
            acc_name = username
            print('in signin page', acc_name)
            # Assuming home_page.py defines a class named HomePage
            home_screen = home_page.HomePage(name='home', acc_name=acc_name)
            self.parent.add_widget(home_screen)
            self.parent.current = 'home'
        else:
            print("Please enter valid Name or Password.")

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        second_screen = SecondScreen(name='second')
        sm.add_widget(second_screen)
        return sm

if __name__ == '__main__':
    MyApp().run()