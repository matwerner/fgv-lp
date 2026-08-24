ARQUIVO = "transacoes.csv"


def carregar_transacoes(caminho: str) -> list[dict]:
    """Carrega as transações do arquivo para uma lista de dicionários."""
    transacoes = []

    with open(caminho, "r", encoding="utf-8") as arquivo:
        arquivo.readline()

        for linha in arquivo:
            data, categoria, descricao, valor = linha.strip().split(",")

            transacao = {
                "data": data,
                "categoria": categoria,
                "descricao": descricao,
                "valor": float(valor),
            }

            transacoes.append(transacao)

    return transacoes


def exibir_transacao(transacao: dict) -> None:
    """Exibe uma transação."""
    print(
        f"{transacao['data']} | "
        f"{transacao['categoria']} | "
        f"{transacao['descricao']} | "
        f"R$ {transacao['valor']:.2f}"
    )


def listar_transacoes(transacoes: list[dict]) -> None:
    """Exibe todas as transações."""
    for transacao in transacoes:
        exibir_transacao(transacao)


def buscar_por_descricao(transacoes: list[dict]) -> None:
    """Solicita uma descrição e exibe as transações correspondentes."""
    busca = input("Buscar por descrição: ").lower()

    for transacao in transacoes:
        if busca in transacao["descricao"].lower():
            exibir_transacao(transacao)


def buscar_por_categoria(transacoes: list[dict]) -> None:
    """Solicita uma categoria e exibe as transações correspondentes."""
    busca = input("Buscar por categoria: ").lower()

    for transacao in transacoes:
        if busca == transacao["categoria"].lower():
            exibir_transacao(transacao)


def exibir_resumo_mensal(transacoes: list[dict]) -> None:
    """Solicita um mês e exibe receitas, despesas e saldo."""
    mes = input("Mês (MM): ")
    ano = input("Ano (AAAA): ")

    receitas = 0.0
    despesas = 0.0

    for transacao in transacoes:
        if transacao["data"].startswith(ano + "-" + mes):
            if transacao["valor"] > 0:
                receitas += transacao["valor"]
            else:
                despesas += -transacao["valor"]

    print(f"Receitas: R$ {receitas:.2f}")
    print(f"Despesas: R$ {despesas:.2f}")
    print(f"Saldo: R$ {receitas - despesas:.2f}")


def mostrar_menu() -> None:
    print("""
0 - Sair
1 - Listar transações
2 - Buscar por descrição
3 - Buscar por categoria
4 - Resumo mensal
""")


def main() -> None:
    transacoes = carregar_transacoes(ARQUIVO)

    while True:
        mostrar_menu()
        opcao = input("Opção: ")

        if opcao == "0":
            break
        elif opcao == "1":
            listar_transacoes(transacoes)
        elif opcao == "2":
            buscar_por_descricao(transacoes)
        elif opcao == "3":
            buscar_por_categoria(transacoes)
        elif opcao == "4":
            exibir_resumo_mensal(transacoes)
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
