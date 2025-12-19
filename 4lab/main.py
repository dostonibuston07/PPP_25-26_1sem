import json
import re

class User:
    def __init__(self, uid, full_name, email):
        self.uid = uid
        self.full_name = full_name
        self.email = email

    def __str__(self):
        return f"{self.full_name} {self.email}"

    def is_email_valid(self):
        return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", self.email) is not None


class CSVUser(User):
    @staticmethod
    def parse(line):
        _, data = line.split(" ", 1)
        uid, name, email = data.split(";")
        return CSVUser(uid, name, email)

class JSONUser(User):
    @staticmethod
    def parse(line):
        _, json_text = line.split(" ", 1)
        obj = json.loads(json_text)
        uid = obj["uid"]
        full_name = obj["first_name"] + " " + obj["last_name"]
        email = obj["contacts"]["email"]
        return JSONUser(uid, full_name, email)

class RAWUser(User):
    @staticmethod
    def parse(line):
        _, data = line.split(" ", 1)
        parts = data.split()
        email = parts[-1]
        full_name = " ".join(parts[:-1])
        uid = None  
        return RAWUser(uid, full_name, email)

def parse_user(line):
    if line.startswith("csv"):
        return CSVUser.parse(line)
    if line.startswith("json"):
        return JSONUser.parse(line)
    if line.startswith("raw"):
        return RAWUser.parse(line)
    return None

def command_emails(users):
    print("Все email:")
    for u in users:
        print(" ", u.email)


def command_find(users, substring):
    print(f'Поиск по имени: "{substring}"')
    found = [u for u in users if substring.lower() in u.full_name.lower()]

    if not found:
        print("  Ничего не найдено")
    else:
        for u in found:
            print(" ", u)


def command_invalid(users):
    print("Пользователи с НЕвалидным email:")
    bad = [u for u in users if not u.is_email_valid()]
    if not bad:
        print("  Все email корректны")
    else:
        for u in bad:
            print(" ", u)

if __name__ == "__main__":
    input_data = [
        "csv 123;Иван Иванов;ivan@example.com",
        'json {"uid": 42, "first_name": "Petr", "last_name": "Petrov", "contacts": {"email": "petr@example.com"}}',
        "raw Иванов Иван ivanovexample.com",        
        "raw Doston Buston dostonbuston@site.com"
    ]

    users = [parse_user(line) for line in input_data]

    print("\n=== Нормализованный вывод пользователей ===")
    for u in users:
        print(" ", u)

    print("\n=== Команда emails ===")
    command_emails(users)

    print("\n=== Команда find name=Иван ===")
    command_find(users, "Иван")

    print("\n=== Команда invalid ===")
    command_invalid(users)
