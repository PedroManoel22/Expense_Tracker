import argparse

from rich import print

from actions import add_expense, delete_expense, list_expenses, summary, update_expense


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="Expense-Tracker",
        description="Gerenciador de despesas pessoais via linha de comando (CLI).",
    )

    subparses = parser.add_subparsers(
        dest="command", required=True, help="Comandos disponíveis."
    )

    # Comando: add
    add_parser = subparses.add_parser("add", help="Adiciona uma nova despesa.")
    add_parser.add_argument(
        "--description", type=str, help="Descrição da despesa (ex: Almoço)."
    )
    add_parser.add_argument(
        "--amount", type=float, help="Valor da despesa (ex: 12.50)."
    )

    # Comando: update

    update_parser = subparses.add_parser(
        "update", help="Atualiza uma despesa existente pelo id."
    )
    update_parser.add_argument("--id", type=int, help="ID da despesa a ser atualizada.")

    # Comando: delete
    delete_parser = subparses.add_parser(
        "delete", help="Deleta uma despesa existente pelo id."
    )
    delete_parser.add_argument("--id", type=int, help="ID da despesa a ser deletada.")

    # Comando: list
    subparses.add_parser("list", help="Lista todas as despesas registradas no sistema.")

    # Comando: summary
    subparses.add_parser("summary", help="Exibe um resumo das despesas registradas.")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "add":
        try:
            add_expense(args.description, args.amount)
            print("[green]\nDespesa adicionada com sucesso![/green]\n")

        except ValueError as e:
            print(f"\n[red]Erro: {e}[/red]\n")

    elif args.command == "update":
        try:
            update_expense(args.id)
            print("[green]\nDespesa atualizada com sucesso![/green]\n")

        except ValueError as e:
            print(f"\n[red]Erro: {e}[/red]\n")

    elif args.command == "delete":
        try:
            delete_expense(args.id)
        except ValueError as e:
            print(f"\n[red]Erro: {e}[/red]\n")

    elif args.command == "list":
        list_expenses()

    elif args.command == "summary":
        summary()


if __name__ == "__main__":
    main()
