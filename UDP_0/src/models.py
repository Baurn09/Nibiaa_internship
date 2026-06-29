import sqlite3
from config import DATABASE

def initialize_database():
    con = sqlite3.connect(DATABASE)

    con.execute("""
        CREATE TABLE IF NOT EXISTS messages(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sender_ip TEXT,
                sender_port INTEGER, 
                message TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    con.commit()
    con.close()