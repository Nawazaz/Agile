import sqlite3
 
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
cursor.execute("SELECT * FROM moods")
rows = cursor.fetchall()

for row in rows:
    print(row)
#cursor.execute("DROP TABLE users")
#print("delete")
#conn.commit()
conn.close()

