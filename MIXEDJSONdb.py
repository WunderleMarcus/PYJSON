import json
import os
import io
import sys
from pprint import pprint   # für schöne Darstellung verschachtelter Daten

FILE_NAME = "mixed.json"  # deine neue JSON-Datei


# =========================================================
# DEMO-KERN: CODE + LOGIK + AUSGABE
# =========================================================

def run_demo(title, code, logic, context=None):
    print("\n" + "=" * 70)
    print(f"📌 DEMO: {title}")
    print("=" * 70)

    print("\n🧾 CODE:")
    print("-" * 70)
    print(code)

    print("\n🧠 LOGIK:")
    print("-" * 70)
    print(logic)

    old_stdout = sys.stdout
    sys.stdout = io.StringIO()

    try:
        exec(code, context if context else {})
        output = sys.stdout.getvalue()
    except Exception as e:
        output = f"Fehler: {e}"

    sys.stdout = old_stdout

    print("\n💻 AUSGABE:")
    print("-" * 70)
    print(output if output else "(keine Ausgabe)")

    print("=" * 70 + "\n")


# =========================================================
# JSON FUNKTIONEN
# =========================================================

def load_data():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


# =========================================================
# GENERISCHE HILFSFUNKTIONEN
# =========================================================

def get_display_name(doc):
    """
    Versucht einen sinnvollen Anzeigenamen zu finden,
    da jedes Dokument andere Felder hat
    """
    for key in ["name", "username", "company", "product", "event", "title", "sensor_id", "user"]:
        if key in doc:
            return doc[key]
    return "Unbekannt"


# =========================================================
# CRUD OPERATIONEN (angepasst auf flexible Struktur)
# =========================================================

def read_documents():
    data = load_data()

    code = '''for doc in data:
    print(doc["id"], doc)'''

    logic = """1. Jedes Dokument wird durchlaufen
2. Dokumente können unterschiedliche Strukturen haben
3. Gesamtes Dokument wird ausgegeben (kein fixes Schema!)"""

    run_demo("READ (Alle Dokumente)", code, logic, {"data": data})


def show_pretty():
    data = load_data()

    code = '''from pprint import pprint
for doc in data:
    pprint(doc)
    print("-" * 40)'''

    logic = """1. pprint formatiert verschachtelte Daten
2. Besonders wichtig bei:
   - Listen in Listen
   - Dictionaries in Dictionaries"""

    run_demo("Struktur anzeigen (verschachtelt)", code, logic, {"data": data, "pprint": pprint})


def update_document():
    data = load_data()
    doc_id = int(input("ID ändern: "))

    for doc in data:
        if doc["id"] == doc_id:
            # Beispiel: wir fügen ein Feld hinzu
            doc["updated"] = True

    save_data(data)

    code = '''for doc in data:
    if doc["id"] == doc_id:
        doc["updated"] = True
        print(doc)'''

    logic = """1. Dokument wird anhand ID gefunden
2. Neue Eigenschaft wird hinzugefügt
3. JSON erlaubt flexible Erweiterung (kein Schema!)"""

    run_demo("UPDATE (flexibles Feld hinzufügen)", code, logic, {"data": data, "doc_id": doc_id})


def delete_document():
    data = load_data()
    doc_id = int(input("ID löschen: "))

    new_data = [doc for doc in data if doc["id"] != doc_id]
    save_data(new_data)

    code = '''data = [doc for doc in data if doc["id"] != doc_id]
print(data)'''

    logic = """1. Neue Liste wird erstellt
2. Dokument mit ID wird entfernt
3. Kein direkter 'DELETE' wie in SQL → Liste wird ersetzt"""

    run_demo("DELETE", code, logic, {"data": new_data, "doc_id": doc_id})


# =========================================================
# SPEZIELLE LERNFUNKTIONEN (für dein JSON!)
# =========================================================

def explore_nested():
    data = load_data()

    code = '''for doc in data:
    if "address" in doc:
        print(doc["address"]["city"])
    
    if "devices" in doc:
        for d in doc["devices"]:
            print(d["type"], d["os"])'''

    logic = """1. Zugriff auf verschachtelte Objekte:
   doc["address"]["city"]

2. Zugriff auf Listen von Objekten:
   for d in doc["devices"]

3. Wichtig:
   Nicht jedes Dokument hat diese Felder → vorher prüfen!"""

    run_demo("Verschachtelte Daten lesen", code, logic, {"data": data})


def show_mapping():
    data = load_data()

    code = '''print(type(data))
print(type(data[0]))
print(data[0])'''

    logic = """1. JSON Array → Python list
2. JSON Objekt → Python dict
3. Unterschiedliche Strukturen pro Eintrag möglich"""

    run_demo("JSON → Python Mapping", code, logic, {"data": data})


def show_limits():
    code = '''print("Keine festen Strukturen")
print("Keine Queries wie SQL")
print("Keine Indizes")
print("Probleme bei parallelem Schreiben")'''

    logic = """1. JSON ist flexibel aber unstrukturiert
2. Suche ist ineffizient
3. Keine Datenbank-Funktionen vorhanden"""

    run_demo("Grenzen von JSON", code, logic)


# =========================================================
# MENÜ
# =========================================================

def menu():
    while True:
        print("\n===== JSON DOKUMENT DEMO =====")
        print("1) Alle Dokumente anzeigen")
        print("2) Struktur schön anzeigen")
        print("3) Dokument ändern (flexibel)")
        print("4) Dokument löschen")
        print("5) Verschachtelte Daten lesen")
        print("6) JSON Mapping")
        print("7) Grenzen")
        print("0) Ende")

        choice = input("Auswahl: ")

        if choice == "1":
            read_documents()
        elif choice == "2":
            show_pretty()
        elif choice == "3":
            update_document()
        elif choice == "4":
            delete_document()
        elif choice == "5":
            explore_nested()
        elif choice == "6":
            show_mapping()
        elif choice == "7":
            show_limits()
        elif choice == "0":
            break
        else:
            print("Ungültig!")


# =========================================================
# START
# =========================================================

if __name__ == "__main__":
    menu()