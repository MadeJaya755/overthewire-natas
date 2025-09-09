import requests
from requests.auth import HTTPBasicAuth
import re

# Kredensial Natas 1
username = 'natas1'
password = 'gtVrDuiDfck831PqWsLEZy5gyDz1clto'
url = 'http://natas1.natas.labs.overthewire.org/'

# Ambil halaman
res = requests.get(url, auth=HTTPBasicAuth(username, password))

# Cari password dari komentar HTML
match = re.search(r"The password for natas2 is (\w+)", res.text)
if match:
    print("Password untuk Natas 2:", match.group(1))
else:
    print("Password tidak ditemukan di source HTML")
