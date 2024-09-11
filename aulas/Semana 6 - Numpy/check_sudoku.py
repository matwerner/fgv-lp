import numpy as np

def check_range(solution):
    return np.all((solution > 0) & (solution < 10))

def check_sudoku(solution: np.array) -> bool:    
    if not check_range(solution):
        raise RuntimeError("Não é uma solução de Sudoku")

    # Como garantimos que todos os números estão entre 1 e 9
    # Ao verificar uma linha / coluna, devem haver 9 elementos distintos
    def check_row(data):
        return np.unique(data).size == 9

    # Verificar linhas
    n_rows = solution.shape[0]
    for i in range(n_rows):
        row = solution[i]
        if not check_row(row):
            print(f"Linha {i} esta errada")
            return False

    # Verificar colunas
    n_cols = solution.shape[1]
    for j in range(n_cols):
        # Transforma a coluna em array 1D
        column = solution[:, j]
        if not check_row(column):
            print(f"Coluna {j} esta errada")
            return False

    # Verificar blocos
    for i in range(3):
        x_start = 3 * i
        x_end = 3 * (i + 1)
        for j in range(3):            
            y_start = 3 * j
            y_end = 3 * (j + 1)

            block = solution[x_start: x_end, y_start:y_end]
            # print(block) # Veriicar visualmente se pegamos o quadrante certo

            # Transforma a matrix 3d em um array 1d
            block_data = block.flatten()
            if not check_row(block_data):
                print(f"Bloco ({i}, {j}) esta errada")
                return False
    
    return True

valid_solution = np.array([
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
])
print(check_sudoku(valid_solution))

invalid_solution = np.array([
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 1, 9]  # Repetição de 1 na última linha
])
print(check_sudoku(invalid_solution))