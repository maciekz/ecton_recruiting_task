import pytest

from ecton_recruiting_task import utils


@pytest.mark.parametrize(
    "input_quantity, input_unit, expected_output", 
    [
        (3.78, "liter", 3.78),
        (20.222, "liter", 20.22),
        (30.335, "liter", 30.34),
        (199.999, "gr", 200),
        (40, "ml", 40),
        (60, None, 60),
        (100.0, None, 100)
    ]
)
def test_format_quantity(input_quantity, input_unit, expected_output):
    output = utils.format_quantity(input_quantity, unit=input_unit)
    assert output == expected_output

 
@pytest.mark.parametrize(
    "source_unit, source_quantity, expected_unit, expected_quantity", 
    [
        ("ml", 10, "ml" , 10),
        ("gallon", 1, "liter", 3.78),
        ("cups", 2, "ml", 480),
        ("pound", 0.44, "gr", 199.5796),
        ("fl. oz.", 2.02, "ml", 59.7314),
    ]
)
def test_convert_units(source_unit, source_quantity, expected_unit, expected_quantity):
    unit, quantity = utils.convert_units(source_unit, source_quantity)
    assert unit == expected_unit
    assert quantity == expected_quantity
