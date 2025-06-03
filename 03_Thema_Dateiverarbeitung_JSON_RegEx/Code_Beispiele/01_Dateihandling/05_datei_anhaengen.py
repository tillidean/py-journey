# -*- coding: utf-8 -*-
# Beispiel: Inhalt an eine Datei anhängen

dateiname_anhaengen = "anhaenge_beispiel.log"

# Schritt 1: Datei erstellen und initialen Inhalt schreiben (Modus 'w')
try:
    with open(dateiname_anhaengen, "w", encoding="utf-8") as f:
        f.write("Log-Datei gestartet.\n")
        f.write("Erster Eintrag: System initialisiert.\n")
    print(f"'{dateiname_anhaengen}' erstellt und initial befüllt.")
except IOError as e:
    print(f"Fehler beim initialen Schreiben: {e}")

# Inhalt anzeigen
print("\n--- Inhalt nach initialem Schreiben ---")
try:
    with open(dateiname_anhaengen, "r", encoding="utf-8") as f:
        print(f.read())
except IOError as e:
    print(f"Fehler beim Lesen: {e}")


# Schritt 2: Neuen Inhalt an die Datei anhängen (Modus 'a')
print(f"\n--- Hänge neuen Inhalt an '{dateiname_anhaengen}' an ---")
try:
    with open(dateiname_anhaengen, "a", encoding="utf-8") as f: # 'a' für append
        f.write("Zweiter Eintrag: Benutzer hat sich angemeldet.\n")
        f.write("Dritter Eintrag: Wichtige Operation ausgeführt.\n")
    print("Neuer Inhalt erfolgreich angehängt.")
except IOError as e:
    print(f"Fehler beim Anhängen: {e}")

# Inhalt erneut anzeigen, um die Änderungen zu sehen
print("\n--- Inhalt nach dem Anhängen ---")
try:
    with open(dateiname_anhaengen, "r", encoding="utf-8") as f:
        print(f.read())
except IOError as e:
    print(f"Fehler beim Lesen: {e}")


# Aufräumen
import os
if os.path.exists(dateiname_anhaengen):
    os.remove(dateiname_anhaengen)
print("\nTestdatei ggf. gelöscht.")