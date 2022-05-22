import json
import logging

logger = logging.getLogger("bmi-calculator")


def check_value(value, datatype="int"):
    """
    Method to check if a value matches a datatype

    Parameters
    ----------
    value : int/float
        Value to check
    datatype : str
        Datatype to check

    Returns
    -------
    bool
        True if there is no datatype mismatch

    Raises:
    ----------
    ValueError
        Raises error if there is a datatype mismatch.
    """
    datatype_mapping = {"int": int,
                        "float": float}
    try:
        datatype_mapping[datatype](value)
        return True
    except ValueError:
        logger.error(f"Datatype mismatch for value: {value} - Expecting {datatype}")
        raise


def calculate_bmi(height: int, weight: int):
    """
    Method to calculate the body mass index

    Parameters
    ----------
    height : int
        Height in centimeters
    weight : int
        Weight in kilograms

    Returns
    -------
    float
        Body mas index as a float (rounded to two decimal)
    """
    check_value(weight)
    check_value(height)

    return round(weight / (height / 100) ** 2, 2)


def count_values(bmi_list: list, upper_boundary=29.9, lower_boundary=25):
    """
    Method to count the bmi values that are between two boundaries.

    Parameters
    ----------
    bmi_list : list
        List with bmi values
    upper_boundary : float
        Max value to filter
    lower_boundary : float
        Min value to filter

    Returns
    -------
    int
        Number of bmi values categorized as overweight
    """
    overweight_list = list()
    for value in bmi_list:
        if lower_boundary <= value <= upper_boundary:
            overweight_list.append(value)
    return len(overweight_list)


def get_bmi_count(data_dict_list):
    """
    Method to count the bmi values categorized as overweight from a list of Jsons.

    Parameters
    ----------
    data_dict_list : list[dict] / str
        Initial data as list of dicts or string representation of list of dicts

    Returns
    -------
    int
        Count of data points categorized as overweight
    """
    if type(data_dict_list) == str:
        data_dict_list = json.loads(data_dict_list)
    bmi_values_list = list()
    for data in data_dict_list:
        bmi_values_list.append(calculate_bmi(height=data["HeightCm"],
                                             weight=data["WeightKg"]))
    return count_values(bmi_values_list)


if __name__ == "__main__":
    data_list = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96},
                 {"Gender": "Male", "HeightCm": 161, "WeightKg": 85},
                 {"Gender": "Male", "HeightCm": 180, "WeightKg": 77},
                 {"Gender": "Female", "HeightCm": 166, "WeightKg": 62},
                 {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
                 {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]
    print(get_bmi_count(data_list))
