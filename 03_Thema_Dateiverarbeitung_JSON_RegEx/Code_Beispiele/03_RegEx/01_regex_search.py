# -*- coding: utf-8 -*-
# Beispiel: re.search() - Findet das erste Vorkommen eines Musters

import re

text = "Der schnelle braune Fuchs springt über den faulen Hund. Der Fuchs ist schlau."

muster = r"Fuchs"  # Einfaches String-Muster

print(f"Text: '{text}'")
print(f"Muster: '{muster}'")

# re.search() sucht das Muster irgendwo im String
match_objekt = re.search(muster, text)

if match_objekt:
    print("\n--- Treffer gefunden! ---")
    print(f"Typ des Match-Objekts: {type(match_objekt)}")

    # group(0) oder group() gibt den gesamten gematchten String zurück
    print(f"Gefundener Text (group()): {match_objekt.group()}")

    # start() gibt den Startindex des Matches zurück
    print(f"Startindex: {match_objekt.start()}")

    # end() gibt den Endindex des Matches zurück (exklusiv)
    print(f"Endindex: {match_objekt.end()}")

    # span() gibt ein Tupel (start, end) zurück
    print(f"Span (Start, Ende): {match_objekt.span()}")
else:
    print("\nKein Treffer gefunden.")

# Beispiel mit einem komplexeren Muster und Gruppen
text2 = "Meine Telefonnummer ist 0123-4567890 und meine E-Mail max.mustermann@example.com"
# Muster, um eine Telefonnummer zu finden und Vorwahl/Nummer zu gruppieren
# r"" -> Raw String, wichtig für RegEx, um Backslashes korrekt zu interpretieren
# (\d{4}) -> Gruppe 1: Vier Ziffern (Vorwahl)
# -? -> Optionaler Bindestrich
# (\d+) -> Gruppe 2: Eine oder mehrere Ziffern (Hauptnummer)
tel_muster = r"(\d{3,4})-?(\d+)"

print(f"\nText2: '{text2}'")
print(f"Telefonmuster: '{tel_muster}'")

tel_match = re.search(tel_muster, text2)

if tel_match:
    print("\n--- Telefonnummer gefunden! ---")
    print(f"Gesamter Match (group(0)): {tel_match.group(0)}")  # oder .group()
    print(f"Gruppe 1 (Vorwahl): {tel_match.group(1)}")
    print(f"Gruppe 2 (Hauptnummer): {tel_match.group(2)}")
    print(f"Alle Gruppen als Tupel (groups()): {tel_match.groups()}")
else:
    print("\nKeine Telefonnummer im Format XXXX-XXXXXXX gefunden.")

# Was passiert, wenn das Muster nicht passt?
nicht_passendes_muster = r"Katze"
kein_match = re.search(nicht_passendes_muster, text)
if kein_match:
    print(f"\nUnerwartet: '{nicht_passendes_muster}' gefunden.")
else:
    print(f"\nErwartet: '{nicht_passendes_muster}' wurde nicht in '{text}' gefunden.")