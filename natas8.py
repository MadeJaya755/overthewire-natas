import base64

encoded_secret = "3d3d516343746d4d6d6c315669563362"

def encode_secret(secret):
    return base64.b64encode(secret.encode())[::-1].hex()

def decode_secret(encoded):
    return base64.b64decode(bytes.fromhex(encoded)[::-1]).decode()

test_secret = "secret_here"
if encode_secret(test_secret) == encoded_secret:
    print("Access granted. Password for natas9 is <censored>")
else:
    print("Wrong secret")

print("Decoded secret:", decode_secret(encoded_secret))
