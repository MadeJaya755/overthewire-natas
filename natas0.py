import requests
from requests.auth import HTTPBasicAuth

url = "http://natas0.natas.labs.overthewire.org"
res = requests.get(url, auth=HTTPBasicAuth("natas0", "natas0"))
print(res.text)
