# QUESTAO 1
def formatar_msg(num, nota):
    if num == 1:
        print(f"{num} nota de {nota}")
    else:
        print(f"{num} notas de {nota}")

def decomposicao_notas(valor):
    notas = [100, 50, 20, 10, 5, 1]
    nums = []

    atual = valor
    for nota in notas:
        num = atual // nota
        atual -= (num*nota)
        nums.append(num)
    print(nums)

    for i in range(len(notas)):
        num = nums[i]
        nota = notas[i]
        formatar_msg(num, nota)

# QUESTAO 2
def busca_binaria(lista, alvo):
    l = 0
    r = len(lista) - 1
    while l <= r:
        mid = (l+r) // 2
        if lista[mid] > alvo:
            r = mid - 1
        elif lista[mid] < alvo:
            l = mid + 1
        else:
            return mid
    return -1

# QUESTAO 4
def consolidar_vendas(caminho_entrada, caminho_saida):
    # Etapa 1. Ler o arquivo e converter
    # Etapa 2. Sumarizar
    # Etapa 3. Escrever o resultado num arquivo

    # LEITURA
    produtos = []
    arquivo = open(caminho_entrada, mode='r', encoding='utf-8')
    for linha in arquivo:
        categoria, valor = linha.strip().split(',')
        valor = int(valor)
        produtos.append((categoria, valor))
    arquivo.close()

    # SUMARIZACAO
    faturamento_por_categoria = {}
    for categoria, valor in produtos:
        if categoria not in faturamento_por_categoria:
            faturamento_por_categoria[categoria] = 0
        faturamento_por_categoria[categoria] += valor
    print(faturamento_por_categoria)

    # ESCRITA
    arquivo = open(caminho_saida, mode='w', encoding='utf-8')
    for chave, valor in faturamento_por_categoria.items():
        arquivo.write(f"{chave},{valor}\n")

if __name__ == '__main__':
    decomposicao_notas(287)
    print(busca_binaria([1, 3, 5, 7, 9], 9))
    consolidar_vendas("vendas.txt", "consolidado.txt")
