'''happy path test'''
import sys
import circle  # pylint: disable=import-error,wrong-import-position
import pytest

sys.path.insert(0, "..")


def test_circle_with_radius_1_2dp():  # pylint: disable=C0116
    my_circle = circle.Circle(float(1.0))
    assert isinstance(my_circle.radius, float)


def test_circle_with_radius_2_2dp():  # pylint: disable=C0116
    with pytest.raises(ValueError):
        my_circle = circle.Circle("-10")  # pylint: disable=W0612 # noqa: F841


def test_circle_with_radius_3_2dp():  # pylint: disable=C0116
    with pytest.raises(TypeError):
        my_circle = circle.Circle("s")  # pylint: disable=W0612 # noqa: F841
