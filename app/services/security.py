from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_secret_phrase(plain_phrase: str, hashed_phrase: str) -> bool:
    return pwd_context.verify(plain_phrase, hashed_phrase)


def get_secret_phrase_hash(secret_phrase: str) -> str:
    return pwd_context.hash(secret_phrase)