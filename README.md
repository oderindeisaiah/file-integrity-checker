# File Integrity Checker (Python)

A cybersecurity tool that detects unauthorized file modifications
by comparing cryptographic hash values.

This project demonstrates how integrity monitoring works in real systems.

---

## 🛡️ Features

- SHA-256 file hashing
- Detects file changes or tampering
- Persistent hash storage
- Efficient file reading using chunks

---

## 🧠 What I Learned

- How file integrity monitoring works
- Hashing files using SHA-256
- Reading files in binary mode
- Detecting unauthorized modifications
- Practical cybersecurity logic

---

## 🛠️ Technologies Used

- Python
- hashlib
- os

---

## 🚀 How It Works

1. First run:
   - User selects a file
   - Program calculates and saves its hash

2. Subsequent runs:
   - File is re-hashed
   - Hash values are compared
   - Alerts if the file was modified

---

## ⚠️ Security Note

The stored hash file is excluded from GitHub using `.gitignore`
to prevent manipulation or exposure.

---

## 📌 Purpose

This project was built to understand file integrity,
tamper detection, and core cybersecurity principles.
