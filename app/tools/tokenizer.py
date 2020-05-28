from datetime import datetime, timedelta, timezone
import jwt
from dotenv import load_dotenv
import os
import requests

load_dotenv()


class Tokenizer:
    def __init__(self):
        """
        Initializer of our class,
        here we define our key to sign the tokens.
        """
        self.key = os.getenv('KEY')

    def genToken(self, email):
        """
        Generate a token with a given
        email.
        Args:
            email: request user email.

        Returns:
            a jwt with user email.

        """
        message = {
            'email': email,
            'iat': datetime.now(timezone.utc),
            'exp': datetime.now(timezone.utc) + timedelta(minutes=1),
        }
        token = jwt.encode(message, self.key, algorithm='HS512')
        return token.decode("utf-8")

    def checkUserType(self, request):
        if 'user_type' not in request.session.keys():
            return False
        else:
            return True

    def getType(self, request):
        r = requests.get("https://tqsapitests.herokuapp.com/profile/",
                         headers={'Authorization': 'Bearer ' + self.genToken(request.user.email)})
        if r.status_code != 200:
            return False
        json = r.json()
        request.session.__setitem__('user_type', json['type'])
        return True