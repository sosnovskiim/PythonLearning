import csv
import json

with open('constellations.json', encoding='utf-8') as file_in:
    constellations = json.load(file_in)
stars = list()
for constellation in constellations:
    for star in constellation['brightest_stars']:
        stars.append({
            'name': star['name'],
            'brightness': star['brightness'],
            'con_name': constellation['name'],
            'con_abbreviation': constellation['abbreviation'],
            'con_area': constellation['area']
        })
with open('stars.csv', 'w', encoding='utf-8', newline='') as file_out:
    writer = csv.DictWriter(file_out, fieldnames=stars[0].keys(), delimiter=' ')
    writer.writeheader()
    for star in stars:
        writer.writerow(star)
