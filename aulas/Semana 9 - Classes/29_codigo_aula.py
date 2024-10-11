livro1 = {
    'nome': '1984',
    'autor': 'George Orwell',
    'ano': 1949
}

livro2 = {
    'nome': 'Revolucao dos Animais',
    'autor': 'George Orwell',
    'ano': 1945
}

livros = [livro1, livro2]

def filtro(livros, depois_ano):
    livros_validos = []
    for livro in livros:
        if livro['ano'] >= depois_ano:
            livros_validos.append(livro)
    return livros_validos

print(filtro(livros, 1960))

# Struct
class Book:

    # Construtor
    def __init__(self, a, b, c) -> None:
        self.nome = a
        self.autor = b
        self.ano = c

book1 = Book("1984", "George Orwell", 1949)
print(book1.nome)
# print(book1["nome"])
book2 = Book("Revolucao dos Animais", "George Orwell", 1945)
print(book2.nome)

class ProdutoDataFrame:

    def __init__(self, dict):
        self.df = dict
        self.validar()
    
    def validar(self):
        columns = ['nome', 'ano']
        for column in columns:
            if column not in self.df.keys():
                raise Exception(f"Coluna {column} nao existe!")

d = {"nome": "Matheus", "ano": 1800}
obj = ProdutoDataFrame(d)
print(obj.df)

class Produto:

    def __init__(self, nome, preco, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
    
    def aplicar_desconto(self, perc):
        desconto = 1 - perc / 100
        self.preco = desconto * self.preco
        print(f"O novo valor do produto é R${self.preco}")

p1 = Produto("Iphone", 10000, "celular")
p2 = Produto("1984", 40, "livro")

print(p1.preco)
print(p2.preco)
p1.aplicar_desconto(10)
print(p1.preco)
print(p2.preco)

class Carrinho:

    def __init__(self):
        self.produtos = []
    
    def adicionar(self, produto: Produto):
        self.produtos.append(produto)
    
    def calcular_total(self):
        total = 0
        for p in self.produtos:
            total += p.preco
        print(f"O total do seu carrinho é R${total}")

carrinho_matheus = Carrinho()
carrinho_matheus.calcular_total()
carrinho_matheus.adicionar(p1)
carrinho_matheus.adicionar(p1)
carrinho_matheus.calcular_total()
carrinho_matheus.adicionar(p2)
carrinho_matheus.calcular_total()

