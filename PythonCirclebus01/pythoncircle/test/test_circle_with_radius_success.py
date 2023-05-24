'''happy path test'''

import sys
import circle  # pylint: disable=import-error,wrong-import-position
sys.path.insert(0, "..")


def test_circle_with_radius_1_2dp():  # pylint: disable=C0116
    my_circle = circle.Circle(float(1.0))
    assert round(my_circle.area(), 2) == 3.14
    assert round(my_circle.perimeter(), 2) == 6.28
    assert my_circle.summary() == "The area is 3.14 and the perimeter is 6.28"


def test_circle_with_radius_2_2dp():  # pylint: disable=C0116
    my_circle = circle.Circle(float(2.0))
    assert round(my_circle.area(), 2) == 12.57
    assert round(my_circle.perimeter(), 2) == 12.57
    assert my_circle.summary() == "The area is 12.57 and the perimeter is 12.57"  # noqa: E501
