import pytest
from python.main import check_value, calculate_bmi, count_values, get_bmi_count


def test_check_value_positive():
    assert check_value(3)
    assert check_value(1.5, "float")


def test_check_value_negative_int():
    with pytest.raises(Exception):
        check_value("foo")


def test_check_value_negative_float():
    with pytest.raises(Exception):
        check_value("foo", "float")


def test_calculate_bmi():
    assert calculate_bmi(175, 75) == 24.49


def test_count_values():
    assert count_values([32.83, 32.79, 23.77, 22.5, 31.11, 29.4]) == 1


def test_get_bmi_count():
    data_list = """[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96},
                    {"Gender": "Male", "HeightCm": 161, "WeightKg": 85},
                    {"Gender": "Male", "HeightCm": 180, "WeightKg": 77},
                    {"Gender": "Female", "HeightCm": 166, "WeightKg": 62},
                    {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
                    {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]"""
    assert get_bmi_count(data_list) == 1 
    assert get_bmi_count(eval(data_list)) == 1
