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
    """Guarda o catálogo de jogos. Filtros e ordenação chegam a cada busca."""

    def __init__(self, jogos):
        self.jogos = jogos

    def buscar(self, filtros, ordenacao):
        resultado = self.jogos
        for filtro in filtros:
            resultado = filtro.filtrar(resultado)
        return ordenacao.ordenar(resultado)


class Exibidor:

    def __init__(self, limite=10):
        self.limite = limite

    def exibir(self, jogos):
        if not jogos:
            print("Nenhum jogo encontrado.")
        for posicao, jogo in enumerate(jogos[:self.limite], start=1):
            print(f"#{posicao}: {self.formatar(jogo)}")

    def formatar(self, jogo):
        return (f"{jogo.titulo} | nota {jogo.nota} | "
                f"{jogo.num_avaliacoes} avaliações | R$ {jogo.preco:.2f}")


# ---------- Linha de comando ----------

def perguntar_filtros():
    filtros = []

    tags = input("Tags (separadas por vírgula, vazio para ignorar): ").strip()
    if tags:
        filtros.append(TagsFiltro([t.strip() for t in tags.split(",")]))

    nota = input("Nota mínima (vazio para ignorar): ").strip()
    if nota:
        avaliacoes = input("Mínimo de avaliações (vazio = 0): ").strip()
        filtros.append(NotaMinimaFiltro(float(nota), int(avaliacoes or 0)))

    preco = input("Preço máximo (vazio para ignorar): ").strip()
    if preco:
        filtros.append(PrecoMaximoFiltro(float(preco)))

    return filtros


def perguntar_ordenacao():
    print("Ordenar por: 1) melhor nota  2) menor preço  3) lançamento mais recente")
    opcao = input("Opção (padrão 1): ").strip() or "1"
    if opcao == "2":
        return PrecoOrdenacao()
    if opcao == "3":
        return LancamentoOrdenacao(decrescente=True)
    return NotaOrdenacao(decrescente=True)


def main():
    jogos = [parse_jogo(d) for d in carregar_jogos("games.jsonl")]
    buscador = Buscador(jogos)
    exibidor = Exibidor(limite=10)

    print(f"{len(jogos)} jogos carregados.")
    while True:
        filtros = perguntar_filtros()
        ordenacao = perguntar_ordenacao()
        exibidor.exibir(buscador.buscar(filtros, ordenacao))

        if input("\nNova busca? (s/n): ").strip().lower() != "s":
            break


if __name__ == "__main__":
    main()
