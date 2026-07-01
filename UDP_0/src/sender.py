import socket
import json

HOST = "127.0.0.1"
PORT = 5005
    
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)



while True:
    print("======Choose Message Type: ========")
    print("1. Plain Text")
    print("2. JSON Telemetry")
    print("3. Exit")
    print("=====================================")

    choice = input("Enter choice : ")

    if choice == "1":
        msg = input("Message: ")
        sock.sendto(msg.encode(), (HOST, PORT))
        print("Text message sent.")

    elif choice == "2":
        device_name = input("Device name: ")
        device_type = input("Device type: ")
        temperature = input("Temperature: ")
        humidity = input("Humidity: ")
        latitude = input("Latitude: ")
        longitude = input("Longitude: ")

        packet = {
            "device_name": device_name, 
            "device_type": device_type, 
            "temperature": temperature, 
            "humidity": humidity, 
            "latitude": latitude, 
            "longitude": longitude
        }

        json_packet = json.dumps(packet)
        sock.sendto(json_packet.encode(), (HOST, PORT))
        print("Telemetry packet sent.")
    
    elif choice == "3":
        break
    else:
        print("Invalid choice")

sock.close()