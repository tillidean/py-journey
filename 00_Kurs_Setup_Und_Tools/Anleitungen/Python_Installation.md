# Python Installation 🐍

Herzlich willkommen! Für diesen Kurs ist eine funktionierende Python-Installation auf deinem Computer unerlässlich. Diese Anleitung führt dich durch die notwendigen Schritte.

---
## 1. Überprüfen einer bestehenden Python-Installation

Möglicherweise ist Python bereits auf deinem System installiert. Öffne ein Terminal (Eingabeaufforderung/PowerShell unter Windows, Terminal unter macOS/Linux) und gib folgende Befehle ein:

* **Windows:**
    ```bash
    python --version
    ```
    oder falls das nicht funktioniert:
    ```bash
    py --version
    ```
* **macOS / Linux:**
    ```bash
    python3 --version
    ```

Wenn eine Version angezeigt wird (z.B. `Python 3.9.x` oder höher), bist du schon gut dabei! Stelle sicher, dass es sich um Python 3.6 oder neuer handelt. Für diesen Kurs empfehlen wir **Python 3.8 oder neuer**.

---
## 2. Python herunterladen

Falls Python nicht installiert ist oder du eine ältere Version hast, lade die aktuelle stabile Version von der offiziellen Webseite herunter:

* **Offizielle Python Webseite:** [https://www.python.org/downloads/](https://www.python.org/downloads/)

Lade den Installer für dein Betriebssystem herunter.

---
## 3. Installationsschritte

### Für Windows:
1.  Starte die heruntergeladene `.exe`-Datei.
2.  **WICHTIG:** Setze im ersten Fenster des Installers unbedingt den Haken bei **"Add Python to PATH"** (oder "Add python.exe to PATH"). Dies erspart dir später viele Probleme.
    ![Windows Python Installer PATH](https://docs.python.org/3/_images/win_installer.png) (_Beispielbild, dein Installer könnte leicht anders aussehen_)
3.  Wähle "Install Now" für die Standardinstallation (empfohlen).
4.  Folge den weiteren Anweisungen. Am Ende kannst du die Pfadlängenbeschränkung deaktivieren ("Disable path length limit"), falls angeboten – das ist meist eine gute Idee.

### Für macOS:
1.  Starte das heruntergeladene `.pkg`-Installationspaket.
2.  Folge den Anweisungen des Installers. Die Standardeinstellungen sind in der Regel passend.
3.  Nach der Installation ist Python normalerweise als `python3` verfügbar.
4.  **Alternative (für fortgeschrittene Benutzer):** Installation via [Homebrew](https://brew.sh/index_de):
    ```bash
    brew install python3
    ```

### Für Linux:
Die meisten Linux-Distributionen haben Python 3 bereits vorinstalliert oder machen die Installation sehr einfach über den Paketmanager.

* **Debian/Ubuntu/Mint:**
    ```bash
    sudo apt update
    sudo apt install python3 python3-pip python3-venv
    ```
* **Fedora:**
    ```bash
    sudo dnf install python3 python3-pip
    ```
* Andere Distributionen haben ähnliche Befehle (z.B. `pacman` für Arch Linux).

---
## 4. Installation überprüfen

Öffne nach der Installation ein **neues** Terminalfenster und überprüfe erneut die Versionen:

* Python:
    * Windows: `python --version` oder `py --version`
    * macOS/Linux: `python3 --version`
* PIP (Python Paketmanager):
    * Windows: `pip --version` oder `py -m pip --version`
    * macOS/Linux: `pip3 --version`

Wenn beide Befehle eine Versionsnummer ausgeben, war die Installation erfolgreich! 🎉

---
## 5. Virtuelle Umgebungen (Sehr empfohlen!)

Es ist eine bewährte Praxis, für jedes Python-Projekt eine eigene **virtuelle Umgebung** (virtual environment) zu erstellen. Das isoliert die Abhängigkeiten (benötigte Pakete) des Projekts.

1.  **Erstellen einer virtuellen Umgebung:**
    Navigiere im Terminal in deinen Projektordner (oder den Ordner, in dem du die Kursaufgaben speichern möchtest) und führe aus:
    * Windows: `python -m venv .venv`
    * macOS/Linux: `python3 -m venv .venv`
    (Der Name `.venv` ist eine gängige Konvention. Du kannst auch andere Namen wählen, z.B. `kurs_env`)

2.  **Aktivieren der virtuellen Umgebung:**
    * **Windows (PowerShell):**
        ```powershell
        .\.venv\Scripts\Activate.ps1
        ```
        (Falls die Ausführung von Skripten blockiert ist, musst du ggf. die Execution Policy anpassen: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`. Bestätige mit `J` oder `A`.)
    * **Windows (CMD / Eingabeaufforderung):**
        ```cmd
        .\.venv\Scripts\activate.bat
        ```
    * **macOS / Linux (bash/zsh):**
        ```bash
        source .venv/bin/activate
        ```
    Nach der Aktivierung siehst du meist den Namen der Umgebung (z.B. `(.venv)`) am Anfang deiner Terminal-Eingabezeile.

3.  **Deaktivieren der virtuellen Umgebung:**
    Gib einfach `deactivate` im Terminal ein.

Innerhalb einer aktivierten Umgebung installierst du Pakete mit `pip install paketname`. Diese sind dann nur in dieser Umgebung verfügbar.

---
## Probleme?

* **"python" wird nicht gefunden / "command not found":**
    * Stelle sicher, dass du beim Windows-Installer "Add Python to PATH" ausgewählt hast.
    * Starte dein Terminal neu, nachdem du die PATH-Variable geändert hast (oder den PC neu starten).
    * Überprüfe die Umgebungsvariablen deines Systems manuell.
* Frage im Kurs nach Hilfe!

Viel Erfolg!