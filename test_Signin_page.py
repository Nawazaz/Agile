import unittest
from kivy.tests.common import GraphicUnitTest
from kivy.base import EventLoop
from kivy.uix.screenmanager import ScreenManager

from Signin_page import SecondScreen

class TestSecondScreen(GraphicUnitTest):
    def setUp(self):
        self.screen_manager = ScreenManager()
        self.second_screen = SecondScreen(name='second')
        self.screen_manager.add_widget(self.second_screen)
        EventLoop.ensure_window()
        EventLoop.window.add_widget(self.screen_manager)

    def tearDown(self):
        EventLoop.window.remove_widget(self.screen_manager)

    def test_login_action_successful(self):
        self.second_screen.children[0].children[2].text = 'testuser'
        self.second_screen.children[0].children[1].text = 'testpassword'
        self.second_screen.login_action(None)
        self.assertEqual(self.screen_manager.current, 'home')

    def test_login_action_invalid_credentials(self):
        self.second_screen.children[0].children[2].text = 'invaliduser'
        self.second_screen.children[0].children[1].text = 'invalidpassword'
        self.second_screen.login_action(None)
        self.assertNotEqual(self.screen_manager.current, 'home')

if __name__ == '__main__':
    unittest.main()
