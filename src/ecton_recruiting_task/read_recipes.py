import argparse
import json
import os

from ecton_recruiting_task import parsers

if __name__ == "__main__":
    PARSERS = {
        "xml": parsers.XmlParser,
        "yaml": parsers.YamlParser,
    }

    parser = argparse.ArgumentParser(description="Read XML and YAML recipes and export them to a JSON file.")
    parser.add_argument("-i", "--input_directory", required=True, help="Path to directory with input files")
    parser.add_argument("-o", "--output_file", help="Path to output JSON file", default="expected_output.json")
    args = parser.parse_args()

    recipes = []
    for item in os.scandir(path=args.input_directory):
        if not item.is_file():
            # Not a file
            continue
        ext = os.path.splitext(item.name)[1][1:]
        if not ext or ext not in PARSERS:
            continue
        parser = PARSERS[ext](item.path)
        recipe = parser.get_recipe()
        if recipe:
            recipes.append(recipe)

    with open(args.output_file, "w") as output_file:
        json.dump(recipes, output_file, indent=4)
