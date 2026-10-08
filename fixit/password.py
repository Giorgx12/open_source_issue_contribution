"""Random password generator."""
import random
import string


def generate(length: int = 12, use_digits: bool = True, use_symbols: bool = False) -> str:
    """Return a random password of the given length."""
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation
    return "".join(random.choice(chars) for _ in range(length - 1))
