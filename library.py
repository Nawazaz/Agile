from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import AsyncImage
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import home_page
import motivational
import webbrowser
from kivy.uix.behaviors import ButtonBehavior

class BookButton(ButtonBehavior, AsyncImage):
    pass

class LibraryScreen(Screen):
    def __init__(self, **kwargs):
        super(LibraryScreen, self).__init__(**kwargs)
       
        self.layout = FloatLayout()
       
        # Add background image
        background = Image(source='Pic/homebg.png', allow_stretch=True, keep_ratio=False)
        self.layout.add_widget(background)
       
        # Add text "Library" at the top center
        library_label = Label(text='Library', size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.5, 'top': 1}, font_size=30, color=(0, 0, 0, 1), font_name="fonts/BreeSerif-Regular.ttf")
        self.layout.add_widget(library_label)
       
        left_image = Image(source='Pic/homeimg.png', size_hint=(None, None), size=(400, 1080), pos_hint={'left': 1})
        self.layout.add_widget(left_image)
       
        # Add book covers and titles to the scrollview
        scrollview = ScrollView(size_hint=(None, None), size=(800, 800), pos_hint={'center_x': 0.5, 'center_y': 0.5}) # Add a scrollview to contain the books
        books_layout = GridLayout(cols=1, spacing=10, size_hint_y=None) # Grid layout to contain the book covers and titles
        books_layout.bind(minimum_height=books_layout.setter('height'))
        
        book_cover_urls = [
            'https://m.media-amazon.com/images/I/718A6RecZKL._SY522_.jpg',
            'https://m.media-amazon.com/images/I/41o9P29YcqL._SY445_SX342_.jpg',
            'https://m.media-amazon.com/images/I/41nrmlG5N8L._SY445_SX342_.jpg',
            'https://m.media-amazon.com/images/I/51SPsmOpFDL._SY445_SX342_.jpg',
            'https://m.media-amazon.com/images/I/51vlZnkzi9L._SY445_SX342_.jpg',
            'https://m.media-amazon.com/images/I/81HV21Pq+cL._SY522_.jpg'
        ]
        
        for url in book_cover_urls:
            book_button = BookButton(source=url, size_hint_y=None, height=300)
            book_button.bind(on_release=self.open_book)  # Bind the button to open the book
            books_layout.add_widget(book_button)
            
            # Add book titles
            title_label = Label(text=self.get_book_title(url), size_hint_y=None, height=50, font_size=18, color=(0, 0, 0, 1), font_name="fonts/BreeSerif-Regular.ttf")
            books_layout.add_widget(title_label)
           
        scrollview.add_widget(books_layout) # Add the books layout to the scroll view
        
        self.layout.add_widget(scrollview)
       
        motivational_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(300, 50), pos_hint={'left': 1, 'top': 0.6})
       
        # Add Motivational Quotes image
        motivational_image = Image(source='Pic/graduationcap.png', size_hint=(None, None), size=(50, 50))
        motivational_layout.add_widget(motivational_image)
       
        # Add Motivational quotes button
        motivational_button = Button(text='Motivational Quotes', size_hint=(None, None), size=(250, 50), font_size=23, background_color=(0, 0, 0, 0), color=(0, 0, 0, 1), font_name="fonts/SedanSC-Regular.ttf")  # Transparent background
        motivational_button.bind(on_press=self.go_to_motivational)
        motivational_layout.add_widget(motivational_button)
       
        Home_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(300, 50), pos_hint={'left': 1, 'top': 0.67})
       
        # Add Home image
        Home_image = Image(source='Pic/homeicon.png', size_hint=(None, None), size=(50, 50))
        Home_layout.add_widget(Home_image)
       
        # Add Home button
        Home_button = Button(text='Home', size_hint=(None, None), size=(200, 50), font_size=23, background_color=(0, 0, 0, 0), color=(0, 0, 0, 1), font_name="fonts/SedanSC-Regular.ttf")  # Transparent background
        Home_button.bind(on_press=self.go_to_home)
        Home_layout.add_widget(Home_button)
       
        # Add logout button
        logout_button = Button(text='Logout', size_hint=(None, None), size=(100, 50), pos_hint={'right': 0.95, 'top': 0.97}, font_size=18, background_color=(1, 0.5, 0, 1), font_name="fonts/BreeSerif-Regular.ttf")
        logout_button.bind(on_press=self.logout)
        self.layout.add_widget(logout_button)

        self.layout.add_widget(motivational_layout)
        self.layout.add_widget(Home_layout)
        
        self.add_widget(self.layout)
       
    def open_book(self, instance):
        # Define a dictionary mapping book covers to their corresponding PDF URLs
        book_cover_to_pdf = {
            'https://m.media-amazon.com/images/I/718A6RecZKL._SY522_.jpg': 'http://www.mentalhealthpromotion.net/resources/understanding-mental-illnesses.pdf',
            'https://m.media-amazon.com/images/I/41o9P29YcqL._SY445_SX342_.jpg': 'file:///C:/Users/SAKH0032/Desktop/What%20Happened%20to%20You_%20-%20Oprah%20Winfrey.pdf',
            'https://m.media-amazon.com/images/I/41nrmlG5N8L._SY445_SX342_.jpg': "file:///C:/Users/SAKH0032/Desktop/It%20Didn't%20Start%20With%20You.pdf",
            'https://m.media-amazon.com/images/I/51SPsmOpFDL._SY445_SX342_.jpg': 'https://cdn.bookey.app/files/pdf/book/en/stop-overthinking.pdf',
            'https://m.media-amazon.com/images/I/51vlZnkzi9L._SY445_SX342_.jpg': 'https://books.yappe.in/pdf/65b5e0fff68f2195c01ac685.pdf',
            'https://m.media-amazon.com/images/I/81HV21Pq+cL._SY522_.jpg': 'https://static.fnac-static.com/multimedia/PT/pdf/9781785043635.pdf'
        }
        # Get the URL of the clicked book cover
        book_cover_url = instance.source
 
        # Look up the corresponding PDF URL in the dictionary
        pdf_url = book_cover_to_pdf.get(book_cover_url)
 
        # Open the PDF URL
        if pdf_url:
            webbrowser.open(pdf_url)
 
    def go_to_home(self, instance):
        # Switching to the home page screen
        home_screen = home_page.HomePage(name='home_page')
        self.parent.add_widget(home_screen)
        self.parent.current = 'home_page'
       
    def go_to_motivational(self, instance):
        # Switching to the motivational quotes page screen
        motivational_screen = motivational.MotivationalScreen(name='motivational_page')
        self.parent.add_widget(motivational_screen)
        self.parent.current = 'motivational_page'
   
    def logout(self, instance):
        # Switching back to the main screen
        self.parent.current = 'main'
    
    def get_book_title(self, url):
        # Define a dictionary mapping book covers to their corresponding titles
        book_titles = {
            'https://m.media-amazon.com/images/I/718A6RecZKL._SY522_.jpg': 'Understanding mental illness',
            'https://m.media-amazon.com/images/I/41o9P29YcqL._SY445_SX342_.jpg': 'What happened to you',
            'https://m.media-amazon.com/images/I/41nrmlG5N8L._SY445_SX342_.jpg': "It didn't start with you",
            'https://m.media-amazon.com/images/I/51SPsmOpFDL._SY445_SX342_.jpg': 'Stop overthinking',
            'https://m.media-amazon.com/images/I/51vlZnkzi9L._SY445_SX342_.jpg': 'Burnout',
            'https://m.media-amazon.com/images/I/81HV21Pq+cL._SY522_.jpg': 'Unwinding anxiety'
        }
        # Get the title corresponding to the provided URL
        return book_titles.get(url, 'Unknown Title')
