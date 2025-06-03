# Git & GitHub: Einrichtung und Workflow für den Kurs 🐙

Dieses Dokument beschreibt die Einrichtung von Git und GitHub und gibt einen grundlegenden Überblick über den Workflow, den wir in diesem Kurs für die Versionskontrolle, Zusammenarbeit und die Einreichung von Hausaufgaben verwenden werden.

**Ziel:**
* Verwendung von Git zur Verfolgung von Code-Änderungen.
* Nutzung von GitHub zum Hosten deines Codes und zur Einreichung von Aufgaben.

**Wichtiger Hinweis:** Dieses Dokument dient als Ergänzung zur ausführlichen **Haupt-`README.md`** im Wurzelverzeichnis des Kurs-Repositories. Die Haupt-`README.md` beschreibt den detaillierten Prozess des **Forkens, Klonens, Synchronisierens mit dem Upstream-Repository und das Erstellen von Pull Requests**. Bitte lies diese zuerst und sehr sorgfältig durch!

---
## Teil 1: Einrichtung (Einmalig auszuführen)

### 1. Git Installieren
Git ist das Versionskontrollsystem, das wir verwenden.
* **Download:** Lade Git von der offiziellen Webseite herunter: [https://git-scm.com/downloads](https://git-scm.com/downloads)
* **Installation:**
    * Führe den heruntergeladenen Installer aus.
    * Die Standardeinstellungen sind in den meisten Fällen in Ordnung.
    * **Windows-Benutzer:** Es wird empfohlen, während der Installation "Git Bash Here" als Kontextmenü-Option auszuwählen. Als Standardeditor für Git-Commit-Nachrichten kannst du einen dir bekannten Editor wählen (z.B. VS Code, Notepad++), falls du mit Vi/Vim (oft Standard) nicht vertraut bist.

### 2. Git Konfigurieren (im Terminal)
Nach der Installation von Git musst du deinen Namen und deine E-Mail-Adresse global für Git konfigurieren. Diese Informationen werden in jeden "Commit" (gespeicherte Änderung) eingebettet.
Öffne ein Terminal (Git Bash unter Windows, sonst das normale Terminal auf macOS/Linux).

```bash
git config --global user.name "Dein Vorname Nachname"
git config --global user.email "deine.email@example.com"
```
*Ersetze die Platzhalter durch deine tatsächlichen Daten. Die E-Mail-Adresse sollte idealerweise die gleiche sein, die du für deinen GitHub-Account verwendest.*

Optional, aber empfohlen, um den Standard-Branch-Namen für neu erstellte Repositories auf `main` zu setzen (falls nicht schon voreingestellt):
```bash
git config --global init.defaultBranch main
```

### 3. GitHub Account Erstellen
GitHub ist die Online-Plattform, auf der wir unsere Git-Repositories hosten und verwalten.
* Erstelle einen kostenlosen Account auf [https://github.com/join](https://github.com/join), falls du noch keinen besitzt.

### 4. (Optional, aber stark empfohlen) SSH-Key für GitHub einrichten
Ein SSH-Key ermöglicht eine sichere, passwortlose Verbindung zwischen deinem Computer und GitHub. Das erspart dir die wiederholte Eingabe deines GitHub-Passworts bei Aktionen wie `git push` oder `git pull`.
* **Anleitungen von GitHub (sehr detailliert und aktuell):**
    1.  [Einen neuen SSH-Schlüssel generieren und zum ssh-agent hinzufügen](https://docs.github.com/de/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
    2.  [Einen neuen SSH-Schlüssel deinem GitHub-Konto hinzufügen](https://docs.github.com/de/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)

    *Folge diesen offiziellen Anleitungen sorgfältig.*

---
## Teil 2: Der grundlegende Git-Workflow im Kurs

Nochmals zur Erinnerung: Der vollständige Prozess (Forken, Klonen, Upstream, Pull Request) steht in der **Haupt-`README.md`**. Hier fokussieren wir uns auf die Kernbefehle, die du täglich nutzen wirst, nachdem dein Setup abgeschlossen ist.

### Wichtige Git-Befehle (Deine täglichen Werkzeuge)

Diese Befehle führst du typischerweise im Terminal **innerhalb des Verzeichnisses deines geklonten Projekts** aus.

* **`git status`**
    * Zeigt dir an, welche Dateien geändert wurden, welche neu sind und welche für den nächsten Commit vorgemerkt (`staged`) sind. *Immer gut, um den Überblick zu behalten!*

* **`git add <dateiname>`** oder **`git add .`**
    * Fügt die angegebene Datei (oder alle geänderten/neuen Dateien im aktuellen Verzeichnis und Unterverzeichnissen mit `.`) zur "Staging Area" hinzu. Das bedeutet, du wählst aus, welche Änderungen im nächsten Commit enthalten sein sollen.

* **`git commit -m "Eine aussagekräftige Commit-Nachricht"`**
    * Speichert die Änderungen aus der Staging Area dauerhaft in der lokalen Historie deines Repositorys. Die Nachricht sollte kurz und prägnant beschreiben, *was* du geändert hast (z.B. "HA01: Additionsfunktion implementiert").

* **Branch-Management:** Für jede Hausaufgabe oder jedes neue Feature solltest du in einem eigenen Branch arbeiten.
    * **`git branch <neuer_branchname>`**: Erstellt einen neuen Branch.
    * **`git checkout <branchname>`**: Wechselt zu einem bereits existierenden Branch.
    * **`git checkout -b <neuer_branchname>`**: Erstellt einen neuen Branch und wechselt direkt dorthin (Kombination der beiden oberen Befehle). *Sehr nützlich für den Start einer neuen Aufgabe!*

* **Synchronisation mit deinem Fork auf GitHub (`origin`):**
    * **`git push origin <branchname>`**: Lädt deine lokalen Commits vom angegebenen Branch zu deinem Fork auf GitHub (genannt `origin`) hoch.
        * Beim allerersten Push eines neuen lokalen Branches zu GitHub: `git push -u origin <branchname>` (Das `-u` setzt den Upstream-Tracking-Branch, sodass du später einfach `git push` verwenden kannst, wenn du auf diesem Branch bist).
    * **`git pull origin <branchname>`**: Holt Änderungen vom angegebenen Branch deines Forks auf GitHub und versucht, sie mit deinem lokalen Branch zusammenzuführen (zu "mergen"). Nützlich, wenn du z.B. auf einem anderen Computer an deinem Fork gearbeitet hast.

* **Synchronisation mit dem Haupt-Kurs-Repository (`upstream`):**
    * (Voraussetzung: `upstream` ist wie in der Haupt-README beschrieben eingerichtet).
    * **`git fetch upstream`**: Holt alle Änderungen (neue Branches, neue Commits) vom Haupt-Kurs-Repository (`upstream`), aktualisiert aber noch nicht deine lokalen Arbeitsdateien.
    * **`git merge upstream/main`**: (Nach `git fetch upstream` und während du auf deinem lokalen `main`-Branch bist: `git checkout main`) Integriert die Änderungen vom `main`-Branch des Haupt-Kurs-Repositorys in deinen lokalen `main`-Branch.
    * Anschließend solltest du deinen lokalen `main`-Branch auch zu deinem Fork pushen: `git push origin main`.

* **`git log`**
    * Zeigt die Commit-Historie an. Mit `q` kannst du die Ansicht wieder verlassen.

### Typischer Arbeitsablauf für eine Hausaufgabe (Lokal, vor dem Pull Request)

1.  **Sicherstellen, dass dein lokaler `main`-Branch aktuell ist (wichtig vor dem Start einer neuen Aufgabe!):**
    ```bash
    git checkout main
    git fetch upstream
    git merge upstream/main
    git push origin main
    ```
2.  **Einen neuen Branch für die aktuelle Aufgabe erstellen:**
    ```bash
    git checkout -b hausaufgabe-0X-deinName
    # z.B. git checkout -b hausaufgabe-01-maxmustermann
    ```
3.  **An der Aufgabe arbeiten:** Code schreiben, Dateien erstellen/bearbeiten.
4.  **Änderungen hinzufügen und committen (mehrmals während der Arbeit):**
    ```bash
    git add . # Oder spezifische Dateien
    git commit -m "HA0X: Teilaufgabe Y erledigt"
    ```
5.  **Änderungen zu deinem Fork auf GitHub pushen:**
    ```bash
    git push origin hausaufgabe-0X-deinName
    # Beim ersten Mal ggf. git push -u origin hausaufgabe-0X-deinName
    ```
6.  Wenn die Aufgabe fertig ist, einen **Pull Request** von deinem `hausaufgabe-0X-deinName`-Branch auf GitHub zum Haupt-Kurs-Repository erstellen (siehe Haupt-`README.md`).

---
## Teil 3: Tipps für erfolgreiches Arbeiten mit Git

* **Häufig committen:** Mache viele kleine, logische Commits. Jeder Commit sollte eine abgeschlossene kleine Änderung darstellen.
* **Aussagekräftige Commit-Nachrichten:** Schreibe klare Nachrichten, die zusammenfassen, was du geändert hast (z.B. "HA01: Implementiere Addition und Subtraktion" statt "Update").
* **Regelmäßig synchronisieren:** Halte deinen lokalen `main`-Branch und deinen Fork auf GitHub aktuell mit dem `upstream` (Original-Kurs-Repository), besonders bevor du einen neuen Aufgaben-Branch erstellst.
* **Arbeite in Branches:** Erstelle für jede Hausaufgabe oder jedes größere Feature einen eigenen Branch. Das Mergen in den `main`-Branch des *Haupt-Repositories* erfolgt dann ausschließlich über Pull Requests.
* **Verstehe, was du tust:** Wenn du dir bei einem Befehl unsicher bist, schaue in der Dokumentation nach oder frage! Mache keine "Git-Magie", ohne die Befehle zu verstehen.

---
## Hilfe und weitere Ressourcen

* **Offizielle Git-Dokumentation:** [https://git-scm.com/doc](https://git-scm.com/doc)
* **GitHub Docs:** [https://docs.github.com/de](https://docs.github.com/de)
* **Interaktives Git Tutorial:** [Learn Git Branching](https://learngitbranching.js.org/?locale=de_DE)
* **Pro Git Buch (kostenlos online):** [https://git-scm.com/book/de/v2](https://git-scm.com/book/de/v2)
* **Fragen im Kurs stellen!**

Viel Erfolg beim Coden und Versionieren! 👍