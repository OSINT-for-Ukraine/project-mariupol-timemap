import json
import re
import csv

def extract_military_units(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    units = []

    pattern = re.compile(r'\d+(?:st|nd|rd|th)?\s+([A-Za-z\s]+)')

    for entry in data:
        description = entry.get('description', '')
        match = pattern.search(description)
        if match:
            unit_type = match.group(1).strip()
            units.append({"unit_type": unit_type, "unit_name": description})
    unique_dicts = {tuple(d.items()) for d in units}
    list_of_unique_dicts = [dict(t) for t in unique_dicts]
    return list_of_unique_dicts

if __name__ == '__main__':
    filename = '01-01-2023.json'
    military_units = extract_military_units(filename)
    with open('military_units.csv', 'w') as f:
        fields = ['unit_type', 'unit_name']
        # using csv.writer method from CSV package
        dict_writer = csv.DictWriter(f, fields)
        dict_writer.writeheader()
        dict_writer.writerows(military_units)
    print(military_units)

