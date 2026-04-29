import json

def pretty_print_json():
    with open("users.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    
    new_user = {"id": 31, "name": "Stefan", "age": 28, "email": "steff@example.com"}

    data.append(new_user)    
    
    with open("users.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(json.dumps(data, ensure_ascii=False, indent=2))

pretty_print_json()