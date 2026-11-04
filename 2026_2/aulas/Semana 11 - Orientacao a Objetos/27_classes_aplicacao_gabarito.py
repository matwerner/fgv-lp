from abc import ABC, abstractmethod
from dataclasses import dataclass
import json


def carregar_jogos(caminho):
    with open(caminho, encoding="utf-8") as arquivo:
        return [json.loads(linha) for linha in arquivo]


@dataclass(frozen=True)
class Jogo:
    titulo: str
    preco: float
    lancamento: str
    tags: list
    nota: float
    num_avaliacoes: int


def parse_jogo(dados):
    return Jogo(
        titulo=dados["Title"],
        preco=dados["Original Price"],
        lancamento=dados["Release Date"],
        tags=dados["Popular Tags"],
        nota=dados["All Reviews Score"],
        num_avaliacoes=dados["All Reviews Count"],
    )


# ---------- Filtros ----------

class Filtro(ABC):

    def filtrar(self, jogos):
        return [j for j in jogos if self.criterio(j)]

    @abstractmethod
    def criterio(self, jogo):
        ...


class TagsFiltro(Filtro):
    """Mantém jogos que possuem PELO MENOS UMA das tags."""

    def __init__(self, tags_validas):
        self.tags_validas = tags_validas

    def criterio(self, jogo):
        return any(tag in jogo.tags for tag in self.tags_validas)


class NotaMinimaFiltro(Filtro):

    def __init__(self, nota_minima, avaliacoes_minimas):
        self.nota_minima = nota_minima
        self.avaliacoes_minimas = avaliacoes_minimas

    def criterio(self, jogo):
        return (jogo.nota >= self.nota_minima
                and jogo.num_avaliacoes >= self.avaliacoes_minimas)


class PrecoMaximoFiltro(Filtro):

    def __init__(self, preco_maximo):
        self.preco_maximo = preco_maximo

    def criterio(self, jogo):
        return jogo.preco <= self.preco_maximo


# ---------- Ordenações ----------

class Ordenacao(ABC):

    def __init__(self, decrescente=False):
        self.decrescente = decrescente

    def ordenar(self, jogos):
        return sorted(jogos, key=self.chave, reverse=self.decrescente)

    @abstractmethod
    def chave(self, jogo):
        ...


class NotaOrdenacao(Ordenacao):

    def chave(self, jogo):
        return (jogo.nota, jogo.num_avaliacoes)


class PrecoOrdenacao(Ordenacao):

    def chave(self, jogo):
        return jogo.preco


class LancamentoOrdenacao(Ordenacao):

    def chave(self, jogo):
        return jogo.lancamento


# ---------- Busca e exibição ----------

class Buscador:

    def __init__(self, filtros, ordenacao):
        self.filtros = filtros
        self.ordenacao = ordenacao

    def buscar(self, jogos):
        for filtro in self.filtros:
            jogos = filtro.filtrar(jogos)
        return self.ordenacao.ordenar(jogos)


class Exibidor:

    def __init__(self, limite=10):
        self.limite = limite

    def exibir(self, jogos):
        for posicao, jogo in enumerate(jogos[:self.limite], start=1):
            print(f"#{posicao}: {self.formatar(jogo)}")

    def formatar(self, jogo):
        return (f"{jogo.titulo} | nota {jogo.nota} | "
                f"{jogo.num_avaliacoes} avaliações | R$ {jogo.preco:.2f}")


def main():
    jogos = [parse_jogo(d) for d in carregar_jogos("games.jsonl")]

    buscador = Buscador(
        filtros=[
            TagsFiltro(["RPG"]),
            NotaMinimaFiltro(80, 1000),
            PrecoMaximoFiltro(100),
        ],
        ordenacao=NotaOrdenacao(decrescente=True),
    )

    resultado = buscador.buscar(jogos)
    Exibidor(limite=10).exibir(resultado)


if __name__ == "__main__":
    main()
