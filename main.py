# 1.sbse pehle indicators dekhna h 
rename = 600 
if rename > 100:
    print("alert: file rename spike")

# rename ek variable h jo data store kr rha h 
# or if condition check kar rahi hai ki rename count limit (100) se zyada hai ya nahi

# fhr hamne fhrse checkkrna h ki indicate hoga y nhi 
# 2. score system banaya h jo check krega suspiciouc h y nhi 
rename = 600 
process = "encryptsvc.exe"
copy_delete = True 

def check_score(rename, process, copy_delete):
    score = 0  # ye isliye liya h ki suspicious chiz pr point bade or pta chle vo h y nhi 

    if rename > 100 :
        score = score + 20 
    if process == "encryptsvc.exe" :
        score = score + 20 
    if copy_delete : 
        score = score + 20 

    if score >= 60 :
        return "critical"
    elif score >= 30 : 
        return "high"
    else :
        return "low"

print(check_score(600, "encryptsvc.exe", True))    # critical
print(check_score(50, "notepad.exe", False))       # low

# 3. ab mai ye check krugi ki svc-backup-admin kitne alg machines pr login huya h 
logins = [              # is list ke andr user or host dono h 
    ("nidhi" , "hp-pc") ,
    ("raghav" , "filesrv") ,
    ("svc-backup-admin" , "dc01") ,
    ("svc-backup-admin" , "hr-pc") ,
    ("svc-backup-admin" , "filesrv") ,
]
hosts = {}         # ye ek dictionary h isme key = user h , or value = us user ke host h 
for user , host in logins: 
    if user not in hosts : 
        hosts[user] = set()  # ye isliye lgya h jisse dupilcate hat jayega or ek host pe 10 bar login kro toh vo 1 hi count krega 
    hosts[user].add(host)

for user in hosts : 
    if len(hosts[user]) >= 3:            # ye len fun batayega ki kitne unique hosts h 
        print(user, "-> lateral movement suspect")

# 4. backup integrity h isme file check krne keliye hash use krugi
# hash file ka fingerprint hai, ek character badle to hash poori tarah badal jaata hai, isse tampering pata chalti hai
import hashlib 
def get_hash(filename):        # ye ek function h isse ek kaam kro name dediya h taki bar bar likhna na pde bss function chl jaye 
    with open(filename,"rb") as f:   # rb ka mtlb h file ko binary mai pado 
        return hashlib.sha256(f.read()).hexdigest()

with open("backup.txt", "w") as f:  # pehle file banao fhr dekho 
    f.write("payroll data")

old_hash = get_hash("backup.txt")
# iss line ko process krne mai time lgega 
with open("backup.txt", "a") as f:   # file me change kro like attack simulate
    f.write(" tampered")
new_hash = get_hash("backup.txt")

# ab ham check krege ki vo dono hash same h y nhi 
if old_hash == new_hash: 
    print ("backup clean")
else : 
    print("backup tampered ! ")