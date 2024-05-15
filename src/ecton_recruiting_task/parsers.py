from xml.dom.minidom import parse

from yaml import load

try:
    from yaml import CSafeLoader as SafeLoader
except ImportError:
    from yaml import SafeLoader

from ecton_recruiting_task.utils import convert_units, format_quantity


class FileParser:
    def __init__(self, file_path):
        self.file_path = file_path

    def _parse_recipe_data(self, recipe_file):
        raise NotImplementedError(f"Recipe parser not implemented for file: {self.file_path}")

    def _prepare_ingredients(self, recipe_data):
        for ingredient in recipe_data["ingredients"]:
            # Change quantities to float
            ingredient["quantity"] = float(ingredient["quantity"])
            # Convert to metric if needed
            if "unit" in ingredient:
                metric_unit, metric_quantity = convert_units(ingredient["unit"], float(ingredient["quantity"]))
                ingredient["unit"] = metric_unit
                ingredient["quantity"] = metric_quantity
            # Format the value
            ingredient["quantity"] = format_quantity(ingredient["quantity"], unit=ingredient.get("unit"))
        return recipe_data

    def get_recipe(self):
        with open(self.file_path) as recipe_file:
            recipe_data = self._prepare_ingredients(self._parse_recipe_data(recipe_file))
            return recipe_data


class XmlParser(FileParser):

    def _get_node_text(self, xml_node):
        elements = []
        for node in xml_node.childNodes:
            if node.nodeType == node.TEXT_NODE:
                elements.append(node.data)
        return "".join(elements)

    def _get_node_text_by_name(self, parent_node, element_name):
        nodes = parent_node.getElementsByTagName(element_name)
        if not nodes:
            return None
        child_node = nodes[0]

        text_nodes = []
        for node in child_node.childNodes:
            if node.nodeType == node.TEXT_NODE:
                text_nodes.append(node.data)
        return "".join(text_nodes)

    def _parse_recipe_data(self, recipe_file):
        result = {}
        document = parse(recipe_file)
        root = document.firstChild

        # Name
        node_text = self._get_node_text_by_name(root, "name")
        if node_text:
            result["name"] = node_text

        # Ingredeints
        ingredients = []
        for ingredient_node in root.getElementsByTagName("ingredients"):
            ingredient = {}
            for node_name in ("item", "quantity", "comment", "unit"):
                node_text = self._get_node_text_by_name(ingredient_node, node_name)
                if node_text:
                    ingredient[node_name] = node_text
            if ingredient:
                ingredients.append(ingredient)
        result["ingredients"] = ingredients

        # Preparations
        preperations = []
        for preparations_node in root.getElementsByTagName("preperations"):
            node_text = self._get_node_text(preparations_node)
            if node_text:
                preperations.append(node_text)
        result["preperations"] = preperations

        return result


class YamlParser(FileParser):

    def _parse_recipe_data(self, recipe_file):
        return load(recipe_file, SafeLoader)
