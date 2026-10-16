import json
import random
from datetime import datetime

from rich import print

from src.functions import (
    load_expenses,
    register_expensive,
    validate_amount,
    validate_description,
    validate_expense_id,
)

AMOUNT_EXPENSES = 1000


def add_expense(description: str, amount: float):
    """Adiciona uma nova despesa ao sistema.

    Valida a descrição e o valor informados, gera um ID único
    aleatório que não exista previamente, obtém a data atual
    e regista a despesa formatada.
    """

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
    """Atualiza os dados de uma despesa existente.

    Valida o ID fornecido, carrega o histórico de despesas,
    solicita ao usuário uma nova descrição e um novo valor,
    valida as novas entradas e atualiza o registo correspondente.
    """

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
    """Elimina uma despesa existente do sistema.

    Valida o ID fornecido, carrega o histórico de despesas,
    filtra a lista removendo o registo correspondente ao ID válido
    e grava os dados atualizados no ficheiro JSON.
    """

    valid_id = validate_expense_id(id)
    expenses = load_expenses()

    updated_expenses = [expense for expense in expenses if expense["id"] != valid_id]

    with open("expenses.json", "w", encoding="utf-8") as file:
        json.dump(updated_expenses, file, indent=4, ensure_ascii=False)

    print("\n[green]Despesa deletada com sucesso![/green]\n")


def list_expenses():
    """Lista todas as despesas registadas no sistema.

    Carrega o histórico de despesas do ficheiro JSON e exibe-as
    de forma formatada na consola. Se não existirem despesas
    registadas, apresenta uma mensagem de aviso.
    """

    expenses = load_expenses()

    if not expenses:
        print("\n[red]Nenhuma despesa registrada.[/red]\n")
    else:
        print("\n[bold]Despesas registradas:[/bold]\n")
        for expense in expenses:
            print(
                f"ID: {expense['id']}, Data: {expense['date']}, Descrição: {expense['description']}, Valor: {expense['amount']}"
            )
        print()


def summary():
    """Exibe um resumo geral das despesas registadas.

    Carrega o histórico de despesas, calcula o valor total gasto
    convertendo os montantes formatados e apresenta o número total
    de despesas juntamente com a quantia global acumulada.
    """

    expenses = load_expenses()

    if not expenses:
        print("\n[red]Nenhuma despesa registrada.[/red]\n")
    else:
        total_amount = sum(
            float(str(expense["amount"]).replace("R$ ", "").replace(",", "."))
            for expense in expenses
        )
        print("\n[bold]Resumo das despesas:[/bold]")
        print(f"Total de despesas: {len(expenses)}")
        print(f"Valor total gasto: R$ {total_amount:.2f}\n")


def list_for_month(month: int):
    """Lista as despesas registadas para um mês específico.

    Carrega o histórico de despesas, filtra os registos cujo mês
    da data coincida com o mês fornecido e exibe-os formatados
    na consola. Se não existirem despesas para o período,
    apresenta uma mensagem de aviso.
    """

    expenses = load_expenses()

    if not expenses:
        print("\n[red]Nenhuma despesa registrada.[/red]\n")
    else:
        filtered_expenses = [
            expense
            for expense in expenses
            if datetime.strptime(str(expense["date"]), "%Y-%m-%d").month == month
        ]

        if not filtered_expenses:
            print(f"\n[red]Nenhuma despesa registrada para o mês {month}.[/red]\n")
        else:
            print(f"\n[bold]Despesas registradas para o mês {month}:[/bold]\n")
            for expense in filtered_expenses:
                print(
                    f"ID: {expense['id']}, Data: {expense['date']}, Descrição: {expense['description']}, Valor: {expense['amount']}"
                )
            print()
