import socket

from config import HOST, PORT
from database import save_message
from models import initialize_database

initialize_database()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

print(f"UDP Server running on {HOST}: {PORT}")

while True:
    data, addr = sock.recvfrom(1024)
    message = data.decode()

    print(f"[{addr[0]}: {addr[1]}] {message}")
    save_message(addr[0], addr[1], message)