# 🔐 Task 4 – The Key Under the Mat: Basic Password Cracking

This project demonstrates the weakness of poor passwords by cracking a captured
password hash using dictionary and brute-force techniques.

## 🧠 Concept Overview
Passwords are not stored in plain text. Systems store **hashes** (cryptographic
fingerprints). When users log in, the typed password is hashed and compared.

Attackers attempt to guess passwords by:
| Method | Description |
|--------|-------------|
| Dictionary Attack | Tries items from a list of common passwords |
| Brute-Force Attack | Tries every combination of characters (slow but guaranteed) |
| Hybrid | Combination of both |

---

## 🛠 Tools Used
| Tool | Purpose |
|------|--------|
| `Python (hashlib)` | Custom cracking script |
| `Wordlist` | List of possible passwords (`rockyou.txt` or wordlist.txt) |
| `John the Ripper` (optional) | Professional hash-cracking tool |
| `Hashcat` (optional) | GPU-accelerated password cracking tool |

---

## 📂 Usage — Python Script
### 1️⃣ Place files in directories

### 2️⃣ Run script

### 3️⃣ Output
Result will be stored in:

---

## 🔥 Running with John the Ripper (optional)

## ⚡ Running with Hashcat (optional)

---

## 📌 Educational Note
This project is for **learning cybersecurity and password security awareness only**.  
Do **NOT** use these techniques on systems you do not own.

---

## 👨‍💻 Author
Cyber Security Lab – Task 4 Implementation
