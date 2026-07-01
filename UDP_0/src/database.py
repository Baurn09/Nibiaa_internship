import sqlite3
from config import DATABASE

def save_message(ip, port, message):
    conn = sqlite3.connect(DATABASE)

    conn.execute("""
        INSERT INTO messages(sender_ip, sender_port, message)
        VALUES (?, ?, ?)
    """, (ip, port, message))

    conn.commit()
    conn.close()

def save_telemetry(dev_name, dev_type, temp, humi, lat, lon, ip, port):
    conn = sqlite3.connect(DATABASE)

    conn.execute("""
        INSERT INTO telemetry(device_name, device_type, temperature, humidity, latitude, longitude, sender_ip, sender_port) VALUES(?, ?, ?, ?, ?, ?, ?, ?)
    """,[dev_name, dev_type, temp, humi, lat, lon, ip, port])
    conn.commit()
    conn.close()