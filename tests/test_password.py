import pytest
from fixit.password import generate


@pytest.mark.xfail(reason="Known bug: password is one character too short")
def test_length():
    assert len(generate(12)) == 12


def test_no_digits():
    assert not any(c.isdigit() for c in generate(50, use_digits=False))


@pytest.mark.xfail(reason="Known bug: length < 1 is not validated")
def test_invalid_length():
    with pytest.raises(ValueError):
        generate(0)

def test_symbols_gen():
    assert any(c in string.punctuation for c in generate(200, use_symbols=True))

def test_no_symbols_gen():
    assert not any(c in string.punctuation for c in generate(200))
