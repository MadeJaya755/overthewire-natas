import requests
from requests.auth import HTTPBasicAuth

# Kredensial Natas 3
username = 'natas3'
password = '<password_natas3>'
url = 'http://natas3.natas.labs.overthewire.org/'

# Request halaman dengan HTTP Basic Auth
res = requests.get(url, auth=HTTPBasicAuth(username, password))

# Print isi halaman untuk menemukan password level 4
print(res.text)
