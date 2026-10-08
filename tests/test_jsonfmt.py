import pytest
from fixit.jsonfmt import format_json


def test_format_json():
    assert format_json('{"a":1}') == '{\n  "a": 1\n}'


@pytest.mark.xfail(reason="Known bug: invalid JSON raises a raw traceback instead of a friendly error")
def test_invalid_json_friendly_error():
    with pytest.raises(ValueError, match="Invalid JSON"):
        format_json("{not json")
