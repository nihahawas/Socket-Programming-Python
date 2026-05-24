"""
Lab 06 — UDP Server Program
Tasks Covered:
  - Task 2: UDP Server and Client communication
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

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = "127.0.0.1"
port = 12346

server_socket.bind((host, port))

print("=" * 50)
print("       UDP SERVER STARTED")
print(f"  Student : {STUDENT_NAME}")
print(f"  Reg No  : {REG_NUMBER}")
print("=" * 50)
print(f"Listening on {host}:{port} ...")
print("Waiting for messages...\n")

msg_count = 0

while True:
    try:
        data, addr = server_socket.recvfrom(1024)
        message = data.decode()
        msg_count += 1
        ts = get_timestamp()

        # Bonus: Convert to UPPERCASE
        upper_msg = message.upper()
        print(f"{ts} Client [{msg_count}] from {addr}: {message}")
        print(f"  ↳ UPPERCASE: {upper_msg}")

        # Bonus: Terminate if client sends 'exit'
        if message.strip().lower() == "exit":
            goodbye = f"{ts} [{STUDENT_NAME} | {REG_NUMBER}] Server: Goodbye!"
            server_socket.sendto(goodbye.encode(), addr)
            print("Client sent 'exit'. Shutting down server.")
            break

        reply = input("Your Reply (type 'exit' to quit): ").strip()

        # Bonus: Add timestamp + student info to reply
        full_reply = f"{ts} [{STUDENT_NAME} | {REG_NUMBER}] Server: {reply}"
        server_socket.sendto(full_reply.encode(), addr)

        # Bonus: Terminate if server types 'exit'
        if reply.lower() == "exit":
            print("You ended the session.")
            break

    except KeyboardInterrupt:
        print("\nServer stopped by user.")
        break

server_socket.close()
print(f"\n✅ UDP Server closed. Total messages handled: {msg_count}")
