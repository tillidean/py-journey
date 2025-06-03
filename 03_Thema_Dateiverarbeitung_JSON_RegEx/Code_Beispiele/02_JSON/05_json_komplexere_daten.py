# -*- coding: utf-8 -*-
# Beispiel: Arbeiten mit komplexeren JSON-Strukturen in Python

import json

# Ein komplexerer JSON-String (z.B. von einer API)
api_antwort_string = """
{
  "query": "Python Bücher",
  "ergebnisseAnzahl": 2,
  "buecher": [
    {
      "id": "isbn123",
      "titel": "Python für Alle",
      "autor": {"vorname": "Ada", "nachname": "Lovelace"},
      "jahr": 2023,
      "kapitel": [
        {"nr": 1, "titel": "Einführung"},
        {"nr": 2, "titel": "Variablen und Typen"},
        {"nr": 3, "titel": "Schleifen"}
      ],
      "tags": ["Python", "Programmierung", "Anfänger"]
    },
    {
      "id": "isbn456",
      "titel": "Datenstrukturen in Python",
      "autor": {"vorname": "Alan", "nachname": "Turing"},
      "jahr": 2022,
      "kapitel": [
        {"nr": 1, "titel": "Listen und Tupel"},
        {"nr": 2, "titel": "Dictionaries und Sets"}
      ],
      "tags": ["Python", "Datenstrukturen", "Fortgeschritten"],
      "verlag": "TechBooks Inc."
    }
  ],
  "fehler": null
}
"""

print("--- Lade und verarbeite komplexen JSON-String ---")
try:
    daten = json.loads(api_antwort_string)

    # Informationen ausgeben
    print(f"Suchanfrage: {daten['query']}")
    print(f"Anzahl der Ergebnisse: {daten['ergebnisseAnzahl']}")

    print("\nBücher:")
    for buch in daten["buecher"]:
        print(f"\n  Titel: {buch['titel']}")
        # Sicherer Zugriff auf verschachtelte Autoreninformationen
        autor_info = buch.get("autor", {})  # Default zu leerem Dict, falls "autor" fehlt
        print(f"  Autor: {autor_info.get('vorname', 'N/A')} {autor_info.get('nachname', 'N/A')}")
        print(f"  Jahr: {buch['jahr']}")

        print("  Erstes Kapitel:", end=" ")
        if buch["kapitel"]:  # Prüfen, ob die Kapitelliste nicht leer ist
            print(f"{buch['kapitel'][0]['nr']}. {buch['kapitel'][0]['titel']}")
        else:
            print("Keine Kapitelinformationen")

        print(f"  Tags: {', '.join(buch['tags'])}")  # Liste von Strings zu einem String verbinden

        # Prüfen, ob ein optionales Feld existiert
        if "verlag" in buch:
            print(f"  Verlag: {buch['verlag']}")

    # Daten modifizieren (Beispiel)
    # Füge ein neues Tag zum ersten Buch hinzu
    if daten["buecher"]:
        daten["buecher"][0]["tags"].append("E-Book")
        daten["buecher"][0]["jahr"] = 2024  # Jahr aktualisieren

    print("\n--- Modifizierte Daten (als JSON-String) ---")
    modifizierter_json_string = json.dumps(daten, indent=2, ensure_ascii=False)
    print(modifizierter_json_string)

except json.JSONDecodeError as e:
    print(f"Fehler beim Parsen des JSON: {e}")
except KeyError as e:
    print(f"Fehler beim Zugriff auf einen Schlüssel: {e} fehlt im JSON-Objekt.")
except Exception as e_all:
    print(f"Ein allgemeiner Fehler: {e_all}")