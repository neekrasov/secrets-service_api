from passlib.hash import bcrypt

def verify_secret_key(plain_secret_key: str, hashed_secret_key: str, salt: str) -> bool:
    return bcrypt.using(salt=salt).verify(plain_secret_key, hashed_secret_key)


def get_secret_key_hash(secret_key: str, salt: str) -> str:
    return bcrypt.using(salt=salt).hash(secret_key)