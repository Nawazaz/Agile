import sqlite3
 
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)
#cursor.execute("DELETE FROM users")
#print("delete")
#conn.commit()
conn.close()
