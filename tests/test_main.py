import pytest
import math

def calculate_area(sides, angles):
    areas = []
    for i in range(len(sides)):
        a, b, c = sides[i]
        A, B, C = math.radians(angles[i][0]), math.radians(angles[i][1]), math.radians(angles[i][2])
        area = 0.5 * a * b * math.sin(C)
        areas.append(area)
    return areas

def test_calculate_area():
    sides = [[3, 4, 5], [5, 12, 13]]
    angles = [[60, 60, 60], [30, 60, 90]]
    expected_areas = [6.0, 30.0]
    assert calculate_area(sides, angles) == pytest.approx(expected_areas)

def test_calculate_area_invalid_input():
    sides = [[3, 4, 5], [5, 12, 13]]
    angles = [[60, 60], [30, 60, 90]]
    with pytest.raises(IndexError):
        calculate_area(sides, angles)

def test_calculate_area_empty_input():
    sides = []
    angles = []
    assert calculate_area(sides, angles) == []
