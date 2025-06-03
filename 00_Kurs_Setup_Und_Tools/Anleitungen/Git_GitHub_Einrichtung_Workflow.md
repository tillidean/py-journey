# Git & GitHub: Einrichtung und Workflow für den Kurs  Git🐙

Dieses Dokument beschreibt die Einrichtung von Git und GitHub und gibt einen kurzen Überblick über den grundlegenden Workflow, den wir in diesem Kurs verwenden werden. Es dient als Ergänzung zur ausführlichen `README.md` im Hauptverzeichnis des Kurs-Repositories.

**Ziel:** Versionskontrolle für deinen Code, Zusammenarbeit (bei Gruppenprojekten) und die strukturierte Einreichung deiner Hausaufgaben.

---
## Teil 1: Einrichtung (Einmalig)

### 1. Git Installieren
Git ist ein System zur Versionskontrolle, das Änderungen an Dateien über die Zeit verfolgt.
* **Download:** Lade Git von der offiziellen Webseite herunter: [https://git-scm.com/downloads](https://git-scm.com/downloads)
* **Installation:** Führe den Installer aus. Die Standardeinstellungen sind in den meisten Fällen passend. Wähle während der Installation ggf. "Git Bash Here" als Kontextmenü-Option für Windows, das kann nützlich sein. Es wird empfohlen, den Standard-Editor bei der Installation auf einen dir bekannten Editor umzustellen (z.B. VS Code, Notepad++), falls du mit Vi/Vim nicht vertraut bist.

### 2. Git Konfigurieren
Nach der Installation von Git solltest du deinen Namen und deine E-Mail-Adresse konfigurieren. Diese Informationen werden in jeden Commit eingebettet, den du erstellst. Öffne ein Terminal (Git Bash unter Windows, sonst das normale Terminal).

```bash
git config --global user.name "Dein Vorname Nachname"
git config --global user.email "deine.email@example.com"