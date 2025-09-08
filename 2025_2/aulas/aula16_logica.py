def verificar_ordenado(seq):
    for i in range(len(seq) - 1):
        if seq[i] > seq[i+1]:
            return False
    return True


def unir_lista(seq1, seq2):
    if not verificar_ordenado(seq1) or not verificar_ordenado(seq2):
        raise ValueError("Sequencias nao estao ordenadas")

    seq3 = []

    i = 0
    j = 0
    while i < len(seq1) and j < len(seq2):
        if seq1[i] < seq2[j]:  # i < len(seq1[i])
            seq3.append(seq1[i])
            i += 1
        else:
            seq3.append(seq2[j])
            j += 1

    while i < len(seq1):
        seq3.append(seq1[i])
        i += 1

    while j < len(seq2):
        seq3.append(seq2[j])
        j += 1

    return seq3
