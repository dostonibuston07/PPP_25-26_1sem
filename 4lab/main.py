import json
import re
class User:
    def __init__(self, uid, name, email):
        self.uid = uid
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} {self.email}"

    def valid_email(self):
        if "@" not in self.email:
            return False
        domain = self.email.split("@")[-1]
        return "." in domain
class CSVUser(User):
    @staticmethod
    def parse(line):
        _, rest = line.split(" ", 1)
        uid, name, email = rest.split(";")
        return CSVUser(uid, name, email)

class JSONUser(User):
    @staticmethod
    def parse(line):
        _, rest = line.split(" ", 1)
        data = json.loads(rest)
        full_name = data["first_name"] + " " + data["last_name"]
        return JSONUser(data["uid"], full_name, data["contacts"]["email"])

class RAWUser(User):
    @staticmethod
    def parse(line):
        _, rest = line.split(" ", 1)
        parts = rest.split()
        email = parts[-1]
        name = " ".join(parts[:-1])
        return RAWUser(None, name, email)
def parse_user(line):
    if line.startswith("csv"):
        return CSVUser.parse(line)
    if line.startswith("json"):
        return JSONUser.parse(line)
    if line.startswith("raw"):
        return RAWUser.parse(line)
def cmd_emails(users):
    print("Emails:")
    for u in users:
        print(" ", u.email)

def cmd_find(users, substr):
    print(f"Поиск по имени: {substr}")
    result = [u for u in users if substr.lower() in u.name.lower()]
    if not result:
        print("  Ничего не найдено")
    else:
        for u in result:
            print(" ", u)

def cmd_invalid(users):
    print("Невалидные email:")
    bad = [u for u in users if not u.valid_email()]
    if not bad:
        print("  Все email корректны")
    else:
        for u in bad:
            print(" ", u)
if __name__ == "__main__":
    data = [
        "csv 123;Иван Иванов;ivan@example.com",
        'json {"uid": 42, "first_name": "Petr", "last_name": "Petrov", "contacts": {"email": "petr@example.com"}}',
        "raw Иванов Иван ivanovexample.com",   
        "raw Anna Smith anna@site.com"
    ]
    
    users = [parse_user(line) for line in data]

    print("Все пользователи")
    for u in users:
        print(" ", u)

    print("\nКоманда emails")
    cmd_emails(users)

    print("\nКоманда find name=Иван")
    cmd_find(users, "Иван")

    print("\nКоманда invalid")
    cmd_invalid(users)
