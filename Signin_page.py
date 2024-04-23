from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.app import App

class NewPage(Screen):
    pass

class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super(SecondScreen, self).__init__(**kwargs)
        layout = FloatLayout()

        background = Image(source='bg.jpg', allow_stretch=True, keep_ratio=False)
        layout.add_widget(background)

        wellness_bridge_label = Label(text='Wellness Bridge', pos_hint={'x': 0.01, 'top': 0.99}, size_hint=(None, None), size=(200, 50), font_name='Arial', italic=True, font_size=25)
        layout.add_widget(wellness_bridge_label)

        center_image = Image(source='left.jpg', allow_stretch=True, keep_ratio=False, size_hint=(None, None), size=(400, 400), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(center_image)

        username_input = TextInput(hint_text='Username', multiline=False, size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.5, 'center_y': 0.6})
        password_input = TextInput(hint_text='Password', multiline=False, password=True, size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        login_button = Button(text='Login', size_hint=(None, None), size=(100, 50), pos_hint={'center_x': 0.5, 'center_y': 0.4})
        login_button.bind(on_press=self.login_action)
        layout.add_widget(username_input)
        layout.add_widget(password_input)
        layout.add_widget(login_button)

        self.add_widget(layout)

    def login_action(self, instance):
        User = self.children[0].children[2]
        Pswrd = self.children[0].children[1]
        if User.text and Pswrd.text:
            new_page = NewPage(name='new_page')
            self.parent.add_widget(new_page)
            self.parent.current = 'new_page'
        else:
            print("Please fill both username and password.")

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        second_screen = SecondScreen(name='second')
        sm.add_widget(second_screen)
        return sm

if __name__ == '__main__':
    MyApp().run()
