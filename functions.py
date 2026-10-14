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


def register_expensive(expense: dict[str, float | str]) -> None:
    expenses: list[dict[str, float | str]] = load_expenses()

    if expense["description"] in [e["description"] for e in expenses]:
        raise ValueError(
            f"\n[yellow]Esta despesa intitulada de '{expense['description']}' já foi adicionada anteriormente.[/yellow]\n"
        )
    else:
        expenses.append(expense)
        with open("expenses.json", "w", encoding="utf-8") as file:
            json.dump(expenses, file, indent=4, ensure_ascii=False)


def validate_description(description: str) -> str:
    clean_description = description.strip()

    if not clean_description:
        raise ValueError(
            "A descrição da despesa não pode estar vazia ou conter apenas espaços."
        )

    return clean_description


def validate_amount(amount: float) -> float:
    if amount <= 0.0:
        raise ValueError("O valor da despesa deve ser maior que zero.")

    return amount


def validate_expense_id(expense_id: int) -> int:
    if expense_id not in [expense["id"] for expense in load_expenses()]:
        raise ValueError(
            f"\n[yellow]Não existe despesa com o ID {expense_id}.[/yellow]\n"
        )

    return expense_id
