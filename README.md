# 🔐 ZIP Password Cracking with John the Ripper  
A **password-cracking demo** using **John the Ripper (Jumbo Edition)** to start brute-force attacks on **ZIP files**.

This script **extracts password hashes from a protected ZIP file** and **cracks the password** using a **brute force approach**

---

## 🚀 **Setup Instructions**
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/mihir-prakash/john-password-crack.git
cd john-password-crack
```

### **2️⃣ Install Dependencies**
#### **For Mac (Homebrew)**
```sh
brew install john-jumbo python
```
#### **For Linux (Ubuntu/Debian)**
```sh
sudo apt update && sudo apt install -y john python3
```
✅ **Verify Installation**:  
```sh
john --version
```

---

## 📌 **Run the Password Cracking Simulation**
```sh
python3 crack_password.py
```
---

## 📜 **How It Works**
- `zip2john` extracts hashes from a password-protected ZIP file.
- `john` uses a **wordlist attack** to crack the password.


---

## 👨‍💻 **Author**
🔗 **[Mihir Prakash](https://github.com/mihir-prakash/)**  

---

## 📜 **License**
This project is open-source under the **MIT License**. Feel free to modify and use it!

