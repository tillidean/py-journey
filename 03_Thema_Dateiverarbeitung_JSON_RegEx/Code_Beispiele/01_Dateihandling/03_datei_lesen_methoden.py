# -*- coding: utf-8 -*-
# Beispiel: Verschiedene Methoden zum Lesen von Dateien

# Stelle sicher, dass die Datei 'beispiel_lesedatei.txt' im selben Verzeichnis
# existiert und den Inhalt von oben hat.

dateiname = "beispiel_lesedatei.txt"

print(f"--- Lese '{dateiname}' mit read() ---")
try:
    with open(dateiname, "r", encoding="utf-8") as f:
        gesamter_inhalt = f.read()  # Liest die gesamte Datei als einen String
        print("Gesamter Inhalt:")
        print(gesamter_inhalt)
except FileNotFoundError:
    print(f"Fehler: Datei '{dateiname}' nicht gefunden.")
except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {e}")

print(f"\n--- Lese '{dateiname}' mit readline() ---")
try:
    with open(dateiname, "r", encoding="utf-8") as f:
        print("Lese Zeile für Zeile mit readline():")
        zeile1 = f.readline()  # Liest die erste Zeile (inkl. \n)
        zeile2 = f.readline()  # Liest die zweite Zeile
        print(f"Zeile 1: {zeile1.strip()}")  # .strip() entfernt Whitespace wie \n
        print(f"Zeile 2: {zeile2.strip()}")

        # Man kann readline() in einer Schleife verwenden, bis ein leerer String zurückkommt
        print("\nRestliche Zeilen mit readline() in Schleife:")
        while True:
            zeile = f.readline()
            if not zeile:  # Leerer String bedeutet Dateiende
                break
            print(zeile.strip())
except FileNotFoundError:
    print(f"Fehler: Datei '{dateiname}' nicht gefunden.")
except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {e}")

print(f"\n--- Lese '{dateiname}' mit readlines() ---")
try:
    with open(dateiname, "r", encoding="utf-8") as f:
        alle_zeilen_liste = f.readlines()  # Liest alle Zeilen in eine Liste von Strings
        print("Alle Zeilen als Liste:")
        # Jedes Element in der Liste enthält noch das \n am Ende
        print(alle_zeilen_liste)
        print("\nFormatierte Ausgabe der Liste:")
        for i, zeile in enumerate(alle_zeilen_liste):
            print(f"Listenelement {i}: {zeile.strip()}")
except FileNotFoundError:
    print(f"Fehler: Datei '{dateiname}' nicht gefunden.")
except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {e}")

print(f"\n--- Lese '{dateiname}' durch Iteration über das Dateiobjekt (bevorzugt!) ---")
try:
    with open(dateiname, "r", encoding="utf-8") as f:
        print("Iteriere Zeile für Zeile:")
        for i, zeile in enumerate(f):  # Effizient für große Dateien
            print(f"Zeile {i + 1}: {zeile.strip()}")
except FileNotFoundError:
    print(f"Fehler: Datei '{dateiname}' nicht gefunden.")
except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {e}")