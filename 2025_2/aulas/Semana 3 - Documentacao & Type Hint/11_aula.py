# Exemplo de um comentário

# Entrada: "Hello World! 127!"
# Saida: "hello world"

# Type Hint

# Basicos: int, float, str, bool
# Complexos: dict, tuple, set, list
from typing import Dict, Any, Optional, List


def normalizar(texto: str) -> str:
    """
    Normaliza o texto colocando em caixa baixa e removendo tudo o que nao é letra;

    Parameters
    ----------
        texto: str
            Texto a ser normalizado

    Returns
    -------
        str:
            Texto normalizado

    Examples:
    >>> teste = "HELLO World! 127"
    >>> normalizar(teste)
    'hello world'
    """
    texto = texto.lower()
    novo_texto = ""
    for c in texto:
        if c.isalpha() or c.isspace():
            novo_texto += c
    novo_texto = novo_texto.strip()  # " abc 127 cde " -> "abc  cde"

    palavras = novo_texto.split()
    novo_texto = " ".join(palavras)
    return novo_texto


def calcula_alunos(
    alunos: Optional[Dict[int, List[float]]]
) -> Optional[Dict[int, float]]:
    """
    Assadasdasd
    """
    if alunos is None:
        return None

    media_alunos = {}
    for matricula, notas in alunos.items():
        media = sum(notas) / len(notas)
        media_alunos[matricula] = media
    return media_alunos


def test():
    if True:
        return 1
    return 0


if __name__ == "__main__":
    teste = "123"
    print(normalizar(teste))

    import doctest
    doctest.testmod()

    alunos = {
        123: [7.7, 8.5],
        456: [5.5, 6.8]
    }

    d = calcula_alunos(alunos)
    print(d)
