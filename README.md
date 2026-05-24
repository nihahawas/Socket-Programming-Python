# 🔌 TCP & UDP Socket Programming using Python

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Socket](https://img.shields.io/badge/Socket-TCP%20%7C%20UDP-green?style=flat)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat)

> A complete implementation of **Client-Server Communication** using Python's built-in `socket` library — covering both TCP and UDP protocols with real-time bidirectional messaging.

---
## TCP Server and Client communication

<img width="1860" height="985" alt="tcp-server-client" src="https://github.com/user-attachments/assets/d052fa5b-5cb3-4414-903a-fb86f771ef71" />

---
## 📌 About This Project

This project demonstrates **real-time Client-Server Communication** using Python sockets.
It implements both **TCP (Transmission Control Protocol)** and **UDP (User Datagram Protocol)** with features like timestamps, uppercase conversion, message counting, and graceful exit handling.

---

## 📁 File Structure

```
Socket-Programming-Python/
│
├── tcp_server.py       # TCP Server Program
├── tcp_client.py       # TCP Client Program
├── udp_server.py       # UDP Server Program
├── udp_client.py       # UDP Client Program
└── README.md           # Project Documentation
```

---

## ✨ Features

- ✅ TCP Client-Server Communication
- ✅ UDP Client-Server Communication
- ✅ Student Name & Registration Number on startup
- ✅ Timestamp on every message `[HH:MM:SS]`
- ✅ Messages automatically converted to **UPPERCASE**
- ✅ Message counter (tracks total messages sent)
- ✅ Type `exit` to gracefully end the session

---

## 🔄 TCP vs UDP

| Feature | TCP | UDP |
|---------|-----|-----|
| Connection | Required | Not Required |
| Reliability | High ✅ | Low ⚠️ |
| Speed | Slower | Faster ⚡ |
| Data Order | Guaranteed | Not Guaranteed |
| Port Used | `12345` | `12346` |
| Real-world Use | HTTP, FTP, Email | Streaming, Gaming, DNS |

---

## 🚀 How to Run

### Prerequisites
```bash
python --version   # Make sure Python 3.x is installed
```

### ▶️ TCP Communication

Open **two terminals** simultaneously:

```bash
# Terminal 1 — Run Server FIRST
python tcp_server.py

# Terminal 2 — Run Client SECOND
python tcp_client.py
```

### ▶️ UDP Communication

```bash
# Terminal 1 — Run Server FIRST
python udp_server.py

# Terminal 2 — Run Client SECOND
python udp_client.py
```

> ⚠️ **Always start the Server before the Client!**

---

## 💬 Sample Output

```
========================================
        UDP SERVER STARTED
  Student : Niha Hawas
========================================
Listening on 127.0.0.1:12346 ...
Waiting for messages...

[20:24:28] Client [1]: HELLO
  └ UPPERCASE: [NIHA HAWAS | 2312274] CLIENT: HELLO
Your Reply: HI

[20:24:46] Client [2]: HAVE YOU DONE YOUR TASK
  └ UPPERCASE: CLIENT: HAVE YOU DONE YOUR TASK
Your Reply: YES IT IS DONE

✅ UDP Server closed. Total messages handled: 7
```

---

## 📋 Tasks Completed

| # | Task | Status |
|---|------|--------|
| 1 | TCP Server and Client communication | ✅ |
| 2 | UDP Server and Client communication | ✅ |
| 3 | Exchange at least 5 messages | ✅ (7 messages) |
| 4 | Send Student Name and Registration Number | ✅ |
| ⭐ | Timestamps on every message | ✅ |
| ⭐ | Convert messages to UPPERCASE | ✅ |
| ⭐ | Terminate session with `exit` command | ✅ |

---

## 🛠️ Technologies Used

| Tool | Purpose |
|------|---------|
| Python 3.x | Core Language |
| `socket` module | Network Communication |
| VS Code | Development Environment |
| GitHub | Version Control |

---

## 📚 Concepts Covered

- Client-Server Architecture
- TCP — Connection-Oriented Communication
- UDP — Connectionless Communication
- Socket Binding, Listening & Accepting
- Real-time Bidirectional Messaging
- Data Encoding & Decoding over Sockets

---


## 👩‍💻 Author

<table>
  <tr>
    <td align="center">
      <b>Niha Hawas</b><br>
      <a href="https://www.linkedin.com/in/nihahawas45">
        <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />
      </a>&nbsp;
      <a href="https://github.com/nihahawas">
        <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />
      </a>
    </td>
  </tr>
</table>

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use and modify.

---

<p align="center">Made with ❤️ by <b>Niha Hawas</b></p>
