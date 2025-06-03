# -*- coding: utf-8 -*-
# Beispiel: Verzeichnisoperationen mit dem os-Modul

import os

neuer_ordner_name = "mein_neuer_testordner"
unterordner_name = os.path.join(neuer_ordner_name, "unterordner") # Pfade korrekt verbinden

# 1. Verzeichnis erstellen mit os.mkdir()
print(f"--- Erstelle Verzeichnis '{neuer_ordner_name}' ---")
try:
    os.mkdir(neuer_ordner_name)
    print(f"Verzeichnis '{neuer_ordner_name}' erfolgreich erstellt.")
except FileExistsError:
    print(f"Fehler: Verzeichnis '{neuer_ordner_name}' existiert bereits.")
except OSError as e:
    print(f"Fehler beim Erstellen von '{neuer_ordner_name}': {e}")

# 2. Verzeichnisse erstellen mit os.makedirs() (erstellt auch Zwischenverzeichnisse)
print(f"\n--- Erstelle Verzeichnisstruktur '{unterordner_name}' mit os.makedirs() ---")
try:
    os.makedirs(unterordner_name, exist_ok=True) # exist_ok=True verhindert Fehler, wenn Ordner schon existiert
    print(f"Verzeichnisstruktur '{unterordner_name}' erfolgreich erstellt oder existierte bereits.")
except OSError as e:
    print(f"Fehler beim Erstellen von '{unterordner_name}': {e}")


# 3. Inhalt eines Verzeichnisses auflisten mit os.listdir()
print(f"\n--- Inhalt von '{neuer_ordner_name}' auflisten ---")
if os.path.exists(neuer_ordner_name) and os.path.isdir(neuer_ordner_name):
    try:
        inhalt = os.listdir(neuer_ordner_name)
        if inhalt:
            print(f"Inhalt von '{neuer_ordner_name}': {inhalt}")
            # Dummy-Datei im Unterordner erstellen für den nächsten Test
            with open(os.path.join(unterordner_name, "dummy.txt"), "w") as f:
                f.write("test")
        else:
            print(f"Verzeichnis '{neuer_ordner_name}' ist leer.")
    except OSError as e:
        print(f"Fehler beim Auflisten von '{neuer_ordner_name}': {e}")
else:
    print(f"Verzeichnis '{neuer_ordner_name}' nicht gefunden.")


# 4. Leeres Verzeichnis löschen mit os.rmdir()
# Zuerst den Unterordner (der jetzt eine Datei enthält) versuchen zu löschen -> Fehler erwartet
print(f"\n--- Versuche, nicht-leeren Unterordner '{unterordner_name}' mit os.rmdir() zu löschen ---")
if os.path.exists(unterordner_name):
    try:
        os.rmdir(unterordner_name)
        print(f"Verzeichnis '{unterordner_name}' gelöscht (unerwartet, da nicht leer).")
    except OSError as e:
        print(f"Erwarteter Fehler beim Löschen von '{unterordner_name}': {e} (Verzeichnis nicht leer?)")
        # Datei im Unterordner löschen, um ihn leer zu machen
        dummy_file_path = os.path.join(unterordner_name, "dummy.txt")
        if os.path.exists(dummy_file_path):
            os.remove(dummy_file_path)
            print(f"Dummy-Datei '{dummy_file_path}' gelöscht.")
        # Jetzt den leeren Unterordner löschen
        try:
            os.rmdir(unterordner_name)
            print(f"Leeres Verzeichnis '{unterordner_name}' jetzt erfolgreich gelöscht.")
        except OSError as e_inner:
            print(f"Fehler beim Löschen des nun leeren '{unterordner_name}': {e_inner}")


# Den Hauptordner löschen (sollte jetzt leer sein oder nur noch der leere Unterordner, der gelöscht wurde)
print(f"\n--- Leeres Verzeichnis '{neuer_ordner_name}' mit os.rmdir() löschen ---")
if os.path.exists(neuer_ordner_name):
    try:
        os.rmdir(neuer_ordner_name)
        print(f"Verzeichnis '{neuer_ordner_name}' erfolgreich gelöscht.")
    except OSError as e:
        print(f"Fehler beim Löschen von '{neuer_ordner_name}': {e} (Ist es wirklich leer?)")
else:
    print(f"Verzeichnis '{neuer_ordner_name}' wurde nicht gefunden.")

# Überprüfung
if not os.path.exists(neuer_ordner_name):
    print(f"Verzeichnis '{neuer_ordner_name}' existiert nicht mehr (wie erwartet).")