import json


def load_expenses() -> list[dict[str, float | str]]:
    """Carrega a lista de despesas do arquivo JSON.

    Retorna uma lista de dicionários com os dados salvos.
    Caso o arquivo não exista ou esteja vazio, retorna uma lista vazia.

    """
    JSON_FILE_PATH = "expenses.json"
    expenses: list[dict[str, float | str]] = []

    try:
        with open(JSON_FILE_PATH, "r") as file:
            content = file.read().strip()
            if not content:
                expenses = []
            else:
                expenses = json.loads(content)
    except FileNotFoundError:
        expenses = []

    return expenses


def register_expensive(expense: dict[str, float | str]) -> None:
    """Regista uma nova despesa no sistema.

    Verifica se já existe uma despesa com a mesma descrição.
    Caso exista, lança um erro; caso contrário, adiciona à lista
    e atualiza o arquivo JSON.
    """

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
    """Valida a descrição da despesa.

    Remove espaços em branco nas pontas e lança um erro caso
    a string esteja vazia. Retorna a descrição limpa.
    """

    clean_description = description.strip()

    if not clean_description:
        raise ValueError(
            "A descrição da despesa não pode estar vazia ou conter apenas espaços."
        )

    return clean_description


def validate_amount(amount: float) -> float:
    """Valida o valor da despesa.

    Garante que o valor seja estritamente maior que zero.
    Caso contrário, lança um erro. Retorna o valor validado.
    """

    if amount <= 0.0:
        raise ValueError("O valor da despesa deve ser maior que zero.")

    return amount


def validate_expense_id(expense_id: int) -> int:
    """Valida se uma despesa com o ID especificado existe.

    Verifica no arquivo de base de dados se o ID informado está cadastrado.
    Caso não exista, lança um erro; caso contrário, retorna o ID validado.
    """

    if expense_id not in [expense["id"] for expense in load_expenses()]:
        raise ValueError(
            f"\n[yellow]Não existe despesa com o ID {expense_id}.[/yellow]\n"
        )

    return expense_id
