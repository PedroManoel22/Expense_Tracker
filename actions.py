import json
from datetime import datetime

from functions import load_expenses


def add_expense(description: str, amount: float):
    clean_description = description.strip()

    if not clean_description:
        raise ValueError(
            "A descrição da despesa não pode estar vazia ou conter apenas espaços."
        )

    if amount <= 0.0:
        raise ValueError("O valor da despesa deve ser maior que zero.")

    expense: dict[str, float | str] = {
        "id": len(load_expenses()) + 1,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "description": clean_description,
        "amount": f"R$ {amount:.2f}",
    }

    expenses: list[dict[str, float | str]] = load_expenses()

    if expense["description"] in [e["description"] for e in expenses]:
        raise ValueError(
            f"\n[yellow]Esta despesa intitulada de '{expense['description']}' já foi adicionada anteriormente.[/yellow]\n"
        )
    else:
        expenses.append(expense)
        with open("expenses.json", "w") as file:
            json.dump(expenses, file, indent=4)


def update_expense(id: int, new_description: str, new_amount: float): ...


def delete_expense(id: int): ...


def list_expenses() -> list[dict[str, float | str]]:
    return load_expenses()
