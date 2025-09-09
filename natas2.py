import requests
from requests.auth import HTTPBasicAuth

# Kredensial Natas 2
username = 'natas2'
password = '3gqisGdR0pjm6tpkDKdIWO2hSvchLeYH'
url = 'http://natas2.natas.labs.overthewire.org/'

# Request halaman dengan HTTP Basic Auth
res = requests.get(url, auth=HTTPBasicAuth(username, password))

# Print isi halaman (untuk menemukan password level 3)
print(res.text)
