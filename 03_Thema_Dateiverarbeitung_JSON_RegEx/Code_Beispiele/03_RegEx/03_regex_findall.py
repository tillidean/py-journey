# -*- coding: utf-8 -*-
# Beispiel: re.findall() - Findet ALLE nicht-überlappenden Vorkommen

import re

text = "Der Preis ist 25 Euro, dann 199 Euro und zuletzt 10 Euro."

# Finde alle Zahlen im Text
# \d+  -> eine oder mehrere Ziffern
zahlen_muster = r"\d+"

print(f"Text: '{text}'")
print(f"Zahlen-Muster: '{zahlen_muster}'")

gefundene_zahlen = re.findall(zahlen_muster, text)

print("\n--- Gefundene Zahlen ---")
if gefundene_zahlen:
    print(f"Typ des Ergebnisses: {type(gefundene_zahlen)}")
    print(f"Alle gefundenen Zahlen: {gefundene_zahlen}") # Gibt eine Liste von Strings zurück
    # Um Zahlen zu erhalten:
    zahlen_als_int = [int(z) for z in gefundene_zahlen]
    print(f"Zahlen als Integer: {zahlen_als_int}")
else:
    print("Keine Zahlen gefunden.")


# Beispiel: Finde alle Wörter, die mit 'D' oder 'd' beginnen
text_woerter = "Der schnelle David tanzt. Die Katze döst."
# \b        -> Wortgrenze (um sicherzustellen, dass wir ganze Wörter matchen)
# [Dd]      -> Entweder 'D' oder 'd'
# \w* -> Null oder mehr alphanumerische Zeichen (Buchstaben, Zahlen, Unterstrich)
d_woerter_muster = r"\b[Dd]\w*"

print(f"\nText für Wörter: '{text_woerter}'")
print(f"D-Wörter-Muster: '{d_woerter_muster}'")

d_woerter = re.findall(d_woerter_muster, text_woerter)
print("\n--- Wörter, die mit D/d beginnen ---")
print(d_woerter)


# Was passiert, wenn das Muster Gruppen enthält?
# re.findall() gibt dann eine Liste von Tupeln zurück, wobei jedes Tupel die Gruppen enthält.
text_emails = "Kontakt: max@example.com, erika.m@test.org, support@company.net"
# Muster mit Gruppen für Benutzername und Domain
email_gruppen_muster = r"([\w\.-]+)@([\w\.-]+\.\w+)"
# Gruppe 1: ([\w\.-]+) -> Benutzername
# Gruppe 2: ([\w\.-]+\.\w+) -> Domain

print(f"\nText mit E-Mails: '{text_emails}'")
print(f"E-Mail-Gruppen-Muster: '{email_gruppen_muster}'")

email_teile = re.findall(email_gruppen_muster, text_emails)
print("\n--- Extrahierte E-Mail-Teile (Benutzer, Domain) ---")
if email_teile:
    print(f"Typ des Ergebnisses: {type(email_teile)}")
    print(f"Ergebnis (Liste von Tupeln): {email_teile}")
    for benutzer, domain in email_teile:
        print(f"Benutzer: {benutzer}, Domain: {domain}")
else:
    print("Keine E-Mail-Teile gefunden.")

# Wenn man den gesamten Match UND die Gruppen will, ist finditer oft besser
# oder man macht die Gruppen "non-capturing" (?:...) wenn man nur den Gesamtmatch will
# oder man hat eine äußere Gruppe um den gesamten Ausdruck.
email_gesamt_muster = r"(([\w\.-]+)@([\w\.-]+\.\w+))" # Äußere Gruppe für Gesamtmatch
emails_komplett = re.findall(email_gesamt_muster, text_emails)
print("\n--- Extrahierte E-Mails komplett (mit Gruppen-Side-Effect) ---")
print(emails_komplett) # Zeigt Tupel: (gesamte_email, benutzer, domain)
# Um nur die gesamten E-Mails zu bekommen, ist ein Muster ohne innere Capturing-Gruppen besser
# oder man verwendet eine non-capturing Gruppe: (?:[\w\.-]+)@(?:[\w\.-]+\.\w+)
# oder man iteriert und nimmt das erste Element des Tupels.
nur_emails = [match[0] for match in emails_komplett]
print(f"Nur die E-Mail-Adressen: {nur_emails}")