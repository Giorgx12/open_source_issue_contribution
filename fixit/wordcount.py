"""Word, line and character counting."""


def count_words(text: str) -> int:
    """Return the number of words in text."""
    return len(text.split(" "))


def count_lines(text: str) -> int:
    """Return the number of lines in text."""
    return len(text.split("\n"))


def count_chars(text: str) -> int:
    """Return the number of characters in text."""
    return len(text)
