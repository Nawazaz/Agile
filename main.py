from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from Signin_page import SecondScreen
import sqlite3
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT NOT NULL, password  TEXT NOT NULL, email  TEXT NOT NULL)''')
conn.commit()

class BackgroundApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.main_screen = MainScreen(name='main')
        self.signup_screen = SignUpScreen(name='signup')
        self.Signin_page = SecondScreen(name='second')
        self.sm.add_widget(self.main_screen) 
        self.sm.add_widget(self.signup_screen)
        self.sm.add_widget(self.Signin_page)
        return self.sm

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        layout = FloatLayout()

        background = Image(source='Pic/antoine-rault-IhWRrZx4-kk-unsplash.jpg', allow_stretch=True, keep_ratio=False)
        layout.add_widget(background)

        App_txt = Label(text='Wellness Bridge', pos_hint={'x': 0.04, 'top': 0.99}, size_hint=(None, None), size=(200, 50), font_name="fonts/BreeSerif-Regular.ttf", italic=True, font_size=40, color=(0.071, 0.078, 0.506, 1))
        layout.add_widget(App_txt)

        images_layout = BoxLayout(pos_hint={'center_x': 0.515, 'center_y': 0.64}, size_hint=(None, None), size=(1112, 763))
        
        Left_img = Image(source='Pic/left.jpg', size_hint=(None, None), size=(500, 500), allow_stretch=True, keep_ratio=False)
        
        LeftImageText_1 = Label(text='Welcome Back!', pos=(430, 600), font_size=55, italic=True, color=(0, 0, 0, 1), size_hint=(None, None), size=(500, 50), halign='center', font_name="fonts/SedanSC-Regular.ttf")

        LeftImageText_2 = Label(text='To keep connected with us', pos=(425, 520), font_size=30, color=(0, 0, 0, 1), size_hint=(None, None), size=(500, 45), halign='center', font_name= "fonts/Pacifico-Regular.ttf")

        LeftImageText_3 = Label(text='please login with your personal info', pos=(430, 488), font_size=30, color=(0, 0, 0, 1), size_hint=(None, None), size=(500, 45), halign='center', font_name= "fonts/Pacifico-Regular.ttf")

        Signin_Btn = Button(text='Sign in', size_hint=(None, None), size=(100, 50), pos=(625, 400), font_name="fonts/BreeSerif-Regular.ttf")
        Signin_Btn.bind(on_press=self.switch_to_another_page)

        Left_img.add_widget(LeftImageText_1)
        Left_img.add_widget(LeftImageText_2)
        Left_img.add_widget(LeftImageText_3)
        Left_img.add_widget(Signin_Btn)

        images_layout.add_widget(Left_img)

        Right_img = Image(source='Pic/right.png', size_hint=(None, None), size=(500, 500), allow_stretch=True, keep_ratio=False)
        
        create_account_label = Label(text='Create Account', pos=(1050, 700), font_size=30, color=(0, 0, 0, 1), size_hint=(None, None), size=(250, 50), halign='center', font_name="fonts/SedanSC-Regular.ttf")
        self.Usr = TextInput(hint_text='Username', multiline=False, pos=(1035, 610), size_hint=(None, None), size=(300, 50))
        self.Pswrd = TextInput(hint_text='Password', multiline=False, password=True, pos=(1035, 550), size_hint=(None, None), size=(300, 50))
        self.Email = TextInput(hint_text='Email', multiline=False, input_type='text', pos=(1035, 490), size_hint=(None, None), size=(300, 50))
       
        Signup_Btn = Button(text='Sign up', size_hint=(None, None), size=(100, 50), pos=(1125, 400), font_name="fonts/BreeSerif-Regular.ttf")
        Signup_Btn.bind(on_press=self.sign_up_action)

        Right_img.add_widget(create_account_label)
        Right_img.add_widget(self.Usr)
        Right_img.add_widget(self.Pswrd)
        Right_img.add_widget(self.Email)
        Right_img.add_widget(Signup_Btn)

        images_layout.add_widget(Right_img)
        layout.add_widget(images_layout)
        self.add_widget(layout)

    def switch_to_another_page(self, instance):
        self.parent.current = 'second'

    def sign_up_action(self, instance):
        if self.Usr.text and self.Pswrd.text and self.Email.text:
            conn = sqlite3.connect('example.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (name, password, email) VALUES (?,?,?)", (self.Usr.text, self.Pswrd.text, self.Email.text))
            conn.commit()
            conn.close()
 
            popup = Popup(title='Registration Success',
                          content=Label(text="Thank you for registering, please sign in now"),
                          size_hint=(None, None), size=(400, 200))
            popup.open()
        else:
             popup = Popup(title='Sign up failed',
                          content=Label(text="Please enter valid name,password or email"),
                          size_hint=(None, None), size=(400, 200))
             popup.open()

class SignUpScreen(Screen):
    def __init__(self, **kwargs):
        super(SignUpScreen, self).__init__(**kwargs)
        layout = FloatLayout()
        sign_up_label = Label(text='Sign Up Page', pos_hint={'center_x': 0.5, 'center_y': 0.9}, font_size=30)
        layout.add_widget(sign_up_label)
        self.add_widget(layout)

if __name__ == "__main__":
    BackgroundApp().run()
conn.commit()
conn.close()