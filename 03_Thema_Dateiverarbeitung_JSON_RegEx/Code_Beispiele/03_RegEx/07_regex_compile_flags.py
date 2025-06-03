# -*- coding: utf-8 -*-
# Beispiel: re.compile() und Verwendung von Flags

import re

text = "Python ist toll. PYTHON ist mächtig. python ist flexibel."
print(f"Text: '{text}'")

# Ohne Flags (Groß-/Kleinschreibung wird beachtet)
muster_normal = r"Python"
treffer_normal = re.findall(muster_normal, text)
print(f"\nSuche nach '{muster_normal}' (case-sensitive): {treffer_normal}") # Findet nur 'Python'

# Mit re.IGNORECASE (oder re.I) Flag
# Option 1: Flag direkt in der Funktion übergeben
treffer_ignorecase_direkt = re.findall(muster_normal, text, flags=re.IGNORECASE)
print(f"Suche nach '{muster_normal}' (ignorecase, direkt): {treffer_ignorecase_direkt}")

# Option 2: Muster vorkompilieren mit re.compile() und Flag
# Dies ist effizienter, wenn dasselbe Muster (mit denselben Flags) oft verwendet wird.
kompiliertes_muster_ic = re.compile(muster_normal, flags=re.IGNORECASE)
print(f"\nKompiliertes Muster: {kompiliertes_muster_ic}")

treffer_ignorecase_kompiliert = kompiliertes_muster_ic.findall(text)
print(f"Suche mit kompiliertem Muster (ignorecase): {treffer_ignorecase_kompiliert}")


# Beispiel mit re.MULTILINE (oder re.M)
# ^ und $ matchen normalerweise nur den Anfang/Ende des gesamten Strings.
# Mit re.MULTILINE matchen sie auch den Anfang/Ende jeder Zeile.
mehrzeiliger_text = """Zeile 1 endet hier.
Zeile 2 beginnt hier und endet auch hier.
Letzte Zeile 3."""
print(f"\nMehrzeiliger Text:\n{mehrzeiliger_text}")

# Finde Zeilen, die mit "Zeile" beginnen
muster_zeilenanfang = r"^Zeile"

treffer_multiline = re.findall(muster_zeilenanfang, mehrzeiliger_text, flags=re.MULTILINE)
print(f"Suche nach '{muster_zeilenanfang}' (multiline): {treffer_multiline}")

treffer_ohne_multiline = re.findall(muster_zeilenanfang, mehrzeiliger_text)
print(f"Suche nach '{muster_zeilenanfang}' (ohne multiline): {treffer_ohne_multiline}") # Findet nur einmal


# Beispiel mit re.DOTALL (oder re.S)
# Der Punkt . matcht normalerweise jedes Zeichen AUSSER einem Zeilenumbruch (\n).
# Mit re.DOTALL matcht der Punkt . auch Zeilenumbrüche.
text_mit_umbruch = "Anfang...Beliebiger Text\nNeue Zeile...Ende"
print(f"\nText mit Umbruch: '{text_mit_umbruch}'")

muster_punkt_normal = r"Anfang.*Ende" # .* -> null oder mehr beliebige Zeichen (ohne \n)
match_punkt_normal = re.search(muster_punkt_normal, text_mit_umbruch)
if match_punkt_normal:
    print(f"Suche nach '{muster_punkt_normal}' (normal): Gefunden '{match_punkt_normal.group()}'")
else:
    print(f"Suche nach '{muster_punkt_normal}' (normal): Nicht gefunden (wegen Zeilenumbruch)")


muster_punkt_dotall = r"Anfang.*Ende"
match_punkt_dotall = re.search(muster_punkt_dotall, text_mit_umbruch, flags=re.DOTALL)
if match_punkt_dotall:
    print(f"Suche nach '{muster_punkt_dotall}' (re.DOTALL): Gefunden '{match_punkt_dotall.group()}'")
else:
    print(f"Suche nach '{muster_punkt_dotall}' (re.DOTALL): Nicht gefunden")