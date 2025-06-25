import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute('''
    CREATE TABLE rides (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        origin TEXT,
        destination TEXT,
        time TEXT,
        contact TEXT
    )
''')
conn.commit()
conn.close()
