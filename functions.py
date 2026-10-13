import json


def load_expenses() -> list[dict[str, float | str]]:
    json_file_path = "expenses.json"
    expenses: list[dict[str, float | str]] = []

    try:
        with open(json_file_path, "r") as file:
            content = file.read().strip()
            if not content:
                expenses = []
            else:
                expenses = json.loads(content)
    except FileNotFoundError:
        expenses = []

    return expenses
