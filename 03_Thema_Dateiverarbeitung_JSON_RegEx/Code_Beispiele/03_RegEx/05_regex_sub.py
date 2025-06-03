# -*- coding: utf-8 -*-
# Beispiel: re.sub() - Suchen und Ersetzen

import re

text = "Der Kunde Max Müller hat die Telefonnummer 0123-45678. Herr Müller ist 30."

print(f"Originaltext: '{text}'")

# Ersetze alle Vorkommen von "Müller" durch "Mustermann"
text_ersetzt1 = re.sub(r"Müller", "Mustermann", text)
print(f"\nNach Ersetzung von 'Müller':\n'{text_ersetzt1}'")

# Ersetze alle Ziffernfolgen durch "[ZENSIERT]"
# \d+ -> eine oder mehrere Ziffern
text_zensiert = re.sub(r"\d+", "[ZENSIERT]", text)
print(f"\nNach Zensur von Zahlen:\n'{text_zensiert}'")

# Ersetze nur die ersten N Vorkommen (mit count Parameter)
text_teilersetzt = re.sub(r"Der|der", "Ein", text, count=1, flags=re.IGNORECASE) # Ignoriere Groß/Kleinschreibung
print(f"\nNach teilweiser Ersetzung von 'Der'/'der' (count=1, ignorecase):\n'{text_teilersetzt}'")

# Verwendung von Gruppen im Ersetzungstext
# Tausche Vorname und Nachname: "Max Müller" -> "Müller, Max"
text_namenstausch = "Kunden: Max Müller, Erika Mustermann, Klaus Kleber"
# (\w+)    -> Gruppe 1: Vorname (ein oder mehrere Wortzeichen)
# \s+      -> Ein oder mehrere Leerzeichen
# (\w+)    -> Gruppe 2: Nachname
muster_name = r"(\w+)\s+(\w+)"
ersetzung_name = r"\2, \1" # \2 referenziert Gruppe 2, \1 Gruppe 1

print(f"\nOriginal Namen: '{text_namenstausch}'")
text_namen_getauscht = re.sub(muster_name, ersetzung_name, text_namenstausch)
print(f"Namen getauscht:\n'{text_namen_getauscht}'")


# Verwendung einer Funktion für die Ersetzung
def hex_ersetzer(match_objekt):
    """Nimmt ein Match-Objekt einer Zahl und gibt es als Hex-String zurück."""
    dezimal_wert = int(match_objekt.group(0)) # group(0) ist der gesamte Match
    return hex(dezimal_wert)

text_mit_zahlen = "Die Werte sind 10, 255 und 42."
print(f"\nOriginal mit Zahlen: '{text_mit_zahlen}'")
# Ersetze alle Zahlen durch ihre Hexadezimal-Repräsentation
text_mit_hex = re.sub(r"\d+", hex_ersetzer, text_mit_zahlen)
print(f"Zahlen durch Hex ersetzt:\n'{text_mit_hex}'")