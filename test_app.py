from app import calculate_area_of_circle
from app import calculate_circumference_of_circle
import math


def test_calculate_area_of_circle():
    assert calculate_area_of_circle(5) == math.pi * 25


def test_calculate_circumference_of_circle():
    assert calculate_circumference_of_circle(5) == 2 * math.pi * 5
