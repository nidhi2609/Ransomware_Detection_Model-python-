# Ransomware Detection & Recovery in Hybrid Infrastructure

---

## 📌 Project Overview

This project demonstrates a simple cybersecurity approach for detecting and analyzing
possible ransomware activity in a hybrid infrastructure environment.

The system uses security indicators such as:

- Sudden file rename activity
- Suspicious encryption process
- File copy/delete behavior
- Suspicious service account logins
- Lateral movement across multiple machines
- Backup file integrity verification using SHA-256 hashing

The project is designed as a simple educational prototype to understand how
ransomware-related indicators can be detected using Python.

---

## 🎯 Problem Statement

A file server used by multiple business services is showing rapid file encryption
behavior.

The following suspicious activities have been observed:

- Sudden spike in file rename operations
- High disk write rate
- Suspicious encryption process
- Suspicious service account activity
- Shadow copies deleted
- SMB traffic surge
- Lateral authentication attempts
- Suspicious PowerShell execution
- Backups are available but their integrity is unknown

The objective is to detect suspicious behavior, identify possible ransomware activity,
verify backup integrity and support recovery planning.

---

## Features
- Score-based ransomware indicator detection
- Lateral movement detection
- Backup integrity check using SHA-256

---

## 🛠️ Technologies Used

- Python 3
- hashlib
- Python Lists
- Python Dictionaries
- Python Sets
- Conditional Statements
- Functions
- SHA-256 Hashing

---

## 📂 Project Structure

```text
ransomware-detection/
│
├── ransomware_detection.py
├── backup.txt
└── README.md
