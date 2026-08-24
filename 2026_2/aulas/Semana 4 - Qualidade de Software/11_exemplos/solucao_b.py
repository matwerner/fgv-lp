ARQUIVO = "transacoes.csv"


def listar_transacoes(arquivo: str) -> None:
    with open(arquivo, "r", encoding="utf-8") as f:
        f.readline()

        for linha in f:
            data, categoria, descricao, valor = linha.strip().split(",")
            print(f"{data} | {categoria} | {descricao} | R$ {float(valor):.2f}")


def buscar_por_descricao(arquivo: str) -> None:
    busca = input("Buscar por descrição: ").lower()

    with open(arquivo, "r", encoding="utf-8") as f:
        f.readline()

        for linha in f:
            data, categoria, descricao, valor = linha.strip().split(",")

            if busca in descricao.lower():
                print(f"{data} | {categoria} | {descricao} | R$ {float(valor):.2f}")


def buscar_por_categoria(arquivo: str) -> None:
    busca = input("Buscar por categoria: ").lower()

    with open(arquivo, "r", encoding="utf-8") as f:
        f.readline()

        for linha in f:
            data, categoria, descricao, valor = linha.strip().split(",")

            if busca == categoria.lower():
                print(f"{data} | {categoria} | {descricao} | R$ {float(valor):.2f}")


def resumo_mensal(arquivo: str) -> None:
    mes = input("Mês (MM): ")
    ano = input("Ano (AAAA): ")

    receitas = 0.0
    despesas = 0.0

    with open(arquivo, "r", encoding="utf-8") as f:
        f.readline()

        for linha in f:
            data, categoria, descricao, valor = linha.strip().split(",")
            valor = float(valor)

            if data.startswith(ano + "-" + mes):
                if valor > 0:
                    receitas += valor
                else:
                    despesas += -valor

    print(f"Receitas: R$ {receitas:.2f}")
    print(f"Despesas: R$ {despesas:.2f}")
    print(f"Saldo: R$ {receitas - despesas:.2f}")


while True:
    print("""
0 - Sair
1 - Listar transações
2 - Buscar por descrição
3 - Buscar por categoria
4 - Resumo mensal
""")

    opcao = input("Opção: ")

    if opcao == "0":
        break
    elif opcao == "1":
        listar_transacoes(ARQUIVO)
    elif opcao == "2":
        buscar_por_descricao(ARQUIVO)
    elif opcao == "3":
        buscar_por_categoria(ARQUIVO)
    elif opcao == "4":
        resumo_mensal(ARQUIVO)
    else:
        print("Opção inválida.")
