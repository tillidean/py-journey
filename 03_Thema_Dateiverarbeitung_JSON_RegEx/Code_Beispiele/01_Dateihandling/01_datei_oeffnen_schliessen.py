# -*- coding: utf-8 -*-
# Beispiel: Dateien öffnen und explizit schließen

print("--- Datei im Lesemodus ('r') öffnen ---")
try:
    # Versuche, eine existierende Datei zu öffnen (ersetze 'beispiel_lesedatei.txt' ggf.)
    # Erstelle 'beispiel_lesedatei.txt' manuell für diesen Test oder passe den Pfad an.
    f_read = open("beispiel_lesedatei.txt", "r", encoding="utf-8")
    print("Datei 'beispiel_lesedatei.txt' erfolgreich zum Lesen geöffnet.")
    inhalt = f_read.read()
    print(f"Inhalt:\n{inhalt}")
    f_read.close() # Wichtig: Datei schließen
    print("Datei 'beispiel_lesedatei.txt' geschlossen.")
except FileNotFoundError:
    print("Fehler: 'beispiel_lesedatei.txt' wurde nicht gefunden.")
except Exception as e:
    print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

print("\n--- Datei im Schreibmodus ('w') öffnen ---")
# 'w' erstellt die Datei, wenn sie nicht existiert, oder überschreibt sie, wenn sie existiert.
try:
    f_write = open("neu_geschrieben.txt", "w", encoding="utf-8")
    print("Datei 'neu_geschrieben.txt' erfolgreich zum Schreiben geöffnet/erstellt.")
    f_write.write("Dies ist die erste Zeile.\n")
    f_write.write("Python ist super!\n")
    f_write.close() # Wichtig: Datei schließen, damit der Inhalt sicher geschrieben wird.
    print("Inhalt in 'neu_geschrieben.txt' geschrieben und Datei geschlossen.")
    # Inhalt prüfen:
    f_r = open("neu_geschrieben.txt", "r", encoding="utf-8")
    print(f"Kontroll-Lesen: {f_r.read()}")
    f_r.close()
except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {e}")


print("\n--- Datei im Anhängemodus ('a') öffnen ---")
# 'a' erstellt die Datei, wenn sie nicht existiert, oder fügt am Ende hinzu.
try:
    f_append = open("neu_geschrieben.txt", "a", encoding="utf-8") # Verwendet die oben erstellte Datei
    print("Datei 'neu_geschrieben.txt' erfolgreich zum Anhängen geöffnet.")
    f_append.write("Diese Zeile wurde angehängt.\n")
    f_append.close()
    print("Inhalt an 'neu_geschrieben.txt' angehängt und Datei geschlossen.")
    # Inhalt prüfen:
    f_r = open("neu_geschrieben.txt", "r", encoding="utf-8")
    print(f"Kontroll-Lesen: {f_r.read()}")
    f_r.close()
except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {e}")


print("\n--- Datei im exklusiven Erstellungsmodus ('x') öffnen ---")
# 'x' erstellt die Datei, gibt aber einen Fehler zurück, wenn sie bereits existiert.
try:
    f_exclusive = open("exklusiv_datei.txt", "x", encoding="utf-8")
    print("Datei 'exklusiv_datei.txt' erfolgreich exklusiv erstellt.")
    f_exclusive.write("Inhalt für exklusive Datei.\n")
    f_exclusive.close()
    print("Datei 'exklusiv_datei.txt' geschrieben und geschlossen.")
except FileExistsError:
    print("Fehler: 'exklusiv_datei.txt' existiert bereits. Modus 'x' schlug fehl.")
except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {e}")

# Aufräumen der Testdateien (optional, aber gut für wiederholbare Tests)
import os
if os.path.exists("neu_geschrieben.txt"):
    os.remove("neu_geschrieben.txt")
if os.path.exists("exklusiv_datei.txt"):
    os.remove("exklusiv_datei.txt")
print("\nTestdateien (neu_geschrieben.txt, exklusiv_datei.txt) ggf. gelöscht.")