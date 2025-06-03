# -*- coding: utf-8 -*-
# Beispiel: Daten aus einer JSON-Datei in Python-Objekte laden

import json
import os

dateiname = "einstellungen.json"  # Diese Datei sollte vom Skript 03 erstellt worden sein

# Überprüfen, ob die Datei existiert, bevor wir versuchen, sie zu laden
if not os.path.exists(dateiname):
    print(f"Fehler: Die Datei '{dateiname}' existiert nicht.")
    print("Bitte führe zuerst das Skript '03_json_python_zu_datei.py' aus, um sie zu erstellen.")
else:
    print(f"--- Lade Daten aus JSON-Datei '{dateiname}' ---")
    try:
        with open(dateiname, "r", encoding="utf-8") as json_datei:
            # json.load() liest aus dem Dateiobjekt und deserialisiert zu einem Python-Objekt
            geladene_einstellungen = json.load(json_datei)

        print("Daten erfolgreich geladen.")
        print("Typ des geladenen Objekts:", type(geladene_einstellungen))

        print("\n--- Geladene Einstellungen ---")
        # Zugriff auf die Daten wie bei einem normalen Python-Dictionary
        print(f"UserID: {geladene_einstellungen.get('userID')}")
        print(f"Username: {geladene_einstellungen.get('username')}")
        print(f"Theme: {geladene_einstellungen.get('theme')}")

        notifications = geladene_einstellungen.get("notifications", {})  # Default to empty dict
        print(f"E-Mail Benachrichtigungen: {notifications.get('email')}")

        print("Lesezeichen:")
        for bookmark in geladene_einstellungen.get("bookmarks", []):  # Default to empty list
            print(f"- {bookmark}")

    except json.JSONDecodeError as e:
        print(f"Fehler beim Parsen der JSON-Datei '{dateiname}': {e}")
        print("Stelle sicher, dass die Datei valides JSON enthält.")
    except IOError as e:
        print(f"Fehler beim Lesen der Datei '{dateiname}': {e}")
    except Exception as e_all:
        print(f"Ein allgemeiner Fehler ist aufgetreten: {e_all}")
    finally:
        # Optional: Datei nach dem Test löschen
        if os.path.exists(dateiname):
            os.remove(dateiname)
            print(f"\nTestdatei '{dateiname}' wurde nach dem Lesen gelöscht.")