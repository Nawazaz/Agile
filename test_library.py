import unittest
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.base import EventLoop
from kivy.uix.button import Button
from kivy.uix.label import Label
from unittest.mock import patch

from library import BookButton, LibraryScreen

class MainScreen(Screen):
    pass

class TestLibraryScreen(unittest.TestCase):
    
    def setUp(self):
        EventLoop.ensure_window()
        self.sm = ScreenManager()
        self.library_screen = LibraryScreen(name='library')
        self.sm.add_widget(self.library_screen)
        
        self.main_screen = MainScreen(name='main')
        self.home_screen = Screen(name='home_page')
        self.motivational_screen = Screen(name='motivational_page')
        
        self.sm.add_widget(self.main_screen)
        self.sm.add_widget(self.home_screen)
        self.sm.add_widget(self.motivational_screen)

    def test_widget_count(self):
        self.assertEqual(len(self.library_screen.layout.children), 8)
    
    def test_labels(self):
        # Check if labels have correct text and properties
        labels = [child for child in self.library_screen.layout.children if isinstance(child, Label)]
        self.assertEqual(len(labels), 3)  # Including title labels for books
        label_texts = [label.text for label in labels]
        self.assertIn('Wellness\n     Bridge', label_texts)
        self.assertIn('Library', label_texts)

    def test_buttons(self):
        buttons = [child for child in self.library_screen.layout.walk(restrict=True) if isinstance(child, Button)]
        self.assertEqual(len(buttons), 3)
        button_texts = [button.text for button in buttons]
        self.assertIn('Logout', button_texts)
        self.assertIn('Home', button_texts)
        self.assertIn('Motivational Quotes', button_texts)

    def test_book_titles(self):
        # Check if the get_book_title method returns correct titles
        urls = [
            'https://m.media-amazon.com/images/I/718A6RecZKL._SY522_.jpg',
            'https://m.media-amazon.com/images/I/41o9P29YcqL._SY445_SX342_.jpg',
            'https://m.media-amazon.com/images/I/41nrmlG5N8L._SY445_SX342_.jpg',
            'https://m.media-amazon.com/images/I/51SPsmOpFDL._SY445_SX342_.jpg',
            'https://m.media-amazon.com/images/I/51vlZnkzi9L._SY445_SX342_.jpg',
            'https://m.media-amazon.com/images/I/81HV21Pq+cL._SY522_.jpg'
        ]
        titles = [
            'Understanding mental illness',
            'What happened to you',
            "It didn't start with you",
            'Stop overthinking',
            'Burnout',
            'Unwinding anxiety'
        ]
        for url, title in zip(urls, titles):
            self.assertEqual(self.library_screen.get_book_title(url), title)

    @patch('webbrowser.open')
    def test_open_book(self, mock_open):
        book_button = BookButton(source='https://m.media-amazon.com/images/I/718A6RecZKL._SY522_.jpg')
        self.library_screen.open_book(book_button)
        mock_open.assert_called_with('http://www.mentalhealthpromotion.net/resources/understanding-mental-illnesses.pdf')

    def test_navigation(self):
        home_button = next((child for child in self.library_screen.layout.walk() if isinstance(child, Button) and child.text == 'Home'), None)
        motivational_button = next((child for child in self.library_screen.layout.walk() if isinstance(child, Button) and child.text == 'Motivational Quotes'), None)

        self.assertIsNotNone(home_button)
        self.assertIsNotNone(motivational_button)

        self.library_screen.go_to_home(home_button)
        self.assertEqual(self.sm.current, 'home_page')

        self.library_screen.go_to_motivational(motivational_button)
        self.assertEqual(self.sm.current, 'motivational_page')

    def test_logout(self):
        logout_button = next((child for child in self.library_screen.layout.walk() if isinstance(child, Button) and child.text == 'Logout'), None)
        self.assertIsNotNone(logout_button)
        self.library_screen.logout(logout_button)
        self.assertEqual(self.sm.current, 'main')

if __name__ == '__main__':
    unittest.main()
