ARQUIVO = "transacoes.csv"

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
        arquivo = open(ARQUIVO, "r", encoding="utf-8")
        arquivo.readline()

        for linha in arquivo:
            data, categoria, descricao, valor = linha.strip().split(",")
            print(f"{data} | {categoria} | {descricao} | R$ {float(valor):.2f}")

        arquivo.close()

    elif opcao == "2":
        busca = input("Buscar por descrição: ").lower()

        arquivo = open(ARQUIVO, "r", encoding="utf-8")
        arquivo.readline()

        for linha in arquivo:
            data, categoria, descricao, valor = linha.strip().split(",")

            if busca in descricao.lower():
                print(f"{data} | {categoria} | {descricao} | R$ {float(valor):.2f}")

        arquivo.close()

    elif opcao == "3":
        busca = input("Buscar por categoria: ").lower()

        arquivo = open(ARQUIVO, "r", encoding="utf-8")
        arquivo.readline()

        for linha in arquivo:
            data, categoria, descricao, valor = linha.strip().split(",")

            if busca == categoria.lower():
                print(f"{data} | {categoria} | {descricao} | R$ {float(valor):.2f}")

        arquivo.close()

    elif opcao == "4":
        mes = input("Mês (MM): ")
        ano = input("Ano (AAAA): ")

        receitas = 0.0
        despesas = 0.0

        arquivo = open(ARQUIVO, "r", encoding="utf-8")
        arquivo.readline()

        for linha in arquivo:
            data, categoria, descricao, valor = linha.strip().split(",")
            valor = float(valor)

            if data.startswith(ano + "-" + mes):
                if valor > 0:
                    receitas += valor
                else:
                    despesas += -valor

        arquivo.close()

        saldo = receitas - despesas

        print(f"Receitas: R$ {receitas:.2f}")
        print(f"Despesas: R$ {despesas:.2f}")
        print(f"Saldo: R$ {saldo:.2f}")

    else:
        print("Opção inválida.")
