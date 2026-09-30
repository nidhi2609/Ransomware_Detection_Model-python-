# Ransomware Detection & Recovery: Project Notes (Study Guide)

> Ye notes seekhne ke liye hain. Code ke blanks aur final explanation **apne words me khud likho**, tabhi viva me explain kar paogi.

---

## 1. Program kya karta hai (4 parts)

| Part | Kaam | Question ka task |
|---|---|---|
| Score system | Indicators ko points dekar severity batata hai (LOW / HIGH / CRITICAL) | Task 1, 2 |
| Lateral movement | Ek user kitne unique hosts pe login hua ginta hai | Task 3, 4 |
| Backup integrity | File ka SHA-256 hash pehle aur baad me compare karta hai | Task 5 |
| Report | Result ko `report.txt` me likhta hai | Task 8, 9 |

**Soch ka tarika:** jo kaam lab me manually karti ho (logs dekhna, hash compare karna), wahi code me likhna hai.

---

## 2. Tumhare code me kya fix karna hai

### Step 2: `check_score` function

Abhi ye galtiyan hain:

| Galti | Fix |
|---|---|
| `def check_score(...)` ke end me `:` nahi hai | `:` lagao |
| Function ka body indent nahi hai | Body ko 4 spaces aage karo |
| `print("critical")` function ke andar hai, to `print(check_score(...))` me `None` aata hai | `print` ki jagah `return` likho |

Sahi structure:

```python
def check_score(rename, process, copy_delete):
    score = 0
    if rename > 100:
        score = score + 20
    if process == "encryptsvc.exe":
        score = score + 20
    if copy_delete:
        score = score + 20

    if score >= 60:
        return "critical"
    elif score >= 30:
        return "high"
    else:
        return "low"

print(check_score(600, "encryptsvc.exe", True))   # critical
print(check_score(50, "notepad.exe", False))      # low
```

**Yaad rakho:** `return` result wapas deta hai, `print` sirf screen pe dikhata hai.

### Step 4: comment saaf karo

Comment me ek stray `"` aur do sentences mix ho gaye hain. Isse ek sentence banao:
`# hash file ka fingerprint hai, ek character badle to hash poori tarah badal jaata hai, isse tampering pata chalti hai`

---

## 3. Ab kya likhna baaki hai (fill-in skeletons)

### A. `find_lateral(logins)`

Step 3 ka wahi logic function me daalo. `pass` hata ke apna code likho:

```python
def find_lateral(logins):
    hosts = {}
    for user, host in logins:
        pass  # TODO 1: agar user hosts me nahi hai to uska khaali set() banao
        pass  # TODO 2: host ko us user ke set me add karo

    suspects = []
    for user in hosts:
        pass  # TODO 3: agar unique hosts >= 3 hain to suspects.append(user)
    return suspects
```

Test: `print(find_lateral(logins))` → `['svc-backup-admin']`

### B. `check_backup(filename, old_hash)`

```python
def check_backup(filename, old_hash):
    new_hash = ____            # TODO: get_hash(...) use karo
    if ____:                   # TODO: dono hash same hain?
        return "clean"
    else:
        return "tampered"
```

Test: `old_hash` lo, file badlo, phir `print(check_backup("backup.txt", old_hash))` → `tampered`

### C. Report file likhna (`report.txt`)

```python
def write_report(severity, suspects, backup_status):
    with open("report.txt", "w") as f:
        f.write("Severity: " + severity + "\n")
        # TODO: suspects aur backup_status bhi isi tarah likho
```

### D. Sabse neeche sab ko jodo

```python
severity = check_score(600, "encryptsvc.exe", True)
suspects = find_lateral(logins)
status = check_backup("backup.txt", old_hash)
write_report(severity, suspects, str(status))
print("Done, report.txt bana")
```

### E. Extra (viva me impress karne ke liye)
- `check_score` me ek naya indicator jodo: `powershell` (True/False) → +10 points.
- `RENAME_LIMIT = 100` jaisa variable upar rakho, taaki limit ek jagah se badle.

---

## 4. Run kaise karein

1. Code ko `detect.py` naam se save karo.
2. Terminal usi folder me kholo.
3. `python detect.py` (ya `py detect.py`)
4. `FileNotFoundError` aaye to check karo ki `backup.txt` usi folder me ban rahi hai (code se `open("backup.txt","w")` se banti hai).

---

## 5. Viva ke sawal (khud jawab likh ke practice karo)

1. `if` aur `elif` me kya fark hai?
2. Dictionary me `set()` kyun use kiya?
3. `print` aur `return` me kya fark hai?
4. Hash kya hota hai, aur ek character badalne pe kya hota hai?
5. Function kyun banate hain?
6. Agar attacker backup ke saath manifest/hash bhi badal de to kya hoga? (Hint: hash ko alag, offline jagah rakho.)

---

## 6. Question ke 10 tasks: kya points likhne hain (apne words me likhna)

| Task | Key points |
|---|---|
| 1. Containment | Poora shutdown nahi, segment/VLAN se isolate; malicious process kill; `svc-backup-admin` disable |
| 2. Encryption rokna (business chalte hue) | Shares read-only; sirf malicious process/hash block; IAM online rakhna |
| 3. Credential abuse | Login logs (kab, kahan se); insider vs stolen credential; password reset, sessions revoke |
| 4. Lateral movement | Ek user ka bahut hosts pe login; SMB surge; PowerShell logs |
| 5. Backup integrity | Hash compare; offline/immutable backup; sandbox me test restore |
| 6. Clean recovery | Attack start time dhundo; usse pehle ka backup; clean network me restore |
| 7. Safe restoration | Critical systems pehle; phased restore; monitoring |
| 8. Evidence preservation | Memory dump, disk image, logs; hash aur chain-of-custody |
| 9. Communication + escalation | Incident commander; SOC → CISO → Legal; regulatory reporting window (India me CERT-In 6 ghante) |
| 10. Hardening | MFA, least privilege, segmentation, immutable backups, EDR, restore drills |

**Last part (tradeoffs):** containment vs availability, speed vs evidence, live recovery vs rebuild, IAM online rakhna vs security.