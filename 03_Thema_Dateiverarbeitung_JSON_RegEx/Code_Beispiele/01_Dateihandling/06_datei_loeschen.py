# -*- coding: utf-8 -*-
# Beispiel: Dateien löschen mit dem os-Modul

import os

dateiname_zum_loeschen = "temp_datei_zum_loeschen.txt"

# 1. Testdatei erstellen
try:
    with open(dateiname_zum_loeschen, "w", encoding="utf-8") as f:
        f.write("Dieser Inhalt ist nur temporär da.")
    print(f"Datei '{dateiname_zum_loeschen}' wurde erstellt.")
except IOError as e:
    print(f"Fehler beim Erstellen der Testdatei: {e}")
    # Beenden, wenn Erstellung fehlschlägt, da Löschen dann keinen Sinn macht
    exit()

# 2. Prüfen, ob die Datei existiert (gute Praxis vor dem Löschen)
if os.path.exists(dateiname_zum_loeschen):
    print(f"Datei '{dateiname_zum_loeschen}' existiert.")

    # 3. Datei löschen
    try:
        os.remove(dateiname_zum_loeschen)
        print(f"Datei '{dateiname_zum_loeschen}' wurde erfolgreich gelöscht.")
    except OSError as e:  # OSError ist eine Basisklasse für viele OS-bezogene Fehler
        print(f"Fehler beim Löschen der Datei '{dateiname_zum_loeschen}': {e}")
        print("Mögliche Ursachen: Keine Berechtigung, Datei wird verwendet, etc.")
else:
    print(f"Datei '{dateiname_zum_loeschen}' wurde nicht gefunden und kann nicht gelöscht werden.")

# 4. Erneut prüfen, ob die Datei existiert
if os.path.exists(dateiname_zum_loeschen):
    print(f"Fehler: Datei '{dateiname_zum_loeschen}' existiert immer noch!")
else:
    print(f"Datei '{dateiname_zum_loeschen}' existiert nicht mehr (wie erwartet).")

print("\n--- Versuch, eine nicht existierende Datei zu löschen ---")
nicht_existierende_datei = "diese_datei_gibt_es_nicht.txt"
try:
    os.remove(nicht_existierende_datei)
    print(f"Überraschung! '{nicht_existierende_datei}' wurde gelöscht (sollte nicht passieren).")
except FileNotFoundError:
    print(f"Erwarteter Fehler: Datei '{nicht_existierende_datei}' nicht gefunden und konnte nicht gelöscht werden.")
except OSError as e:
    print(f"Ein anderer OS-Fehler beim Löschversuch: {e}")