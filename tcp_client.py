"""
Lab 06 — TCP Client Program
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

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 12345

print("=" * 50)
print("       TCP CLIENT STARTED")
print(f"  Student : {STUDENT_NAME}")
print(f"  Reg No  : {REG_NUMBER}")
print("=" * 50)

try:
    client_socket.connect((host, port))
    print(f"✅ Connected to server at {host}:{port}\n")

    # Receive server's intro message
    intro = client_socket.recv(1024).decode()
    print(f"Server Info: {intro}\n")

    msg_count = 0

    while True:
        message = input("Your Message (type 'exit' to quit): ").strip()

        if not message:
            continue

        # Bonus: Add timestamp + student info to message
        ts = get_timestamp()
        full_message = f"{ts} [{STUDENT_NAME} | {REG_NUMBER}] Client: {message}"
        client_socket.send(full_message.encode())

        msg_count += 1

        # Bonus: Terminate if client types 'exit'
        if message.lower() == "exit":
            print("You ended the session.")
            break

        data = client_socket.recv(1024).decode()

        # Bonus: Convert server reply to UPPERCASE for display
        print(f"Server Reply [{msg_count}]: {data}")
        print(f"  ↳ UPPERCASE: {data.upper()}\n")

        if "Goodbye" in data:
            break

except ConnectionRefusedError:
    print("❌ ERROR: Could not connect to server.")
    print("   → Make sure tcp_server.py is running FIRST.")

finally:
    client_socket.close()
    print("\n✅ Client closed. Messages sent: {msg_count}")
