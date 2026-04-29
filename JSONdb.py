import json
import os
import io
import sys

FILE_NAME = "users.json"


# =========================================================
# DEMO-KERN: CODE + LOGIK + AUSGABE
# =========================================================

def run_demo(title, code, logic, context=None):
    """
    Zeigt:
    1. Code (was wird ausgeführt?)
    2. Logik (was passiert dabei?)
    3. Ausgabe (was kommt raus?)
    """

    print("\n" + "=" * 70)
    print(f"📌 DEMO: {title}")
    print("=" * 70)

    # ---------------------------
    # CODE anzeigen
    # ---------------------------
    print("\n🧾 CODE:")
    print("-" * 70)
    print(code)

    # ---------------------------
    # LOGIK anzeigen
    # ---------------------------
    print("\n🧠 LOGIK:")
    print("-" * 70)
    print(logic)

    # ---------------------------
    # AUSGABE erzeugen
    # ---------------------------
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()

    try:
        exec(code, context if context else {})
        output = sys.stdout.getvalue()
    except Exception as e:
        output = f"Fehler: {e}"

    sys.stdout = old_stdout

    # ---------------------------
    # AUSGABE anzeigen
    # ---------------------------
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

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []


def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


# =========================================================
# CRUD OPERATIONEN
# =========================================================

def create_user():
    data = load_data()

    name = input("Name: ")
    email = input("Email: ")

    new_user = {
        "id": len(data) + 1,
        "name": name,
        "email": email,
        "active": True
    }

    data.append(new_user)
    save_data(data)

    code = f'''new_user = {new_user}
data.append(new_user)
print(new_user)'''

    logic = """1. Neues Dictionary wird erstellt (User)
2. User wird zur Liste hinzugefügt (append)
3. print() gibt den neuen User aus
4. Daten wurden vorher bereits in JSON gespeichert"""

    run_demo("CREATE", code, logic, {"data": data, "new_user": new_user})


def read_users():
    data = load_data()

    code = '''for user in data:
    print(user["id"], user["name"], user["email"])'''

    logic = """1. Schleife geht jeden User in der Liste durch
2. Zugriff auf Dictionary-Werte über Keys ("id", "name", ...)
3. print() gibt pro User eine Zeile aus"""

    run_demo("READ", code, logic, {"data": data})


def update_user():
    data = load_data()

    user_id = int(input("ID ändern: "))

    for user in data:
        if user["id"] == user_id:
            user["name"] = "UPDATED"

    save_data(data)

    code = '''for user in data:
    if user["id"] == user_id:
        user["name"] = "UPDATED"
        print(user)'''

    logic = """1. Schleife durchsucht alle User
2. Bedingung prüft passende ID
3. Wert im Dictionary wird geändert
4. print() zeigt den aktualisierten User"""

    run_demo("UPDATE", code, logic, {"data": data, "user_id": user_id})


def delete_user():
    data = load_data()

    user_id = int(input("ID löschen: "))

    new_data = [user for user in data if user["id"] != user_id]
    save_data(new_data)

    code = '''data = [user for user in data if user["id"] != user_id]
print(data)'''

    logic = """1. List Comprehension erstellt neue Liste
2. Nur User ohne passende ID bleiben erhalten
3. Alte Liste wird ersetzt
4. print() zeigt neue Daten"""

    run_demo("DELETE", code, logic, {"data": new_data, "user_id": user_id})


# =========================================================
# LERNFUNKTIONEN
# =========================================================

def show_mapping():
    data = load_data()

    code = '''print(data)
print(type(data))'''

    logic = """1. JSON wurde bereits in Python geladen
2. print(data) zeigt die Struktur
3. type(data) zeigt: list (JSON Array)
4. Enthalten sind Dictionaries (JSON Objekte)"""

    run_demo("JSON → Python Mapping", code, logic, {"data": data})


def show_limits():
    code = '''print("Keine Indizes")
print("Keine Queries")
print("Keine Transaktionen")
print("Race Conditions möglich")'''

    logic = """1. JSON ist nur eine Datei (kein DB-System)
2. Keine Suchoptimierung (Indizes)
3. Keine parallele Sicherheit
4. Keine komplexen Abfragen möglich"""

    run_demo("Grenzen von JSON", code, logic)


# =========================================================
# MENÜ
# =========================================================

def menu():
    while True:
        print("\n===== JSON DEMO SYSTEM =====")
        print("1) CREATE")
        print("2) READ")
        print("3) UPDATE")
        print("4) DELETE")
        print("5) JSON Mapping")
        print("6) Grenzen")
        print("0) Ende")

        choice = input("Auswahl: ")

        if choice == "1":
            create_user()
        elif choice == "2":
            read_users()
        elif choice == "3":
            update_user()
        elif choice == "4":
            delete_user()
        elif choice == "5":
            show_mapping()
        elif choice == "6":
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