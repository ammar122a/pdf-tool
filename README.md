# PDF Tool

Ein Python-Projekt zum Zusammenführen mehrerer PDF-Dateien.
Das Projekt wird schrittweise um weitere Funktionen erweitert.

## Aktuelle Funktionen

- Mehrere PDFs in der richtigen Reihenfolge zusammenführen.
- Eingabedateien auf Existenz prüfen.
- Verhindern, dass eine vorhandene Ausgabedatei überschrieben wird.

## Installation

Voraussetzung: Python ist installiert.

Im Terminal des Projektordners eine virtuelle Umgebung erstellen
und die Abhängigkeiten installieren:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Verwendung

1. Im Projektordner einen Unterordner `samples` erstellen.
2. Zwei PDF-Dateien als `dokument1.pdf` und `dokument2.pdf` darin ablegen.
3. Das Programm starten:

   ```powershell
   .\.venv\Scripts\python.exe main.py
   ```

Das Ergebnis wird als `merged.pdf` im Projektordner gespeichert.
Eingabedateien und Ausgabepfad lassen sich aktuell in `main.py` anpassen.

Eine bereits vorhandene Ausgabedatei muss vor einem erneuten
Durchlauf umbenannt oder entfernt werden.

## Geplante Erweiterungen

- Grafische Benutzeroberfläche.
- Dateien hinzufügen, entfernen und ihre Reihenfolge ändern.
- Export als TXT, DOCX, JPG und PNG.
- Bildexport als Einzelbilder oder ein zusammenhängendes Bild.
- PDF-Komprimierung.
- Bilder zuschneiden, frei oder mit Formatvorlagen.

## Projektziel

Praktische Erfahrung mit Python, Dateiverarbeitung, Fehlerbehandlung,
automatisierten Tests und Git sammeln.