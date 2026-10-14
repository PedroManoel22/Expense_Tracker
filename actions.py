import json
import random
from datetime import datetime

from rich import print

from functions import (
    load_expenses,
    register_expensive,
    validate_amount,
    validate_description,
    validate_expense_id,
)

AMOUNT_EXPENSES = 1000


def add_expense(description: str, amount: float):
    clean_description = validate_description(description)

    valid_amount = validate_amount(amount)

    current_expenses = load_expenses()

    existing_ids = {expense["id"] for expense in current_expenses}

    while True:
        new_id = random.randint(1, AMOUNT_EXPENSES)
        if new_id not in existing_ids:
            break

    expense: dict[str, float | str] = {
        "id": new_id,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "description": clean_description,
        "amount": f"R$ {valid_amount:.2f}",
    }

    return register_expensive(expense)


def update_expense(id: int):
    valid_id = validate_expense_id(id)

    if valid_id:
        expenses = load_expenses()

        for expense in expenses:
            if expense["id"] == id:
                new_description = input(
                    f"Digite a nova descrição para a despesa '{expense['description']}': "
                ).strip()
                new_amount_str = input(
                    f"Digite o novo valor para a despesa '{expense['description']}' (ex: 12.50): "
                ).strip()

                new_description = validate_description(new_description)

                new_amount = validate_amount(float(new_amount_str))

                expense["description"] = new_description
                expense["amount"] = f"R$ {new_amount:.2f}"


def delete_expense(id: int):
    valid_id = validate_expense_id(id)
    expenses = load_expenses()

    updated_expenses = [expense for expense in expenses if expense["id"] != valid_id]

    with open("expenses.json", "w", encoding="utf-8") as file:
        json.dump(updated_expenses, file, indent=4, ensure_ascii=False)

    print(
        f"\n[green]Despesa '{expenses[valid_id - 1]['description']}' deletada com sucesso![/green]\n"
    )


def list_expenses() -> list[dict[str, float | str]]:
    return load_expenses()
