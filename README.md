# 📘 Linux, Cloud Computing & Python

## Arbeiten mit JSON-Dokumenten (NoSQL)

Diese Anleitung dient als kompakter Überblick und Cheat Sheet zum Arbeiten mit JSON-Daten in Python im Kontext von Linux und Cloud Computing.

---

## 🧠 1. Dokumentenmodell (NoSQL) vs. Relationale Datenbanken

### 📄 Dokumentenmodell (NoSQL)

* Daten werden als **Dokumente** gespeichert (z. B. JSON)
* Flexibles Schema (kein festes Tabellenlayout)
* Verschachtelte Strukturen möglich (Objekte in Objekten)

**Beispiel (JSON):**

```json
{
  "name": "Max",
  "age": 30,
  "skills": ["Python", "Linux"]
}
```

### 🗃️ Relationales Modell (SQL)

* Daten in **Tabellen mit festen Spalten**
* Beziehungen über **Fremdschlüssel**
* Strenges Schema

| name | age |
| ---- | --- |
| Max  | 30  |

### ⚖️ Unterschiede im Überblick

| Feature    | NoSQL (Dokumente) | Relational (SQL)   |
| ---------- | ----------------- | ------------------ |
| Schema     | Flexibel          | Fest definiert     |
| Struktur   | Verschachtelt     | Tabellenbasiert    |
| Skalierung | Horizontal        | Vertikal           |
| Abfragen   | Eingeschränkt     | Sehr mächtig (SQL) |

---

## 🐍 2. JSON in Python laden & speichern

### 🔄 Mapping: JSON ↔ Python

| JSON       | Python      |
| ---------- | ----------- |
| Objekt     | dict        |
| Array      | list        |
| String     | str         |
| Zahl       | int / float |
| true/false | True/False  |
| null       | None        |

---

### 📥 JSON laden (`json.load`)

```python
import json

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(data)
```

---

### 📤 JSON speichern (`json.dump`)

```python
import json

data = {
    "name": "Anna",
    "age": 25
}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)
```

✅ `indent=4` sorgt für lesbare Formatierung

---

## 🔧 3. CRUD-Operationen mit JSON-Dateien

### 🟢 CREATE (Erstellen)

```python
data.append({"name": "Lisa", "age": 22})
```

---

### 🔵 READ (Lesen)

```python
for person in data:
    print(person["name"])
```

---

### 🟡 UPDATE (Aktualisieren)

```python
for person in data:
    if person["name"] == "Anna":
        person["age"] = 26
```

---

### 🔴 DELETE (Löschen)

```python
data = [p for p in data if p["name"] != "Lisa"]
```

---

### 🔁 Typischer Workflow

```python
import json

# Datei laden
with open("data.json", "r") as f:
    data = json.load(f)

# Daten ändern
data.append({"name": "Tom", "age": 40})

# Datei speichern
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)
```

---

## ⚠️ 4. Grenzen von JSON-Dateispeicherung

### ❌ Einschränkungen

* 🔍 **Keine komplexen Abfragen** (kein SQL)
* ⚡ **Keine Indizes** → langsam bei großen Datenmengen
* 🔒 **Keine Transaktionen** → keine garantierte Konsistenz
* 👥 **Probleme bei parallelem Zugriff**

  * Mehrere Schreibzugriffe können Daten zerstören
* 📦 **Nicht skalierbar für große Systeme**

---

### ✅ Wann JSON sinnvoll ist

* Kleine Projekte / Skripte
* Konfigurationsdateien
* Daten-Austausch (APIs)
* Prototyping

---

### 🚫 Wann lieber eine Datenbank nutzen

* Viele gleichzeitige Nutzer
* Große Datenmengen
* Komplexe Abfragen notwendig
* Hohe Datenintegrität erforderlich

---

## ☁️ Kontext: Linux & Cloud

* JSON-Dateien werden häufig in Linux-Systemen genutzt (z. B. Configs)
* In Cloud-Umgebungen oft ersetzt durch:

  * NoSQL-Datenbanken (z. B. Dokumentenstores)
  * APIs mit JSON als Austauschformat

---

## 🧾 Cheat Sheet

```python
# Laden
json.load(file)

# Speichern
json.dump(data, file, indent=4)

# JSON ↔ Python
dict <-> object
list <-> array

# Workflow
load → modify → dump
```

---

## 🚀 Fazit

JSON + Python ist ideal für einfache Datenhaltung und Lernen von Datenstrukturen.
Für produktive Systeme solltest du jedoch auf echte Datenbanken umsteigen.

