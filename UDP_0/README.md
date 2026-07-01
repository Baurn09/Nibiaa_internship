# UDP_0

A simple Python-based UDP server implementation built to understand the fundamentals of connectionless networking. This task demonstrates how a UDP server listens for incoming datagrams, processes received messages, and stores them in a local SQLite database.

## Objective

The goal of this project is to learn the basics of UDP communication by implementing:

* A UDP server that listens for incoming messages.
* A UDP client (sender) that transmits messages.
* A SQLite database for storing received data.
* A modular Python project structure that can be extended in the future.

---

## Features

* UDP socket communication
* Receive plain text messages
* Store received messages in SQLite
* Modular project architecture
* Easy to extend with codecs, logging, and custom protocols

---

## Project Structure

```
udp-server/
│
├── src/
│   ├── config.py         # Application configuration
│   ├── server.py         # UDP server
│   ├── sender.py         # UDP client
│   ├── database.py       # Database operations
│   └── models.py         # Database initialization
│
├── tests/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Technologies Used

* Python 3.x
* socket (Standard Library)
* sqlite3 (Standard Library)

No external libraries are required for the initial implementation.

---

## Getting Started

### 1. Clone the repository

```bash
git clone <repository-url>
cd udp-server
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

### Start the UDP server

```bash
python src/server.py
```

### Run the sender

Open another terminal and execute:

```bash
python src/sender.py
```

Type any message and press Enter. The server will receive the message and store it in the database.

---

## Example

Sender

```
Hello UDP!
```

Server Output

```
UDP Server started on 0.0.0.0:5005

Received from 127.0.0.1:54321

Message:
Hello UDP!
```


## License

This project is intended for educational and learning purposes.
