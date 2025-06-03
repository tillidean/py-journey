# -*- coding: utf-8 -*-
# Beispiel: Python-Objekte in eine JSON-Datei schreiben

import json
import os

# Zu speichernde Daten
user_settings = {
    "userID": 101,
    "username": "testuser",
    "theme": "dark",
    "notifications": {
        "email": True,
        "sms": False,
        "push": True
    },
    "bookmarks": ["artikel1", "video2", "tutorial3"]
}

dateiname = "einstellungen.json"

print(f"--- Speichere Python-Dictionary in '{dateiname}' ---")
try:
    with open(dateiname, "w", encoding="utf-8") as json_datei:
        # json.dump() schreibt das Python-Objekt direkt in das Dateiobjekt
        # indent=4 sorgt für eine menschenlesbare Formatierung
        json.dump(user_settings, json_datei, indent=4, ensure_ascii=False)
        # ensure_ascii=False ist nützlich, wenn man Umlaute etc. direkt lesbar speichern will
    print(f"Daten erfolgreich in '{dateiname}' geschrieben.")

    # Optional: Inhalt der Datei zur Kontrolle ausgeben
    print(f"\n--- Inhalt von '{dateiname}' (zur Kontrolle): ---")
    with open(dateiname, "r", encoding="utf-8") as f_check:
        print(f_check.read())

except IOError as e:
    print(f"Fehler beim Schreiben der JSON-Datei: {e}")
except Exception as e_all:
    print(f"Ein allgemeiner Fehler ist aufgetreten: {e_all}")
finally:
    # Aufräumen (optional)
    if os.path.exists(dateiname):
        # os.remove(dateiname)
        # print(f"\nDatei '{dateiname}' wurde zu Testzwecken wieder gelöscht.")
        pass # Belasse die Datei für das nächste Beispiel (04_json_datei_zu_python.py)