import pytest
from fixit.wordcount import count_chars, count_lines, count_words


def test_count_words_simple():
    assert count_words("hello world") == 2


@pytest.mark.xfail(reason="Known bug: multiple spaces are counted as words")
def test_count_words_extra_spaces():
    assert count_words("hello    world") == 2


@pytest.mark.xfail(reason="Known bug: empty string returns 1")
def test_count_words_empty():
    assert count_words("") == 0


@pytest.mark.xfail(reason="Known bug: trailing newline adds a phantom line")
def test_count_lines_trailing_newline():
    assert count_lines("a\nb\n") == 2


def test_count_chars():
    assert count_chars("abc") == 3
