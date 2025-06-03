# Willkommen zum Programmierkurs-Repository! 👋

Hallo zusammen und herzlich willkommen zum offiziellen Code- und Aufgaben-Repository für unseren Programmierkurs bei **ABS IT**!

Dieses Repository dient als zentrale Anlaufstelle für alle Codebeispiele, Übungsaufgaben und Hausaufgaben, die wir im Laufe des Kurses behandeln werden. Ziel ist es, euch eine strukturierte Umgebung zu bieten, in der ihr nicht nur auf Materialien zugreifen, sondern auch aktiv mitarbeiten und eure Lösungen einreichen könnt.

## Inhaltsverzeichnis

* [Voraussetzungen](#voraussetzungen)
* [Workflow: So nutzt du dieses Repository](#workflow-so-nutzt-du-dieses-repository)
    * [1. Repository Forken (Deine persönliche Kopie erstellen)](#1-repository-forken-deine-persönliche-kopie-erstellen)
    * [2. Deinen Fork Klonen (Code auf deinen Computer herunterladen)](#2-deinen-fork-klonen-code-auf-deinen-computer-herunterladen)
    * [3. Upstream Remote hinzufügen (Verbindung zum Original-Repository)](#3-upstream-remote-hinzufügen-verbindung-zum-original-repository)
    * [4. Deinen Fork aktuell halten](#4-deinen-fork-aktuell-halten)
* [Arbeiten an Aufgaben](#arbeiten-an-aufgaben)
    * [Einen neuen Branch für jede Aufgabe erstellen](#einen-neuen-branch-für-jede-aufgabe-erstellen)
    * [Änderungen committen und pushen](#änderungen-committen-und-pushen)
* [Hausaufgaben einreichen (Pull Request erstellen)](#hausaufgaben-einreichen-pull-request-erstellen)
* [Wichtige Hinweise](#wichtige-hinweise)
* [Fragen?](#fragen)

---

## Voraussetzungen

Bevor du startest, stelle bitte sicher, dass du Folgendes eingerichtet hast:

1.  **Git:** Du musst Git auf deinem Computer installiert haben. Falls nicht, lade es von [git-scm.com](https://git-scm.com/) herunter und installiere es.
2.  **GitHub-Account:** Du benötigst einen kostenlosen GitHub-Account. Registriere dich auf [github.com](https://github.com), falls du noch keinen hast.

---

## Workflow: So nutzt du dieses Repository

Um effektiv mit diesem Repository arbeiten zu können und deine Hausaufgaben einzureichen, folge bitte diesen Schritten:

### 1. Repository Forken (Deine persönliche Kopie erstellen)

Ein "Fork" ist deine persönliche Kopie dieses Haupt-Repositories auf deinem eigenen GitHub-Account. Hier kannst du Änderungen vornehmen, ohne das Original direkt zu beeinflussen.

* **So geht's:**
    1.  Navigiere zur Hauptseite dieses Repositorys auf GitHub: `[Link zu deinem Haupt-Repository hier einfügen]`
    2.  Klicke oben rechts auf den **"Fork"**-Button.
        ![GitHub Fork Button](https://docs.github.com/assets/cb-20363/images/help/repository/fork-button.png)
    3.  Wähle deinen GitHub-Account als Ziel für den Fork aus. GitHub erstellt nun eine Kopie des Repositorys unter deinem Account (z.B. `dein-username/kurs-repository`).

### 2. Deinen Fork Klonen (Code auf deinen Computer herunterladen)

Nachdem du das Repository geforkt hast, musst du eine lokale Kopie deines Forks auf deinen Computer herunterladen (klonen), um mit den Dateien arbeiten zu können.

* **So geht's:**
    1.  Navigiere zu deinem Fork auf GitHub (z.B. `https://github.com/dein-username/kurs-repository`).
    2.  Klicke auf den grünen **"< > Code"**-Button.
    3.  Kopiere die URL unter "HTTPS" (sie sollte etwa so aussehen: `https://github.com/dein-username/kurs-repository.git`).
        ![GitHub Clone URL](https://docs.github.com/assets/cb-30830/images/help/repository/code-button.png)
    4.  Öffne ein Terminal oder eine Git-Bash auf deinem Computer.
    5.  Navigiere zu dem Verzeichnis, in dem du das Projekt speichern möchtest (z.B. `cd Documents/ABS_IT_Kurs`).
    6.  Führe den folgenden Befehl aus (ersetze die URL mit deiner kopierten URL):
        ```bash
        git clone [https://github.com/dein-username/kurs-repository.git](https://github.com/dein-username/kurs-repository.git)
        ```
    7.  Wechsle in das neu erstellte Verzeichnis:
        ```bash
        cd kurs-repository
        ```

### 3. Upstream Remote hinzufügen (Verbindung zum Original-Repository)

Damit du deinen Fork mit Änderungen aus dem ursprünglichen (unserem Haupt-) Repository aktualisieren kannst, musst du eine Verbindung ("Remote") zum Original-Repository einrichten. Dies wird üblicherweise "upstream" genannt.

* **So geht's (im Terminal, im Verzeichnis deines geklonten Forks):**
    1.  Führe diesen Befehl aus, um das Original-Repository als "upstream" hinzuzufügen (ersetze den Link falls nötig):
        ```bash
        git remote add upstream [Link zu deinem Haupt-Repository hier einfügen, z.B. [https://github.com/ABS-IT-Dozent/kurs-repository.git](https://github.com/ABS-IT-Dozent/kurs-repository.git)]
        ```
    2.  Überprüfe, ob es geklappt hat:
        ```bash
        git remote -v
        ```
        Du solltest jetzt Einträge für `origin` (deinen Fork) und `upstream` (das Haupt-Repository) sehen.

### 4. Deinen Fork aktuell halten

Bevor du mit einer neuen Aufgabe beginnst oder deine Arbeit einreichst, solltest du sicherstellen, dass dein Fork (und deine lokale Kopie) die neuesten Änderungen aus dem Haupt-Repository (`upstream`) enthält.

* **So geht's (im Terminal, im `main`- oder `master`-Branch deines lokalen Repositorys):**
    1.  Stelle sicher, dass du im Hauptbranch bist (meist `main` oder `master`):
        ```bash
        git checkout main
        ```
    2.  Hole die neuesten Änderungen vom `upstream`-Repository:
        ```bash
        git fetch upstream
        ```
    3.  Merge die Änderungen vom `upstream/main` in deinen lokalen `main`-Branch:
        ```bash
        git merge upstream/main
        ```
    4.  (Optional, aber empfohlen) Pushe diese Updates auch zu deinem Fork auf GitHub (`origin`):
        ```bash
        git push origin main
        ```

---

## Arbeiten an Aufgaben

Für jede Aufgabe oder Hausaufgabe solltest du einen separaten Branch erstellen. Das hält deine Arbeit sauber und isoliert.

### Einen neuen Branch für jede Aufgabe erstellen

* **So geht's (im Terminal):**
    1.  Stelle sicher, dass dein `main`-Branch aktuell ist (siehe [Deinen Fork aktuell halten](#4-deinen-fork-aktuell-halten)).
    2.  Erstelle einen neuen Branch und wechsle direkt dorthin. Wähle einen aussagekräftigen Namen für den Branch (z.B. `hausaufgabe-01` oder `feature-user-login`):
        ```bash
        git checkout -b name-des-neuen-branches 
        # z.B. git checkout -b hausaufgabe-01-maxmustermann
        ```

### Änderungen committen und pushen

Während du an der Aufgabe arbeitest:

1.  **Änderungen hinzufügen (Staging):**
    ```bash
    git add . 
    # Fügt alle geänderten Dateien hinzu, oder spezifiziere Dateien: git add dateiname.py
    ```
2.  **Änderungen committen (Snapshot erstellen):**
    Schreibe eine aussagekräftige Commit-Nachricht!
    ```bash
    git commit -m "Kurze Beschreibung deiner Änderungen, z.B. Hausaufgabe 01: Funktion X implementiert"
    ```
3.  **Änderungen zu deinem Fork auf GitHub pushen:**
    Wenn du den Branch zum ersten Mal pushst, musst du ihn mit `origin` (deinem Fork) verbinden:
    ```bash
    git push -u origin name-des-neuen-branches
    ```
    Für spätere Pushes auf demselben Branch genügt:
    ```bash
    git push
    ```

---

## Hausaufgaben einreichen (Pull Request erstellen)

Sobald du mit einer Aufgabe fertig bist und deine Änderungen auf deinem Branch zu deinem Fork auf GitHub gepusht hast, kannst du einen **Pull Request (PR)** erstellen. Dies ist die Aufforderung, deine Änderungen in das Haupt-Repository zu übernehmen (und für mich die Möglichkeit, deine Arbeit zu sehen und Feedback zu geben).

* **So geht's:**
    1.  Gehe zu deinem Fork auf GitHub (z.B. `https://github.com/dein-username/kurs-repository`).
    2.  Wenn du kürzlich Änderungen zu einem Branch gepusht hast, zeigt GitHub oft einen gelben Hinweis mit einem Button **"Compare & pull request"**. Klicke darauf.
        ![Compare & pull request button](https://docs.github.com/assets/cb-119532/images/help/pull_requests/compare-and-pull-request-button.png)
    3.  Alternativ kannst du zum Tab **"Pull requests"** gehen und auf **"New pull request"** klicken.
    4.  **WICHTIG:** Stelle sicher, dass die Basis für den Pull Request korrekt ist:
        * **`base repository`**: Das Haupt-Repository (z.B. `ABS-IT-Dozent/kurs-repository`) und der `main` Branch (oder ein spezifischer Aufgabenbranch, falls von mir vorgegeben).
        * **`head repository`**: Dein Fork (z.B. `dein-username/kurs-repository`) und der Branch, auf dem deine Lösungen sind (z.B. `hausaufgabe-01-maxmustermann`).
        ![Pull Request base and head](https://docs.github.com/assets/cb-78334/images/help/pull_requests/pr-options.png)
    5.  Gib deinem Pull Request einen klaren Titel (z.B. "Hausaufgabe 01 - Max Mustermann") und eine kurze Beschreibung deiner Lösung oder eventueller Probleme.
    6.  Klicke auf **"Create pull request"**.

Ich werde dann benachrichtigt, kann deinen Code reviewen und dir Feedback geben oder ihn mergen.

---

## Wichtige Hinweise

* **Commit-Nachrichten:** Schreibt aussagekräftige Commit-Nachrichten. Ein guter Stil ist z.B. "HA01: Implementiere Funktion X" oder "Fix: Fehler bei Eingabevalidierung".
* **Ein Branch pro Aufgabe:** Verwendet für jede Hausaufgabe einen neuen, sauberen Branch.
* **Regelmäßig Pullen/Fetchen:** Haltet euren `main`-Branch aktuell mit dem `upstream`-Repository, bevor ihr neue Aufgaben-Branches erstellt.
* **Keine direkten Pushes zum `main`-Branch eures Forks, wenn es um Aufgaben geht:** Arbeitet immer in Feature-Branches und mergt diese dann (oder lasst sie per PR mergen).
* **Deadlines:** Beachtet die Abgabefristen für die Hausaufgaben!

---

## Fragen? ❓

Wenn ihr Fragen zum Workflow, zu Git, GitHub oder den Aufgaben habt:

* Stellt sie gerne im Kurs.
* [Optional: Link zu einem Forum, Chat-Kanal oder E-Mail-Adresse für Fragen hier einfügen]

Viel Erfolg und Spaß beim Programmieren!