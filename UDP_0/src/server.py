import socket
import json

from config import HOST, PORT
from database import save_telemetry, save_message
from models import initialize_database

initialize_database()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))
sock.settimeout(1)

print(f"UDP Server running on {HOST}: {PORT}")

try:
    while True:
        try:
            data, addr = sock.recvfrom(1024)
        except socket.timeout:
            continue
        
        message = data.decode()

        try:
            packet = json.loads(message)
            
            print("\n Telemetry Received: ")
            print(f"Device Name: {packet['device_name']}")
            print(f"Device Type: {packet['device_type']}")
            print(f"Temperature: {packet['temperature']}")
            print(f"Humidity: {packet['humidity']}")
            print(f"Latitude: {packet['latitude']}")
            print(f"Longitude: {packet['longitude']}")
            print(f"Sender: {addr[0]}: {addr[1]}")

            save_telemetry(
                packet['device_name'],
                packet['device_type'],
                packet['temperature'],
                packet['humidity'],
                packet['latitude'],
                packet['longitude'],
                addr[0], addr[1]
            )
        except json.JSONDecodeError:
            print("\nText Message: ")
            print(f"[{addr[0]}:{addr[1]}] {message}")
            save_message(addr[0], addr[1], message)

except KeyboardInterrupt:
    print("\nShutting down server...")

finally:
    sock.close()