import hashlib
import os
import getpass
import re

# Step 1: Function to validate password strength
def is_strong(password):
    if (len(password) >= 8 and
        re.search(r'[A-Z]', password) and
        re.search(r'[a-z]', password) and
        re.search(r'\d', password) and
        re.search(r'[!@#$%^&*(),.?":{}|<>]', password)):
        return True
    return False

# Step 2: Function to hash + salt the password
def hash_password(password):
    salt = os.urandom(16)  # Random 16 bytes
    salted_password = salt + password.encode()
    hashed = hashlib.sha256(salted_password).hexdigest()
    return salt.hex(), hashed

# Step 3: Main CLI interaction
print("🔐 Password Encryption Tool")
password = getpass.getpass("Enter your password: ")

if is_strong(password):
    salt, hashed = hash_password(password)
    print("\n✅ Password encrypted successfully!")
    print(f"Salt: {salt}")
    print(f"Hashed Password: {hashed}")
else:
    print("\n❌ Weak password. Use at least 8 characters with uppercase, lowercase, number, and special character.")
