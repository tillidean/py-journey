# Coding Styleguide für Python 🐍

Ein konsistenter Programmierstil ist entscheidend für die Lesbarkeit, Wartbarkeit und Zusammenarbeit bei Softwareprojekten – auch bei kleineren Übungen und Hausaufgaben. Dieser Styleguide gibt grundlegende Empfehlungen für das Schreiben von Python-Code in diesem Kurs und verweist auf offizielle Standards.

Das Hauptziel ist es, Code zu schreiben, der nicht nur funktioniert, sondern auch für andere (und dich selbst in der Zukunft!) leicht verständlich ist.

---
## PEP 8 – Der offizielle Style Guide für Python Code

Der wichtigste Style Guide für Python ist **PEP 8**. PEP steht für "Python Enhancement Proposal". PEP 8 ist eine Sammlung von Richtlinien und Best Practices für das Schreiben von lesbarem Python-Code.

* **Offizielle PEP 8 Dokumentation:** [https://peps.python.org/pep-0008/](https://peps.python.org/pep-0008/)

**Es wird dringend empfohlen, sich mit PEP 8 vertraut zu machen und dessen Richtlinien zu befolgen.** Die meisten Punkte in diesem Dokument sind Zusammenfassungen oder Hervorhebungen aus PEP 8.

---
## Kernaspekte von PEP 8 (und unsere Empfehlungen)

### 1. Einrückung (Indentation)
* Verwende **4 Leerzeichen** pro Einrückungsebene.
* Verwende keine Tabs für die Einrückung. Konfiguriere deinen Editor so, dass er Tabs automatisch in 4 Leerzeichen umwandelt.

### 2. Zeilenlänge (Line Length)
* Begrenze alle Zeilen auf eine maximale Länge von **79 Zeichen**.
* Für Codezeilen, bei denen dies schwer einzuhalten ist, sind bis zu 88 oder 99 Zeichen manchmal akzeptabel (besonders bei modernen Bildschirmen), aber PEP 8 empfiehlt 79 Zeichen für besseren Umgang mit mehreren offenen Fenstern und Code-Review-Tools.

### 3. Leerzeilen (Blank Lines)
* Verwende Leerzeilen, um Code logisch zu gliedern.
* **Zwei Leerzeilen** vor und nach Top-Level Funktions- und Klassendefinitionen.
* **Eine Leerzeile** vor und nach Methodendefinitionen innerhalb einer Klasse.
* Innerhalb von Funktionen können Leerzeilen sparsam eingesetzt werden, um logische Abschnitte zu trennen.

### 4. Importe (Imports)
* Importe sollten immer am Anfang der Datei stehen, nach eventuellen Modul-Docstrings und Kommentaren, aber vor globalen Variablen und Konstanten.
* Reihenfolge der Importe:
    1.  Standardbibliotheks-Importe (z.B. `import os`, `import sys`)
    2.  Verwandte Drittanbieter-Importe (z.B. `import requests`, `import numpy`)
    3.  Lokale Anwendungs-/Bibliotheks-spezifische Importe.
* Vermeide Wildcard-Importe (`from modul import *`), da sie den Namensraum unübersichtlich machen.
* Schreibe jeden Import auf eine eigene Zeile:
    ```python
    # Gut:
    import os
    import sys

    # Schlecht:
    import os, sys
    ```

### 5. Leerraum in Ausdrücken und Anweisungen (Whitespace)
* Verwende Leerzeichen um Operatoren: `x = 1`, `y = x + 2`, `a += b`.
* Nach Kommas, Semikolons oder Doppelpunkten (aber nicht davor): `my_list = [1, 2, 3]`, `def meine_funktion(arg1, arg2):`.
* Keine Leerzeichen direkt innerhalb von Klammern, eckigen Klammern oder geschweiften Klammern: `spam(ham[1], {eggs: 2})`.
* Keine Leerzeichen am Ende einer Zeile (trailing whitespace).

### 6. Namenskonventionen (Naming Conventions)
* **Variablen:** `kleinbuchstaben_mit_unterstrichen` (snake_case). Beispiel: `anzahl_studenten`, `benutzer_name`.
* **Funktionen:** `kleinbuchstaben_mit_unterstrichen` (snake_case). Beispiel: `berechne_summe()`, `drucke_bericht()`.
* **Konstanten:** `GROSSBUCHSTABEN_MIT_UNTERSTRICHEN` (SCREAMING_SNAKE_CASE). Beispiel: `MAX_CONNECTIONS`, `PI`.
* **Klassen:** `CapWords` oder `PascalCase` (erster Buchstabe jedes Wortes groß). Beispiel: `MeineKlasse`, `DatenbankVerbindung`.
* **Module:** Kurze, `kleingeschriebene_namen`. Unterstriche können verwendet werden, wenn es die Lesbarkeit verbessert.
* **Methoden:** Wie Funktionen (`kleinbuchstaben_mit_unterstrichen`).
* **Interne Verwendung:** Ein führender Unterstrich (`_variablenname`) signalisiert, dass eine Variable oder Methode für den internen Gebrauch gedacht ist.
* **Wähle immer aussagekräftige Namen!** Vermeide einbuchstabige Namen außer für sehr kurze Schleifenvariablen (z.B. `i`, `j`, `k`) oder mathematische Kontexte.

### 7. Kommentare (Comments)
* Schreibe Kommentare, um Code zu erklären, der nicht offensichtlich ist. Guter Code ist oft selbsterklärend, aber Kommentare können helfen, das "Warum" hinter einer bestimmten Implementierung zu verdeutlichen.
* **Block-Kommentare:** Beginnen mit `# ` und erklären den folgenden Codeblock.
* **Inline-Kommentare:** Sparsam verwenden, stehen in derselben Zeile wie der Code und beginnen mit `# `. Halte mindestens zwei Leerzeichen Abstand zum Code. `x = x + 1  # Inkrementiere x`
* **Docstrings (Dokumentations-Strings):**
    * Sehr wichtig! Schreibe Docstrings für alle öffentlichen Module, Funktionen, Klassen und Methoden.
    * Verwende dreifache Anführungszeichen: `"""Einzeiliger Docstring."""` oder für mehrzeilige:
        ```python
        def meine_funktion(parameter1, parameter2):
            """
            Fasst zusammen, was die Funktion tut.

            Args:
                parameter1 (typ): Beschreibung von Parameter 1.
                parameter2 (typ): Beschreibung von Parameter 2.

            Returns:
                typ: Beschreibung des Rückgabewertes.
            """
            # Code hier
            pass
        ```

---
## Werkzeuge zur Unterstützung des Styleguides

Es gibt Werkzeuge, die dir helfen können, deinen Code konsistent zu halten und PEP 8-Verletzungen zu finden oder automatisch zu beheben:

* **Linters (Überprüfen den Code):**
    * **Flake8:** Ein beliebter Linter, der PEP 8, PyFlakes (Fehlererkennung) und McCabe (Komplexitätsprüfung) kombiniert.
        * Installation: `pip install flake8`
        * Ausführung: `flake8 dein_code.py`
    * **Pylint:** Ein weiterer mächtiger Linter mit mehr Konfigurationsmöglichkeiten.
* **Formatters (Formatieren den Code automatisch):**
    * **Black:** Ein "uncompromising" Code-Formatter, der den Code automatisch nach sehr strikten (aber PEP 8-nahen) Regeln formatiert. Nimmt dir viele Entscheidungen ab und sorgt für hohe Konsistenz.
        * Installation: `pip install black`
        * Ausführung: `black dein_code.py`
    * **autopep8:** Formatiert Code automatisch, um ihn PEP 8-konform zu machen.
        * Installation: `pip install autopep8`
        * Ausführung: `autopep8 --in-place dein_code.py`

**Empfehlung:** Gewöhne dir an, einen Linter (z.B. Flake8) und einen Formatter (z.B. Black) zu verwenden. Viele Code-Editoren (wie VS Code) bieten Integrationen für diese Tools.

---
## Allgemeine Gute Programmierpraktiken

* **DRY (Don't Repeat Yourself):** Vermeide Code-Duplizierung. Fasse wiederholenden Code in Funktionen oder Klassen zusammen.
* **KISS (Keep It Simple, Stupid):** Bevorzuge einfache und klare Lösungen gegenüber komplexen.
* **Lesbarkeit zählt (Readability Counts):** Schreibe Code für Menschen, nicht nur für den Computer. Dein zukünftiges Ich (und andere) werden es dir danken.
* **Früh und oft testen:** Stelle sicher, dass dein Code wie erwartet funktioniert.

---
## Kursspezifische Regeln

*Eventuelle kursspezifische Ergänzungen oder Abweichungen von diesem Styleguide werden hier oder im Unterricht vom Dozenten bekannt gegeben.*

---

Halte dich an diese Richtlinien, um sauberen, lesbaren und wartbaren Python-Code zu schreiben. Es ist eine Fähigkeit, die im Laufe der Zeit entwickelt wird!