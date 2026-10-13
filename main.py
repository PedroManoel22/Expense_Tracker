import argparse

from rich import print

from actions import add_expense


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


if __name__ == "__main__":
    main()
