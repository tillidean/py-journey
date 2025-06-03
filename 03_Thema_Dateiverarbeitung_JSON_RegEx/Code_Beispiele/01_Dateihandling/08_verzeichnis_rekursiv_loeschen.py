# -*- coding: utf-8 -*-
# Beispiel: Verzeichnisse rekursiv löschen mit shutil.rmtree()

import os
import shutil  # Shell Utilities Modul

ordner_zum_loeschen_komplett = "komplett_zu_loeschender_ordner"

# 1. Eine komplexere Verzeichnisstruktur mit Dateien erstellen
print(f"--- Erstelle Test-Verzeichnisstruktur '{ordner_zum_loeschen_komplett}' ---")
try:
    # Hauptordner
    os.makedirs(ordner_zum_loeschen_komplett, exist_ok=True)

    # Unterordner und Dateien
    unterordner1 = os.path.join(ordner_zum_loeschen_komplett, "ebene1")
    os.makedirs(unterordner1, exist_ok=True)
    with open(os.path.join(ordner_zum_loeschen_komplett, "datei_root.txt"), "w") as f:
        f.write("Inhalt Root")
    with open(os.path.join(unterordner1, "datei_ebene1.txt"), "w") as f:
        f.write("Inhalt Ebene 1")

    unterordner2 = os.path.join(unterordner1, "ebene2")
    os.makedirs(unterordner2, exist_ok=True)
    with open(os.path.join(unterordner2, "datei_ebene2.txt"), "w") as f:
        f.write("Inhalt Ebene 2")
    print(f"Test-Verzeichnisstruktur '{ordner_zum_loeschen_komplett}' erstellt.")

except OSError as e:
    print(f"Fehler beim Erstellen der Teststruktur: {e}")
    exit()

# 2. Verzeichnis (samt Inhalt) mit shutil.rmtree() löschen
print(f"\n--- Lösche Verzeichnis '{ordner_zum_loeschen_komplett}' und seinen gesamten Inhalt ---")

# WICHTIG: Eine Sicherheitsabfrage oder zumindest eine klare Warnung ist empfehlenswert!
# input_check = input(f"ACHTUNG: Bist du sicher, dass du den Ordner '{ordner_zum_loeschen_komplett}' und seinen gesamten Inhalt unwiderruflich löschen willst? (ja/nein): ")
# if input_check.lower() != 'ja':
#     print("Löschvorgang abgebrochen.")
#     exit()

if os.path.exists(ordner_zum_loeschen_komplett):
    try:
        print(f"!!! ACHTUNG: Gleich wird der Ordner '{ordner_zum_loeschen_komplett}' rekursiv gelöscht !!!")
        # Hier könnte man eine kurze Pause einbauen, damit der Benutzer das lesen kann
        # import time
        # time.sleep(3)
        shutil.rmtree(ordner_zum_loeschen_komplett)
        print(f"Verzeichnis '{ordner_zum_loeschen_komplett}' und sein gesamter Inhalt wurden erfolgreich gelöscht.")
    except OSError as e:
        print(f"Fehler beim Löschen des Verzeichnisses '{ordner_zum_loeschen_komplett}': {e}")
else:
    print(f"Verzeichnis '{ordner_zum_loeschen_komplett}' wurde nicht gefunden.")

# 3. Überprüfung
if not os.path.exists(ordner_zum_loeschen_komplett):
    print(f"Verzeichnis '{ordner_zum_loeschen_komplett}' existiert nicht mehr (wie erwartet).")
else:
    print(f"FEHLER: Verzeichnis '{ordner_zum_loeschen_komplett}' existiert immer noch!")

print("\n--- Wichtiger Hinweis zu shutil.rmtree() ---")
print("shutil.rmtree() ist sehr mächtig und löscht ohne Rückfrage.")
print("Sei EXTREM VORSICHTIG bei der Verwendung dieses Befehls, besonders mit Variablen in Pfaden.")
print("Ein Tippfehler kann zu erheblichem Datenverlust führen!")