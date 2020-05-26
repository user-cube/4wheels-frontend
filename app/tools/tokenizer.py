from datetime import datetime, timedelta, timezone
import jwt
from dotenv import load_dotenv
import os

load_dotenv()

class Tokenizer:
    def __init__(self):
        self.key = os.getenv('KEY')

    def genToken(self, email):
        message = {
            'email': email,
            'iat': datetime.now(timezone.utc),
            'exp': datetime.now(timezone.utc) + timedelta(minutes=1),
        }
        token = jwt.encode(message, self.key, algorithm='HS512')
        return token.decode("utf-8")