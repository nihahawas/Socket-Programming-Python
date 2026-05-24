"""
Lab 06 — UDP Client Program
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

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = "127.0.0.1"
port = 12346

print("=" * 50)
print("       UDP CLIENT STARTED")
print(f"  Student : {STUDENT_NAME}")
print(f"  Reg No  : {REG_NUMBER}")
print("=" * 50)
print(f"Sending to UDP Server at {host}:{port}\n")
print("Type your messages below. Type 'exit' to quit.\n")

msg_count = 0

while True:
    message = input("Your Message (type 'exit' to quit): ").strip()

    if not message:
        continue

    ts = get_timestamp()
    # Bonus: Add timestamp + student info to message
    full_message = f"{ts} [{STUDENT_NAME} | {REG_NUMBER}] Client: {message}"
    client_socket.sendto(full_message.encode(), (host, port))
    msg_count += 1

    # Bonus: Terminate if user types 'exit'
    if message.lower() == "exit":
        print("You ended the session.")
        # Still receive the goodbye from server
        try:
            client_socket.settimeout(2)
            data, addr = client_socket.recvfrom(1024)
            print(f"Server: {data.decode()}")
        except:
            pass
        break

    data, addr = client_socket.recvfrom(1024)
    reply = data.decode()

    # Bonus: Show reply and UPPERCASE version
    print(f"Server Reply [{msg_count}]: {reply}")
    print(f"  ↳ UPPERCASE: {reply.upper()}\n")

    if "Goodbye" in reply:
        break

client_socket.close()
print(f"\n✅ UDP Client closed. Messages sent: {msg_count}")
