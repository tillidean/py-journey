# -*- coding: utf-8 -*-
# Beispiel: Methoden zum Schreiben in Dateien

dateiname_schreiben = "schreib_beispiel.txt"

print(f"--- Schreibe in '{dateiname_schreiben}' mit write() ---")
try:
    with open(dateiname_schreiben, "w", encoding="utf-8") as f: # 'w' überschreibt die Datei
        f.write("Dies ist die erste Zeile, geschrieben mit write().\n")
        f.write("Python ermöglicht einfaches Dateischreiben.\n")
        anzahl_geschriebener_zeichen = f.write("Diese Zeile hat eine bestimmte Länge.")
        print(f"'{anzahl_geschriebener_zeichen}' Zeichen in die letzte Zeile geschrieben.")
    print(f"Inhalt erfolgreich in '{dateiname_schreiben}' geschrieben.")

    # Inhalt zur Kontrolle lesen
    with open(dateiname_schreiben, "r", encoding="utf-8") as f_check:
        print("\nInhalt der Datei:")
        print(f_check.read())
except IOError as e:
    print(f"Fehler beim Schreiben/Lesen: {e}")


dateiname_writelines = "writelines_beispiel.txt"
print(f"\n--- Schreibe in '{dateiname_writelines}' mit writelines() ---")
zeilen_liste = [
    "Zeile 1 für writelines.\n", # Zeilenumbruch \n ist wichtig!
    "Zeile 2, auch mit Umbruch.\n",
    "Letzte Zeile ohne expliziten Umbruch hier im String."
]
try:
    with open(dateiname_writelines, "w", encoding="utf-8") as f:
        f.writelines(zeilen_liste) # Schreibt alle Strings aus der Liste
    print(f"Inhalt erfolgreich in '{dateiname_writelines}' mit writelines() geschrieben.")

    # Inhalt zur Kontrolle lesen
    with open(dateiname_writelines, "r", encoding="utf-8") as f_check:
        print("\nInhalt der Datei:")
        print(f_check.read())
except IOError as e:
    print(f"Fehler beim Schreiben/Lesen: {e}")


# Aufräumen
import os
if os.path.exists(dateiname_schreiben):
    os.remove(dateiname_schreiben)
if os.path.exists(dateiname_writelines):
    os.remove(dateiname_writelines)
print("\nTestdateien ggf. gelöscht.")