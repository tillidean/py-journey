# -*- coding: utf-8 -*-
# Beispiel: Gruppen (Capturing Groups) in Regulären Ausdrücken

import re

text = "Name: Max Mustermann, Alter: 30, Beruf: Entwickler"
print(f"Text: '{text}'")

# Muster, um Name, Alter und Beruf zu extrahieren
# Jede Klammer () definiert eine "Capturing Group"
# Gruppe 1: (\w+\s\w+)     -> Name (zwei Wörter mit Leerzeichen dazwischen)
# Gruppe 2: (\d+)          -> Alter (eine oder mehrere Ziffern)
# Gruppe 3: ([\w\s]+)      -> Beruf (ein oder mehrere Wortzeichen oder Leerzeichen)
muster_mit_gruppen = r"Name: (\w+\s\w+), Alter: (\d+), Beruf: ([\w\s]+)"

match = re.search(muster_mit_gruppen, text)

if match:
    print("\n--- Informationen extrahiert ---")
    # match.group(0) oder match.group() ist immer der gesamte gematchte String
    print(f"Gesamter Match (group(0)): '{match.group(0)}'")

    # Zugriff auf die einzelnen Gruppen über ihren Index (beginnend bei 1)
    print(f"Name (Gruppe 1): '{match.group(1)}'")
    print(f"Alter (Gruppe 2): '{match.group(2)}'")
    print(f"Beruf (Gruppe 3): '{match.group(3)}'")

    # match.groups() gibt ein Tupel aller Gruppen zurück
    print(f"Alle Gruppen als Tupel (groups()): {match.groups()}")  # ('Max Mustermann', '30', 'Entwickler')

    # Man kann Gruppen auch Namen geben (Named Capturing Groups)
    # Syntax: (?P<name>...)
    muster_benannte_gruppen = r"Name: (?P<vollname>\w+\s\w+), Alter: (?P<lebensalter>\d+), Beruf: (?P<job>[\w\s]+)"

    match_benannt = re.search(muster_benannte_gruppen, text)
    if match_benannt:
        print("\n--- Informationen mit benannten Gruppen ---")
        print(f"Name (via Name 'vollname'): '{match_benannt.group('vollname')}'")
        print(f"Alter (via Name 'lebensalter'): '{match_benannt.group('lebensalter')}'")
        print(f"Beruf (via Name 'job'): '{match_benannt.group('job')}'")

        # groupdict() gibt ein Dictionary der benannten Gruppen zurück
        print(f"Benannte Gruppen als Dictionary (groupdict()): {match_benannt.groupdict()}")
else:
    print("Kein Match für das detaillierte Muster gefunden.")

# Non-Capturing Groups (?:...)
# Manchmal möchte man Teile eines Musters gruppieren (z.B. für Quantifizierer oder Alternativen),
# aber diese Gruppe nicht als Ergebnis "einfangen".
text_version = "Version: 1.2.3-beta"
# Wir wollen die gesamte Version, aber nicht "Version: "
# (?:Version:\s*) -> Non-capturing group für "Version: "
# ([\d\.\w-]+)    -> Capturing group für die eigentliche Versionsnummer
muster_version = r"(?:Version:\s*)([\d\.\w-]+)"

match_version = re.search(muster_version, text_version)
if match_version:
    print(f"\n--- Versionsextraktion mit Non-Capturing Group ---")
    print(f"Gesamter Match: '{match_version.group(0)}'")  # "Version: 1.2.3-beta"
    print(f"Nur die Version (Gruppe 1): '{match_version.group(1)}'")  # "1.2.3-beta"
    print(f"Alle Gruppen (groups()): {match_version.groups()}")  # Nur ('1.2.3-beta',)
else:
    print("Version nicht gefunden.")