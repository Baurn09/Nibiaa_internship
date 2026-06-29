import sqlite3
from config import DATABASE

def save_message(ip, port, message):
    con = sqlite3.connect(DATABASE)

    con.execute("""
        INSERT INTO messages(sender_ip, sender_port, message) VALUES(?, ?, ?)
    """,[ip, port , message])
    con.commit()
    con.close()