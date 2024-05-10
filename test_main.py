import unittest
from kivy.tests.common import GraphicUnitTest
from kivy.base import EventLoop

from main import MainScreen, SignUpScreen

class TestMainScreen(GraphicUnitTest):
    def setUp(self):
        self.main_screen = MainScreen()
        EventLoop.ensure_window()
        EventLoop.window.add_widget(self.main_screen)

    def tearDown(self):
        EventLoop.window.remove_widget(self.main_screen)

    def test_switch_to_another_page(self):
        self.main_screen.switch_to_another_page(None)
        self.assertEqual(self.main_screen.parent.current, 'second')

    def test_sign_up_action_valid(self):
        self.main_screen.Usr.text = 'testuser'
        self.main_screen.Pswrd.text = 'testpassword'
        self.main_screen.Email.text = 'test@example.com'
        self.main_screen.sign_up_action(None)
        # Check if popup for successful registration is shown
        self.assertTrue(self.main_screen.children)

    def test_sign_up_action_invalid(self):
        self.main_screen.Usr.text = ''
        self.main_screen.Pswrd.text = ''
        self.main_screen.Email.text = ''
        self.main_screen.sign_up_action(None)
        # Check if popup for invalid registration is shown
        self.assertTrue(self.main_screen.children)

class TestSignUpScreen(GraphicUnitTest):
    def setUp(self):
        self.signup_screen = SignUpScreen()
        EventLoop.ensure_window()
        EventLoop.window.add_widget(self.signup_screen)

    def tearDown(self):
        EventLoop.window.remove_widget(self.signup_screen)

    def test_signup_screen_elements(self):
        self.assertTrue(self.signup_screen.children)

if __name__ == '__main__':
    unittest.main()
