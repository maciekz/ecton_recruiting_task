import pytest

from ecton_recruiting_task import parsers


def test_file_parser_raises_exception():
    # FileParser should not be used directly
    parser = parsers.FileParser("src/ecton_recruiting_task/tests/test_data/example_input_1.xml")
    with pytest.raises(NotImplementedError):
        parser.get_recipe()

 
def test_xml_parser():
    parser = parsers.XmlParser("src/ecton_recruiting_task/tests/test_data/example_input_1.xml")
    recipe = parser.get_recipe()
    expected_recipe = {
		"name": "pudding",
		"ingredients": [
			{"item": "milk", "quantity": 3.78, "unit": "liter"},
			{"item": "sugar", "quantity": 480, "unit": "ml"},
			{"item": "vanilla", "quantity": 10, "unit": "ml"},
			{"item": "egg yolks", "quantity": 12, "comment": "room temperature"}
		],
		"preperations": [
			"omitted for brevity"
		]
	}
    assert recipe == expected_recipe


def test_yaml_parser():
    parser = parsers.YamlParser("src/ecton_recruiting_task/tests/test_data/example_input_2.yaml")
    recipe = parser.get_recipe()
    expected_recipe = {
		"name": "rice",
		"ingredients": [
			{"item": "rice", "quantity": 200, "unit": "gr"},
			{"item": "oil", "quantity": 60, "unit": "ml"},
			{"item": "onion", "quantity": 1, "comment": "white or red"}
		],
		"preperations": [
			"omitted for brevity"
		]
	}
    assert recipe == expected_recipe