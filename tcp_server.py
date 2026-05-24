"""
Lab 06 — TCP Server Program
Tasks Covered:
  - Task 1: TCP Server and Client communication
  - Task 3: Exchange at least five messages
  - Task 4: Send Student Name and Registration Number
  Bonus:
  - Timestamp in messages
  - Convert received message to UPPERCASE
  - Terminate when user types 'exit'
"""

import socket
import datetime

# ─────────────────────────────────────────
#  STUDENT INFO — EDIT THESE
# ─────────────────────────────────────────
STUDENT_NAME = "Niha Hawas"
REG_NUMBER   = "2312274"
# ─────────────────────────────────────────

def get_timestamp():
    return datetime.datetime.now().strftime("[%H:%M:%S]")

# Create TCP Socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Allow reuse of port immediately after restart
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host = "127.0.0.1"
port = 12345

# Bind IP and Port
server_socket.bind((host, port))

# Listen for one incoming connection
server_socket.listen(1)
print("=" * 50)
print("       TCP SERVER STARTED")
print(f"  Student : {STUDENT_NAME}")
print(f"  Reg No  : {REG_NUMBER}")
print("=" * 50)
print(f"Listening on {host}:{port} ...")
print("Waiting for client to connect...\n")

conn, addr = server_socket.accept()
print(f"✅ Connected with: {addr}\n")

# Send student info to client on connect
intro = f"SERVER CONNECTED | Student: {STUDENT_NAME} | Reg: {REG_NUMBER}"
conn.send(intro.encode())

msg_count = 0

while True:
    try:
        data = conn.recv(1024).decode()

        if not data:
            print("Client disconnected.")
            break

        msg_count += 1
        ts = get_timestamp()

        # Bonus: Convert to UPPERCASE before displaying
        upper_data = data.upper()
        print(f"{ts} Client [{msg_count}]: {data}  →  UPPERCASE: {upper_data}")

        # Bonus: Terminate if client sent 'exit'
        if data.strip().lower() == "exit":
            print("Client sent 'exit'. Closing connection.")
            conn.send("Server: Goodbye!".encode())
            break

        reply = input("Your Reply (type 'exit' to quit): ").strip()

        # Bonus: Add timestamp to reply
        full_reply = f"{ts} [{STUDENT_NAME} | {REG_NUMBER}] Server: {reply}"
        conn.send(full_reply.encode())

        # Bonus: Terminate server if server types 'exit'
        if reply.lower() == "exit":
            print("You ended the session.")
            break

    except ConnectionResetError:
        print("Connection was reset by client.")
        break

conn.close()
server_socket.close()
print(f"\n✅ Session ended. Total messages exchanged: {msg_count}")
