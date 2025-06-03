# -*- coding: utf-8 -*-
# Beispiel: JSON-Strings in Python-Objekte umwandeln (Deserialisierung)

import json

# Ein JSON-String, der ein Objekt repräsentiert
json_string_objekt = """
{
    "produktName": "Super Laptop",
    "preis": 1299.99,
    "aufLager": true,
    "spezifikationen": {
        "cpu": "Intel i7",
        "ramGB": 16,
        "festplatteSSDGB": 512
    },
    "bewertungen": null
}
"""

print("--- JSON-String (Objekt) ---")
print(json_string_objekt)

# Umwandlung des JSON-Strings in ein Python-Dictionary
# json.loads() -> load string
try:
    python_dict = json.loads(json_string_objekt)
    print("\n--- Python Dictionary (aus JSON-String) ---")
    print(python_dict)
    print(f"\nProdukttyp: {type(python_dict)}")
    print(f"Produktname: {python_dict['produktName']}")
    print(f"RAM: {python_dict['spezifikationen']['ramGB']} GB")
    if python_dict["bewertungen"] is None:
        print("Es gibt noch keine Bewertungen.")

except json.JSONDecodeError as e:
    print(f"\nFehler beim Parsen des JSON-Strings: {e}")


# Ein JSON-String, der ein Array repräsentiert
json_string_array = """
[
    "Apfel",
    "Banane",
    "Kirsche",
    {"typ": "Gemüse", "name": "Brokkoli"},
    42,
    false
]
"""
print("\n--- JSON-String (Array) ---")
print(json_string_array)

try:
    python_liste = json.loads(json_string_array)
    print("\n--- Python Liste (aus JSON-String) ---")
    print(python_liste)
    print(f"Listentyp: {type(python_liste)}")
    print(f"Erstes Element: {python_liste[0]}")
    print(f"Name des Gemüses: {python_liste[3]['name']}")

except json.JSONDecodeError as e:
    print(f"\nFehler beim Parsen des JSON-Strings: {e}")