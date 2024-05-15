# Mapping from imperial to metric units.
# Metric quantities are based on official conversion numbers so they might not match the examples exactly.
# Each entry has the format:
# 'imperial_unit': ('metric_unit', metric_quantity)
IMPERIAL_TO_METRIC_MAPPING = {
    "gallon": ("liter", 3.78),
    "cups": ("ml", 240),
    "pound": ("gr", 453.59),
    "fl. oz.": ("ml", 29.57),
}
# The units that should be rounded to integers
INTEGER_UNITS = ("gr", "ml")


def format_quantity(quantity, unit=None):
    # Round the values and use integer if there's no decimal part
    if unit is not None and unit in INTEGER_UNITS:
        quantity = round(quantity, 0)
    else:
        quantity = round(quantity, 2)
    
    if quantity.is_integer():
        # Return an integer
        return int(quantity)
    return quantity


def convert_units(source_unit, source_quantity):
    if source_unit not in IMPERIAL_TO_METRIC_MAPPING:
        # No conversion needed
        return source_unit, source_quantity
    metric_unit, metric_quantity = IMPERIAL_TO_METRIC_MAPPING.get(source_unit)
    return metric_unit, source_quantity * metric_quantity
