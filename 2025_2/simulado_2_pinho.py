from datetime import date


class Livro:

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self)


class Transacao:

    def __init__(self, usuario1, livro1, usuario2, livro2):
        self.usuario1 = usuario1
        self.livro1 = livro1
        self.usuario2 = usuario2
        self.livro2 = livro2
        self.status = "pendente"
        self.data = None

    def concluir(self):
        if self.status != "pendente":
            raise Exception("Transacao ja terminou!")

        self.usuario1.remover_livro(self.livro1)
        self.usuario2.remover_livro(self.livro2)
        self.usuario1.adicionar_livro(self.livro2)
        self.usuario2.adicionar_livro(self.livro1)
        self.status = "concluido"
        self.data = date.today()

    def cancelar(self):
        if self.status != "pendente":
            raise Exception("Transacao ja terminou!")
        self.status = "cancelado"
        self.data = date.today()


class Usuario:

    def __init__(self, nome):
        self.nome = nome
        self.livros = []
        self.avaliacoes = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def remover_livro(self, livro):
        self.livros.remove(livro)

    def solicitar_troca(self, usuario2, livro1, livro2):
        return Transacao(self, livro1, usuario2, livro2)


def simulacao():
    l1 = Livro("1984", "George Orwell")
    l2 = Livro("Biblia", "Jesus")

    u1 = Usuario("Matheus")
    u1.adicionar_livro(l1)

    u2 = Usuario("Luiz")
    u2.adicionar_livro(l2)

    print(u1.livros)
    solicitacao = u1.solicitar_troca(u2, l1, l2)
    solicitacao.concluir()
    print(u1.livros)


if __name__ == "__main__":
    simulacao()
