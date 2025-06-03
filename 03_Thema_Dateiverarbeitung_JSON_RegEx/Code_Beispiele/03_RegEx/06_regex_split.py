# -*- coding: utf-8 -*-
# Beispiel: re.split() - Teilt einen String anhand eines Musters

import re

text1 = "Apfel,Birne;Kirsche Banane Orange"
print(f"Originaltext 1: '{text1}'")

# Teilen bei Komma, Semikolon oder Leerzeichen
# [,;\s]  -> Zeichenklasse: Komma ODER Semikolon ODER Whitespace-Zeichen
# +        -> Ein oder mehrere Vorkommen des Trennzeichens
trennmuster1 = r"[,;\s]+"
teile1 = re.split(trennmuster1, text1)
print(f"\nGeteilt bei '[{trennmuster1}]': {teile1}")


text2 = "Eintrag1:Wert1##Eintrag2:Wert2====Eintrag3:Wert3"
print(f"\nOriginaltext 2: '{text2}'")

# Teilen bei variablen Trennzeichen (## oder ====)
# (?:##|====) -> Non-capturing Gruppe: Entweder ## ODER ====
#               Non-capturing, damit die Trennzeichen selbst nicht in der Ergebnisliste landen
trennmuster2 = r"(?:##|====)" # Ohne non-capturing: r"(##|====)" würde Trenner mitliefern
teile2 = re.split(trennmuster2, text2)
print(f"Geteilt bei '{trennmuster2}': {teile2}")


text3 = "Kapitel 1: Einleitung. Kapitel 2: Hauptteil. Kapitel 3: Schluss."
print(f"\nOriginaltext 3: '{text3}'")

# Teilen, aber die Trennzeichen (Kapitelüberschriften) behalten
# Hierzu muss die Gruppe, die das Trennzeichen matcht, eine "capturing group" sein (in Klammern)
trennmuster_mit_behalten = r"(\.\s*Kapitel\s*\d+:)" # Punkt, Leerzeichen, "Kapitel", Zahl, Doppelpunkt
teile3 = re.split(trennmuster_mit_behalten, text3)
print(f"\nGeteilt bei '{trennmuster_mit_behalten}' (mit Behalten der Trenner):")
# Das Ergebnis enthält die Trenner als separate Elemente
# Oft muss man die Liste danach noch filtern (leere Strings entfernen etc.)
print(teile3)
# Beispiel für eine gefilterte und neu zusammengesetzte Ansicht:
# ['Kapitel 1: Einleitung', '. Kapitel 2:', ' Hauptteil', '. Kapitel 3:', ' Schluss.'] (ungefähr)
gefilterte_teile3 = [s.strip() for s in teile3 if s and s.strip() != '.'] # Beispielhafte Filterung
print(f"Gefiltert: {gefilterte_teile3}")


# maxsplit-Parameter
text4 = "eins,zwei,drei,vier,fünf"
print(f"\nOriginaltext 4: '{text4}'")
teile4_maxsplit1 = re.split(r",", text4, maxsplit=1)
print(f"Geteilt mit maxsplit=1: {teile4_maxsplit1}") # ['eins', 'zwei,drei,vier,fünf']

teile4_maxsplit2 = re.split(r",", text4, maxsplit=2)
print(f"Geteilt mit maxsplit=2: {teile4_maxsplit2}") # ['eins', 'zwei', 'drei,vier,fünf']