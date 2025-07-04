import sqlite3

#connecting to sqlite database
connection_obj = sqlite3.connect('geek.db')

#cursor object
cursor_obj = connection_obj.cursor()


cursor_obj.execute("""
CREATE TABLE IF NOT EXISTS GEEK(
    Email varchar(255) PRIMARY KEY,
    Name varchar(50),
    Score int
);
""")

data = [
    ("geekk1@gmail.com", "Geek1", 25),
    ("geekk2@gmail.com", "Geek2", 15),
    ("geekk3@gmail.com", "Geek3", 36),
    ("geekk4@gmail.com", "Geek4", 27),
    ("geekk5@gmail.com", "Geek5", 40),
    ("geekk6@gmail.com", "Geek6", 36),
    ("geekk7@gmail.com", "Geek7", 27)
]

# Insert data only if not already present
try:
    cursor_obj.executemany(
        "INSERT OR IGNORE INTO GEEK (Email, Name, Score) VALUES (?, ?, ?)", data
    )
except sqlite3.IntegrityError as e:
    print(f"IntegrityError: {e}")
except sqlite3.OperationalError as e:
    print(f"OperationalError: {e}")
except Exception as e:
    print(f"Error: {e}")

connection_obj.commit()

# View all data in the GEEK table
print("\nCurrent data in GEEK table:")
for row in cursor_obj.execute("SELECT * FROM GEEK"):
    print(row)

#close the connection
connection_obj.close()