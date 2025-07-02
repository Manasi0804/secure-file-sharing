from cryptography.fernet import Fernet
import os

ENCRYPTION_KEY = os.getenv("SECRET_KEY")[:32].ljust(32, "0").encode()
fernet = Fernet(Fernet.generate_key())

def encrypt_id(data: str):
    return fernet.encrypt(data.encode()).decode()

def decrypt_id(token: str):
    return fernet.decrypt(token.encode()).decode()
