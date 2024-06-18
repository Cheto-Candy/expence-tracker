import sqlite3

conn = sqlite3.connect('expenses.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY,
    date TEXT,
    category TEXT,
    description TEXT,
    amount REAL
)
''')

conn.commit()
conn.close()
