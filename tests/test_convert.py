import pytest
from fixit.convert import (celsius_to_fahrenheit, fahrenheit_to_celsius,
                           km_to_miles, miles_to_km)


def test_c_to_f():
    assert celsius_to_fahrenheit(100) == 212


def test_f_to_c():
    assert fahrenheit_to_celsius(32) == 0


def test_km_to_miles():
    assert km_to_miles(10) == pytest.approx(6.21371, rel=1e-4)


@pytest.mark.xfail(reason="Known bug: miles_to_km divides instead of multiplies")
def test_miles_to_km():
    assert miles_to_km(1) == pytest.approx(1.609344)
