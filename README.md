# Expense Tracker CLI 💰

Uma aplicação de linha de comando (CLI) robusta, performática e modular para gestão e acompanhamento de despesas pessoais, desenvolvida em Python. Este projeto foi concebido seguindo as especificações do desafio [Expense Tracker](https://roadmap.sh/projects/expense-tracker) do Roadmap.sh, aplicando princípios de arquitetura limpa, tipagem estática e persistência de dados.

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📌 Sobre o Projeto

O **Expense Tracker CLI** permite que o utilizador monitorize os seus gastos financeiros diretamente a partir do terminal, com suporte para adicionar, atualizar, remover, listar e filtrar despesas por mês, além de gerar resumos financeiros automáticos.

Projetado com foco em **Separation of Concerns (SoC)**, o código foi estruturado em camadas claras: interface de utilizador e parsing de argumentos (`main.py`), lógica de negócio e ações de fluxo (`actions.py`), e funções utilitárias de validação e persistência I/O (`functions.py`).

### 🎯 Diferenciais Técnicos para Recrutadores

- **Validação Defensiva de Dados:** Tratamento rigoroso de entradas de utilizador (como garantias de montantes positivos `amount > 0`, remoção de espaços em branco e prevenção de IDs duplicados).
- **Tipagem Estática Avançada:** Uso ostensivo de _Type Hints_ (incluindo _Union Types_ `float | str`) para auditoria estática com Pylance/Mypy.
- **Tratamento Elegante de Exceções:** Sistema centralizado de exceções (`ValueError`) com feedback amigável ao utilizador através da biblioteca **Rich**.
- **Persistência em JSON com Encoding UTF-8:** Manipulação segura de ficheiros JSON sem risco de corrupção de carateres acentuados ou concorrência na escrita.

---

## 🛠️ Tecnologias e Conceitos Aplicados

- **Python 3.10+**: Construção com sintaxe moderna e tipagem explícita.
- **Rich**: Formatação avançada de saídas na consola com cores e estilos (erros em vermelho, sucessos em verde, destaques em negrito).
- **Argparse**: Parser nativo de argumentos da linha de comando com suporte completo a subcomandos e _flags_.
- **Arquitetura Modular**:
  - `main.py`: Entrypoint e parsing da CLI.
  - `actions.py`: Orquestração e casos de uso da aplicação.
  - `functions.py`: Camada de infraestrutura (I/O) e validações puras.

---

## 🚀 Funcionalidades e Comandos

| Comando               | Sintaxe                                     | Descrição                                                               |
| :-------------------- | :------------------------------------------ | :---------------------------------------------------------------------- |
| **Adicionar**         | `add --description <DESC> --amount <VALOR>` | Cadastra uma nova despesa com ID gerado aleatoriamente e data atual.    |
| **Listar Tudo**       | `list`                                      | Exibe o histórico completo de despesas registadas.                      |
| **Listar por Mês**    | `summary --month <MÊS>`                     | Filtra e exibe apenas as despesas ocorridas no mês especificado (1-12). |
| **Resumo Financeiro** | `summary`                                   | Calcula e exibe a quantidade de despesas e o valor total acumulado.     |
| **Atualizar**         | `update --id <ID>`                          | Permite editar interativamente a descrição e o valor de uma despesa.    |
| **Eliminar**          | `delete --id <ID>`                          | Remove permanentemente uma despesa da base de dados pelo ID.            |

---

## 💻 Como Executar e Utilizar

### 0. Clonar o Repositório e Instalar Dependências

```bash
git clone [https://github.com/PedroManoel22/Expense_Tracker.git](https://github.com/PedroManoel22/Expense_Tracker.git)
cd Expense_Tracker

# Instalar dependência visual (Rich)
pip install rich
```

### 1. Consultando a Ajuda (--help)

```bash
python3 main.py --help
```

### 2. Adicionando Despesas (add)

```bash
python3 main.py add --description "Almoço de Negócios" --amount 45.90
python3 main.py add --description "Assinatura da Internet" --amount 120.00
```

### 3. Atualizando uma Despesa (update)

```bash
python3 main.py update --id 342
```

### 4. Deletando uma Despesa (delete)

```bash
python3 main.py delete --id 342
```

### 5. Listando Todas as Despesas (list)

```bash
python3 main.py list
```

### 6. Resumo Geral de Gastos (summary)

```bash
python3 main.py summary
```

### 7. Filtragem Despesas por Mẽs (summary --month)

```bash
python3 main.py summary --month 10
```
