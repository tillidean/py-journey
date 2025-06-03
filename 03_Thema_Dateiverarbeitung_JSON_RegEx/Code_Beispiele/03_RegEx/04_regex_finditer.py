# -*- coding: utf-8 -*-
# Beispiel: re.finditer() - Gibt einen Iterator über Match-Objekte zurück

import re

text = "Apfel kostet 2 Euro, Birne 3 Euro, Orange 1 Euro."

# Finde alle Frucht-Preis-Paare
# (\w+)      -> Gruppe 1: Ein oder mehrere Wortzeichen (Frucht)
# \s+kostet\s+ -> " kostet " (mit Leerzeichen)
# (\d+)      -> Gruppe 2: Eine oder mehrere Ziffern (Preis)
# \s+Euro    -> " Euro"
muster = r"(\w+)\s+kostet\s+(\d+)\s+Euro"

print(f"Text: '{text}'")
print(f"Muster: '{muster}'")

# re.finditer() gibt einen Iterator zurück
# Das ist speichereffizienter als findall(), besonders bei vielen Treffern oder großen Texten,
# da nicht alle Treffer gleichzeitig im Speicher gehalten werden.
iterator_matches = re.finditer(muster, text)

print("\n--- Gefundene Frucht-Preis-Paare (mit finditer) ---")
gefunden = False
for match_objekt in iterator_matches:
    gefunden = True
    print(f"\nNächster Treffer:")
    print(f"  Gesamter Match: '{match_objekt.group(0)}'") # oder .group()
    print(f"  Frucht (Gruppe 1): '{match_objekt.group(1)}'")
    print(f"  Preis (Gruppe 2): '{match_objekt.group(2)}'")
    print(f"  Startindex: {match_objekt.start()}")
    print(f"  Endindex: {match_objekt.end()}")

if not gefunden:
    print("Keine Übereinstimmungen gefunden.")

# Noch ein Beispiel: Alle Wörter extrahieren, die auf 'e' enden
text2 = "Eine Biene summt leise. Die Sonne scheint helle."
muster_e_ende = r"\b\w*e\b" # Wortgrenze, beliebige Wortzeichen, 'e', Wortgrenze

print(f"\nText 2: '{text2}'")
print(f"Muster 'e'-Ende: '{muster_e_ende}'")

print("\n--- Wörter, die auf 'e' enden ---")
for match in re.finditer(muster_e_ende, text2, re.IGNORECASE): # Flag für Groß-/Kleinschreibung
    print(f"Gefunden: '{match.group()}' bei Index {match.start()}")