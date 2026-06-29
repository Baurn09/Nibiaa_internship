import socket

HOST = "127.0.0.1"
PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input("Message: ")
    sock.sendto(msg.encode(), (HOST, PORT))

    if msg.lower() == "exit":
        break