"""Small text helpers."""


def is_palindrome(text: str) -> bool:
    """Return True if text reads the same forwards and backwards."""
    return text == text[::-1]


def reverse_words(text: str) -> str:
    """Reverse the order of words in text."""
    return " ".join(reversed(text.split(" ")))
