# -*- coding: utf-8 -*-
# Beispiel: Dateioperationen mit dem 'with'-Statement

# Das 'with'-Statement stellt sicher, dass die Datei automatisch
# geschlossen wird, auch wenn Fehler auftreten.

# Datei zum Schreiben öffnen (oder erstellen/überschreiben)
dateiname_with = "with_beispiel.txt"
try:
    with open(dateiname_with, "w", encoding="utf-8") as f_write:
        f_write.write("Hallo vom with-Statement!\n")
        f_write.write("Diese Datei wird automatisch geschlossen.\n")
        print(f"In '{dateiname_with}' wurde geschrieben.")
    # An diesem Punkt ist f_write.closed True, die Datei ist zu.
    print(f"Ist die Datei '{dateiname_with}' nach dem with-Block geschlossen? {f_write.closed}")

except IOError as e:
    print(f"Fehler beim Schreiben der Datei: {e}")


# Datei zum Lesen öffnen
try:
    with open(dateiname_with, "r", encoding="utf-8") as f_read:
        print(f"\nInhalt von '{dateiname_with}':")
        inhalt = f_read.read()
        print(inhalt)
    print(f"Ist die Datei '{dateiname_with}' nach dem Lesen geschlossen? {f_read.closed}")

except FileNotFoundError:
    print(f"Fehler: Die Datei '{dateiname_with}' wurde nicht gefunden.")
except IOError as e:
    print(f"Fehler beim Lesen der Datei: {e}")


# Fehlerfall im with-Block simulieren
print("\nSimuliere Fehler im with-Block:")
try:
    with open("fehler_test.txt", "w", encoding="utf-8") as f_error:
        f_error.write("Dieser Text wird geschrieben...\n")
        print("Zeile in 'fehler_test.txt' geschrieben.")
        # Simuliere einen Fehler
        # raise ValueError("Ein simulierter Fehler ist aufgetreten!")
        # Wenn man den Fehler auskommentiert, wird die Datei normal geschrieben und geschlossen.
        # Wenn der Fehler aktiv ist, wird die Datei trotzdem geschlossen!
        print("... kein Fehler aufgetreten im Block.")
except ValueError as ve:
    print(f"Simulierter Fehler abgefangen: {ve}")
except IOError as e:
    print(f"IO-Fehler: {e}")
finally:
    # Überprüfen, ob die Datei geschlossen wurde (auch wenn der Fehler nicht aktiv ist)
    # Dies ist außerhalb des with-Blocks, f_error ist hier nicht mehr gültig
    # Um das zu testen, müsste man den Dateinamen kennen und neu öffnen oder den Status vor dem Fehler prüfen.
    # Wichtig ist: 'with' kümmert sich darum.
    print("Der finally-Block wird immer ausgeführt.")


# Aufräumen
import os
if os.path.exists(dateiname_with):
    os.remove(dateiname_with)
if os.path.exists("fehler_test.txt"):
    os.remove("fehler_test.txt")
print("\nTestdateien ggf. gelöscht.")