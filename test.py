import sqlite3
import matplotlib.pyplot as plt

# Connect to the SQLite database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Define the user_id for which you want to retrieve data
user_id = 'n'

# Execute the SQL query to retrieve timestamp and mood data for the specified user_id
cursor.execute('SELECT timestamp, mood FROM moods WHERE acc_name = ? ORDER BY timestamp', (user_id,))
data = cursor.fetchall()

# Close the database connection
conn.close()

# Extract timestamp and mood data
timestamps, moods = zip(*data)

# Plot the data
plt.plot(timestamps, moods, marker='o', linestyle='-')
plt.xlabel('Timestamp')
plt.ylabel('Mood')
plt.title('Mood over Time for User ID: {}'.format(user_id))
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability if needed
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()