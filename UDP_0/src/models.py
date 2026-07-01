import sqlite3
from config import DATABASE

def initialize_database():
    conn = sqlite3.connect(DATABASE)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS messages(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender_ip TEXT NOT NULL,
            sender_port INTEGER NOT NULL,
            message TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS telemetry(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                device_name TEXT NOT NULL,
                device_type TEXT NOT NULL, 
                temperature REAL NOT NULL,
                humidity INTEGER NOT NULL, 
                latitude REAL NOT NULL, 
                longitude REAL NOT NULL,
                sender_ip TEXT NOT NULL, 
                sender_port INTEGER NOT NULL, 
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()