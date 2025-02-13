#Fisher-Yates

import random

def fisher_yates_shuffle(arr):
    n = len(arr)
    for i in range(n-1, 0, -1):
        j = random.randint(0, i)  # Escolhe um índice aleatório entre 0 e i
        arr[i], arr[j] = arr[j], arr[i]  # Troca os elementos
    return arr

# Exemplo de uso
lista = [1, 2, 3, 4, 5]
embaralhada = fisher_yates_shuffle(lista)
print(embaralhada)
