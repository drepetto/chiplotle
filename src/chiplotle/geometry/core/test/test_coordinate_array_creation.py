import pytest

from chiplotle import CoordinateArray


def test_coordinate_array_raises_value_error_on_non_coordinate_parameters():
    with pytest.raises(ValueError):
        CoordinateArray([0, 1])
