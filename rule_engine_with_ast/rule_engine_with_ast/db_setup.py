# db_setup.py

import sqlite3

def create_table():
    conn = sqlite3.connect('rules.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rule_name TEXT,
            rule_string TEXT
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()
    print("Database setup complete.")
