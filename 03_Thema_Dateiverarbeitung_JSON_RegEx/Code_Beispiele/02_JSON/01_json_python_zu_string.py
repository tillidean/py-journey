# -*- coding: utf-8 -*-
# Beispiel: Python-Objekte in JSON-Strings umwandeln (Serialisierung)

import json

# Ein Python-Dictionary
person_dict = {
    "name": "Max Mustermann",
    "alter": 30,
    "stadt": "Berlin",
    "istStudent": False,
    "kurse": [
        {"titel": "Python Grundlagen", "semester": 1},
        {"titel": "Webentwicklung", "semester": 2}
    ],
    "telefon": None # None wird zu null in JSON
}

print("--- Python Dictionary ---")
print(person_dict)

# Umwandlung in einen JSON-String
# json.dumps() -> dump string
json_string_person = json.dumps(person_dict)
print("\n--- JSON-String (kompakt) ---")
print(json_string_person)

# Umwandlung in einen schön formatierten JSON-String mit Einrückung
json_string_formatiert = json.dumps(person_dict, indent=4)
print("\n--- JSON-String (formatiert mit indent=4) ---")
print(json_string_formatiert)

# Sortieren der Schlüssel im JSON-String
json_string_sortiert = json.dumps(person_dict, indent=4, sort_keys=True)
print("\n--- JSON-String (formatiert & Schlüssel sortiert) ---")
print(json_string_sortiert)


# Eine Python-Liste
zahlen_liste = [1, 2, {"a": 3, "b": 4}, 5, True, None, "Hallo"]
print("\n--- Python Liste ---")
print(zahlen_liste)

json_string_liste = json.dumps(zahlen_liste, indent=2)
print("\n--- JSON-String von Liste (formatiert mit indent=2) ---")
print(json_string_liste)