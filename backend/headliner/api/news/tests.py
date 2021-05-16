import pytest


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        x = 7 / 0  # pylint: disable=unused-variable
