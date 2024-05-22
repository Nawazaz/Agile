from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
import library
import motivational
import reminders
import podcast
import sqlite3
from datetime import datetime
import matplotlib.pyplot as plt

class HomePage(Screen):
    def __init__(self, acc_name='', **kwargs):
        super(HomePage, self).__init__(**kwargs)
        self.acc_name = acc_name  # Store the acc_name

        self.layout = FloatLayout()
        
        # Add background image
        background = Image(source='Pic/homeimg.png', allow_stretch=True, keep_ratio=False)
        self.layout.add_widget(background)
        
        # Add text "Home" at the top center
        home_label = Image(source='Pic/Logo.png', size_hint=(None, None), size=(300, 150), pos_hint={'left': 2, 'top': 1})  # Black color
        self.layout.add_widget(home_label)
        
        # Add "Wellness bridge" label on the left image
        wellness_label = Label(text='Wellness\n     Bridge', size_hint=(None, None), size=(300, 50), 
                            pos_hint={'right': 0.87, 'top': 0.6}, font_size=135, 
                            color=(0.071, 0.078, 0.506, 1),  # Navy blue color
                            text_size=(None, None), halign='left', 
                            font_name="fonts/BreeSerif-Regular.ttf")
        self.layout.add_widget(wellness_label)

        # Add description text below Wellness Bridge
        description_text = Label(text='Wellness Bridge is a revolutionary app designed to\n empower individuals with mental health issues\n by providing a supportive community platform\n and comprehensive resources for holistic\n well being.',
                                size_hint=(None, None), size=(800, 100), 
                                pos_hint={'right': 1, 'top': 0.3}, 
                                font_size=24, color=(0, 0, 0, 1),  # Black color
                                text_size=(None, None), halign='left', font_name="fonts/BreeSerif-Regular.ttf")
        self.layout.add_widget(description_text)

        main_image = Image(source='Pic/hmbg.png', size_hint=(None, None), size=(1000, 1000), pos_hint={'left': 0, 'bottom': 2}, allow_stretch=True)
        self.layout.add_widget(main_image)

        
        # Create a BoxLayout for Library
        library_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.5, 'top': 0.97})
        
        # Add Library button
        library_button = Button(text='Library', size_hint=(None, None), size=(200, 50), font_size=23, background_color=(0, 0, 0, 0), color=(0, 0, 0, 1), font_name="fonts/BreeSerif-Regular.ttf")  # Transparent background
        library_button.bind(on_press=self.go_to_library)
        library_layout.add_widget(library_button)
        
        self.layout.add_widget(library_layout)
        
        # Create a BoxLayout for Motivational quotes
        quotes_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(300, 50), pos_hint={'right': 0.68 , 'top': 0.97})
        
        # Add Motivational quotes button
        quotes_button = Button(text='Motivational quotes', size_hint=(None, None), size=(200, 50), font_size=23, background_color=(0, 0, 0, 0), color=(0, 0, 0, 1), font_name="fonts/BreeSerif-Regular.ttf")
        quotes_button.bind(on_press=self.go_to_motivational)
        quotes_layout.add_widget(quotes_button)
        
        self.layout.add_widget(quotes_layout)
        
        # Create a BoxLayout for reminders
        reminders_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.71 , 'top': 0.97})
       
        # Add reminders button
        reminders_button = Button(text='Reminders', size_hint=(None, None), size=(200, 50), font_size=23, background_color=(0, 0, 0, 0), color=(0, 0, 0, 1), font_name="fonts/BreeSerif-Regular.ttf")
        reminders_button.bind(on_press=self.go_to_reminders)
        reminders_layout.add_widget(reminders_button)
       # Create a BoxLayout for podcast
        podcast_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.42, 'top': 0.97})
       
        # Add Podcast button
        podcast_button = Button(text='Podcast', size_hint=(None, None), size=(200, 50), font_size=23, background_color=(0, 0, 0, 0), color=(0, 0, 0, 1),font_name="fonts/BreeSerif-Regular.ttf")
        podcast_button.bind(on_press=self.go_to_podcast)
        podcast_layout.add_widget(podcast_button)
       
        analytics_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.79, 'top': 0.97})

        analytics_button = Button(text='Analytics', size_hint=(None, None), size=(200, 50), font_size=23, background_color=(0, 0, 0, 0), color=(0, 0, 0, 1),font_name="fonts/BreeSerif-Regular.ttf")
        analytics_button.bind(on_press=self.show_graph)
        analytics_layout.add_widget(analytics_button)

        self.layout.add_widget(analytics_layout)
        self.layout.add_widget(podcast_layout)
        self.layout.add_widget(reminders_layout)

        # Add logout button
        logout_button = Button(text='Logout', size_hint=(None, None), size=(100, 50), pos_hint={'right': 0.95, 'top': 0.97}, font_size=18, background_color=(1, 0.5, 0, 1), font_name="fonts/BreeSerif-Regular.ttf")
        logout_button.bind(on_press=self.logout)
        self.layout.add_widget(logout_button)
        
        username_label = Label(text=f'{self.acc_name}', size_hint=(None, None), size=(200, 50), pos_hint={'right': 0.89, 'top': 0.97}, font_size=16, color=(0, 0, 0, 1))
        self.layout.add_widget(username_label)

        self.add_widget(self.layout)

        # Show mood popup after sign-in
        self.show_mood_popup()
    
    def show_graph(self, instance):
        # Connect to the SQLite database
        conn = sqlite3.connect('example.db')
        cursor = conn.cursor()

        # Define the user_id for which you want to retrieve data
        user_id = self.acc_name

        # Execute the SQL query to retrieve timestamp and mood data for the specified user_id
        cursor.execute('SELECT timestamp, mood FROM moods WHERE acc_name = ? ORDER BY timestamp', (user_id,))
        data = cursor.fetchall()

        # Close the database connection
        conn.close()

        if data:
            # Extract timestamp and mood data
            timestamps, moods = zip(*data)

            # Plot the data
            plt.figure()
            plt.plot(timestamps, moods, marker='o', linestyle='-')
            plt.xlabel('Timestamp')
            plt.ylabel('Mood')
            plt.title('Mood over Time for User ID: {}'.format(user_id))
            plt.xticks(rotation=45)  # Rotate x-axis labels for better readability if needed
            plt.tight_layout()  # Adjust layout to prevent clipping of labels

            # Save the plot as an image file
            plot_path = 'mood_plot.png'
            plt.savefig(plot_path)
            plt.close()

            # Display the plot image in the Kivy application
            if hasattr(self, 'plot_image'):
                self.layout.remove_widget(self.plot_image)

            self.plot_image = Image(source=plot_path, size_hint=(0.8, 0.8), pos_hint={'center_x': 0.5, 'center_y': 0.3})
            self.layout.add_widget(self.plot_image)

            # Add Close Graph button
            self.close_graph_button = Button(text='Close Graph', size_hint=(None, None), size=(150, 50), pos_hint={'center_x': 0.5, 'center_y': 0.2}, font_size=20, background_color=(1, 0, 0, 1), font_name="fonts/BreeSerif-Regular.ttf")
            self.close_graph_button.bind(on_press=self.close_graph)
            self.layout.add_widget(self.close_graph_button)
        else:
            # Display a message if no data is found
            no_data_label = Label(text='No mood data available', size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5, 'center_y': 0.3}, font_size=20, color=(1, 0, 0, 1))
            self.layout.add_widget(no_data_label)

    def close_graph(self, instance):
        if hasattr(self, 'plot_image'):
            self.layout.remove_widget(self.plot_image)
            del self.plot_image

        if hasattr(self, 'close_graph_button'):
            self.layout.remove_widget(self.close_graph_button)
            del self.close_graph_button
    def show_mood_popup(self):
        # Create the content for the popup
        popup_content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        popup_content.add_widget(Label(text='How are you feeling today?', color=(0, 0, 0, 1)))

        # Create a BoxLayout for the emojis
        emoji_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint=(None, None), height=100)
        emoji_layout.bind(minimum_width=emoji_layout.setter('width'))

        # Add emoji buttons
        moods = ['happy', 'sad', 'neutral']  # List of moods
        for mood in moods:
            btn = Button(size_hint=(None, None), size=(100, 100), background_normal=f'Pic/{mood}.png', background_down=f'Pic/{mood}_down.png')
            btn.bind(on_press=self.on_mood_selected)
            btn.mood = mood  # Assign the mood to the button
            emoji_layout.add_widget(btn)

        popup_content.add_widget(emoji_layout)

        # Create the popup
        self.mood_popup = Popup(title='Mood Check', content=popup_content, size_hint=(0.7, 0.3), auto_dismiss=False,
                                background='rounded_background.png', background_color=(1, 1, 1, 0.7))

        # Center the emoji layout within the popup
        emoji_layout.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        # Open the popup
        self.mood_popup.open()

    # Function to initialize the database and create the table if it doesn't exist
    def init_db():
        conn = sqlite3.connect('example.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS moods (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                acc_name TEXT, 
                mood TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        conn.close()

    # Call the function to initialize the database
    init_db()
    
    def on_mood_selected(self, instance):
        selected_mood = instance.mood
        print(f"Mood selected: {selected_mood}")
        self.insert_mood_data(selected_mood)
        self.mood_popup.dismiss()  # Close the popup after mood selection


    def insert_mood_data(self, mood):
        conn = sqlite3.connect('example.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO moods (acc_name, mood, timestamp)
            VALUES (?, ?, ?)
        ''', (self.acc_name, mood, datetime.now()))
        
        conn.commit()
        conn.close()

    def go_to_library(self, instance):
        # Switching to the library screen
        library_screen = library.LibraryScreen(name='library')
        self.parent.add_widget(library_screen)
        self.parent.current = 'library'
    
    def go_to_motivational(self, instance):
        # Switching to the motivational screen
        motivational_screen = motivational.MotivationalScreen(name='motivational')
        self.parent.add_widget(motivational_screen)
        self.parent.current = 'motivational'
    
    def logout(self, instance):
        # Switching back to the main screen
        self.parent.current = 'main'
    
    def go_to_reminders(self, instance):
        # Switching to the reminders screen
        reminders_screen = reminders.RemindersScreen(name='reminders')
        self.parent.add_widget(reminders_screen)
        self.parent.current = 'reminders'
    
    def go_to_podcast(self, instance):
        # Switching to the podcast screen
        podcast_screen = podcast.PodcastScreen(name='podcast')
        self.parent.add_widget(podcast_screen)
        self.parent.current = 'podcast'

if __name__ == '__main__':
    from kivy.base import runTouchApp
    from kivy.uix.screenmanager import ScreenManager

    # Create the screen manager
    sm = ScreenManager()
    sm.add_widget(HomePage(name='home'))
    #home_page = HomePage(account_name=account_name, name='home')
    #sm.add_widget(home_page)
    runTouchApp(sm)