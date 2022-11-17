from passlib.hash import bcrypt


class SecurityService:
    def __init__(self, salt: str):
        self.salt = salt

    def verify_secret_key(self, plain_secret_key: str, hashed_secret_key: str) -> bool:
        return bcrypt.using(salt=self.salt).verify(plain_secret_key, hashed_secret_key)

    def get_secret_key_hash(self, secret_key: str) -> str:
        return bcrypt.using(salt=self.salt).hash(secret_key)
