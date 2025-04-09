import jwt
from datetime import datetime, timedelta

def generate_jwt():
    now = datetime.utcnow()
    payload = {
        'iss': 'https://auth.cofeemesh.io',  # Issuer of the token
        'aud': 
        'iat': now,
        'exp': now + timedelta(seconds=60),  # Token valid for 60 seconds
        'sub': 'user_id_123'  # Subject (user ID)
    }