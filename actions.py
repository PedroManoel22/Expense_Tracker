def add_expense(description: str, amount: float):
    clean_description = description.strip()

    if not clean_description:
        raise ValueError(
            "A descrição da despesa não pode estar vazia ou conter apenas espaços."
        )

    if amount <= 0:
        raise ValueError("O valor da despesa deve ser maior que zero.")
