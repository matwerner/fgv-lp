ARQUIVO = "transacoes.csv"


def normalizar_texto(texto: str) -> str:
    """Remove espaços extras e padroniza o texto para comparação."""
    return texto.strip().lower()


def carregar_transacoes(caminho: str) -> list[dict]:
    """Carrega as transações do arquivo para uma representação interna."""
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


def buscar_por_descricao(
    transacoes: list[dict],
    descricao: str
) -> list[dict]:
    """Retorna as transações cuja descrição contém o termo informado."""
    resultado = []
    descricao = normalizar_texto(descricao)

    for transacao in transacoes:
        descricao_transacao = normalizar_texto(transacao["descricao"])

        if descricao in descricao_transacao:
            resultado.append(transacao)

    return resultado


def buscar_por_categoria(
    transacoes: list[dict],
    categoria: str
) -> list[dict]:
    """Retorna as transações pertencentes à categoria informada."""
    resultado = []
    categoria = normalizar_texto(categoria)

    for transacao in transacoes:
        categoria_transacao = normalizar_texto(transacao["categoria"])

        if categoria == categoria_transacao:
            resultado.append(transacao)

    return resultado


def calcular_resumo_mensal(
    transacoes: list[dict],
    ano: str,
    mes: str
) -> dict[str, float]:
    """Calcula receitas, despesas e saldo de um mês."""
    receitas = 0.0
    despesas = 0.0
    periodo = ano + "-" + mes

    for transacao in transacoes:
        if transacao["data"].startswith(periodo):
            valor = transacao["valor"]

            if valor > 0:
                receitas += valor
            else:
                despesas += -valor

    return {
        "receitas": receitas,
        "despesas": despesas,
        "saldo": receitas - despesas,
    }


def exibir_transacao(transacao: dict) -> None:
    """Exibe uma transação."""
    print(
        f"{transacao['data']} | "
        f"{transacao['categoria']} | "
        f"{transacao['descricao']} | "
        f"R$ {transacao['valor']:.2f}"
    )


def exibir_transacoes(transacoes: list[dict]) -> None:
    """Exibe uma coleção de transações."""
    for transacao in transacoes:
        exibir_transacao(transacao)


def exibir_resumo(resumo: dict[str, float]) -> None:
    """Exibe um resumo financeiro."""
    print(f"Receitas: R$ {resumo['receitas']:.2f}")
    print(f"Despesas: R$ {resumo['despesas']:.2f}")
    print(f"Saldo: R$ {resumo['saldo']:.2f}")


def mostrar_menu() -> None:
    """Exibe as opções disponíveis."""
    print("""
0 - Sair
1 - Listar transações
2 - Buscar por descrição
3 - Buscar por categoria
4 - Resumo mensal
""")


def ler_opcao() -> str:
    """Solicita uma opção válida do menu."""
    while True:
        opcao = input("Opção: ")

        if opcao in ("0", "1", "2", "3", "4"):
            return opcao

        print("Opção inválida.")


def main() -> None:
    transacoes = carregar_transacoes(ARQUIVO)

    while True:
        mostrar_menu()
        opcao = ler_opcao()

        if opcao == "0":
            break

        elif opcao == "1":
            exibir_transacoes(transacoes)

        elif opcao == "2":
            descricao = input("Buscar por descrição: ")
            resultado = buscar_por_descricao(transacoes, descricao)
            exibir_transacoes(resultado)

        elif opcao == "3":
            categoria = input("Buscar por categoria: ")
            resultado = buscar_por_categoria(transacoes, categoria)
            exibir_transacoes(resultado)

        elif opcao == "4":
            mes = input("Mês (MM): ")
            ano = input("Ano (AAAA): ")

            resumo = calcular_resumo_mensal(
                transacoes,
                ano,
                mes
            )

            exibir_resumo(resumo)


if __name__ == "__main__":
    main()
