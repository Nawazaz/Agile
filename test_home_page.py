import unittest
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.base import EventLoop
from kivy.clock import Clock

from home_page import HomePage  
import library
import motivational

class TestApp(App):
    def build(self):
        self.screen_manager = ScreenManager()
        self.home_page = HomePage(name='home')
        self.screen_manager.add_widget(self.home_page)
        
       
        main_screen = Screen(name='main')
        self.screen_manager.add_widget(main_screen)
        
        return self.screen_manager

class HomePageTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        EventLoop.ensure_window()
        cls.test_app = TestApp()
        Clock.schedule_once(lambda dt: cls.test_app.stop(), 0)  # Stop the app immediately after starting
        cls.test_app.run()
        cls.test_app = TestApp()
        cls.test_app.build()  # Build the app without running the main loop

    def setUp(self):
        self.screen_manager = self.test_app.screen_manager
        self.home_page = self.test_app.home_page

    def test_initial_layout(self):
        for child in self.home_page.children:
            print(type(child), child)

        # Check if the background image is correctly added
        background = self.home_page.children[0].children[-1]  
        self.assertIsInstance(background, Image)
        self.assertEqual(background.source, 'Pic/homeimg.png')

        home_label = self.home_page.children[0].children[-2]
        self.assertIsInstance(home_label, Image)
        self.assertEqual(home_label.source, 'Pic/Logo.png')

        wellness_label = self.home_page.children[0].children[-3]
        self.assertIsInstance(wellness_label, Label)
        self.assertEqual(wellness_label.text, 'Wellness\n     Bridge')

        # Check if the description text is correctly added
        description_text = self.home_page.children[0].children[-4]
        self.assertIsInstance(description_text, Label)
        self.assertIn('Wellness Bridge is a revolutionary app', description_text.text)

    def test_library_button(self):
        library_button = self.home_page.children[0].children[-6].children[0]  
        self.assertIsInstance(library_button, Button)
        library_button.trigger_action(duration=0.1)

        self.assertEqual(self.screen_manager.current, 'library')

    def test_motivational_button(self):
        quotes_button = self.home_page.children[0].children[-7].children[0] 
        self.assertIsInstance(quotes_button, Button)
        
        # Simulate pressing the button using Kivy's clock to ensure it's within the event loop
        Clock.schedule_once(lambda dt: quotes_button.trigger_action(duration=0.1), 0)
        Clock.schedule_once(lambda dt: self.assertEqual(self.screen_manager.current, 'motivational'), 0.2)

    def test_logout_button(self):
        logout_button = self.home_page.children[0].children[-8]
        self.assertIsInstance(logout_button, Button)
        
     
        Clock.schedule_once(lambda dt: logout_button.trigger_action(duration=0.1), 0)
        Clock.schedule_once(lambda dt: self.assertEqual(self.screen_manager.current, 'main'), 0.2)

if __name__ == '__main__':
    unittest.main()
