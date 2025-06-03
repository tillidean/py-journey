# -*- coding: utf-8 -*-
# Beispiel: Die Wichtigkeit von Raw Strings (r"...") für Reguläre Ausdrücke

import re

# Problem: Backslashes in normalen Python-Strings und in RegEx
# In Python ist \n ein Zeilenumbruch, \t ein Tabulator etc.
# In RegEx ist \d eine Ziffer, \s ein Whitespace etc.
# Wenn man ein RegEx-Muster definieren will, das einen literalen Backslash
# gefolgt von einem 'd' (\d) enthält, wird es kompliziert.

# Beispiel: Wir wollen das Muster \section finden (literaler Backslash, dann "section")
# In einem normalen String müsste man den Backslash escapen: "\\"
# Das RegEx-Modul interpretiert dann "\\section" als literalen Backslash gefolgt von "section".
normaler_string_muster = "\\section"
text_mit_section = "Dies ist \section{Einleitung}"

print(f"Text: '{text_mit_section}'")
print(f"Normaler String als Muster: '{normaler_string_muster}' (Python sieht: '\\\\section')")

match_normal = re.search(normaler_string_muster, text_mit_section)
if match_normal:
    print(f"Mit normalem String gefunden: '{match_normal.group()}'") # Funktioniert hier zufällig, weil \s nicht \s ist
else:
    print("Mit normalem String nicht gefunden.")


# Problem deutlicher bei RegEx-Spezialsequenzen:
# Angenommen, wir wollen \b (Wortgrenze) in einem normalen String verwenden.
# Python würde \b als Backspace-Zeichen interpretieren, wenn es nicht escaped wird.
# Für das RegEx-Modul müsste man schreiben: "\\bWort\\b"
muster_wortgrenze_normal = "\\bWort\\b"
text_wort = "Das Wort ist wichtig."
print(f"\nText für Wortgrenze: '{text_wort}'")
print(f"Normaler String für Wortgrenze: '{muster_wortgrenze_normal}'")

match_wort_normal = re.search(muster_wortgrenze_normal, text_wort)
if match_wort_normal:
    print(f"Wort mit normalem String und doppelten Backslashes gefunden: '{match_wort_normal.group()}'")
else:
    print("Wort mit normalem String und doppelten Backslashes nicht gefunden.")


# Die Lösung: Raw Strings!
# In einem Raw String (r"...") haben Backslashes keine spezielle Bedeutung für Python.
# Python übergibt den String so an das RegEx-Modul, wie er geschrieben wurde.
# Das RegEx-Modul kann dann \d, \s, \b etc. korrekt als seine eigenen Spezialsequenzen interpretieren.

raw_string_muster_section = r"\section" # Python übergibt "\section" an re
print(f"\nRaw String als Muster: '{raw_string_muster_section}' (Python übergibt: '\\section')")
match_raw = re.search(raw_string_muster_section, text_mit_section)
if match_raw:
    print(f"Mit Raw String gefunden: '{match_raw.group()}'")
else:
    print("Mit Raw String nicht gefunden.")


muster_wortgrenze_raw = r"\bWort\b" # Python übergibt "\bWort\b" an re
print(f"Raw String für Wortgrenze: '{muster_wortgrenze_raw}'")
match_wort_raw = re.search(muster_wortgrenze_raw, text_wort)
if match_wort_raw:
    print(f"Wort mit Raw String gefunden: '{match_wort_raw.group()}'")
else:
    print("Wort mit Raw String nicht gefunden.")

print("\nFazit: IMMER Raw Strings (r\"...\") für Reguläre Ausdrücke in Python verwenden,")
print("um Verwirrung und Fehler durch die doppelte Interpretation von Backslashes zu vermeiden!")