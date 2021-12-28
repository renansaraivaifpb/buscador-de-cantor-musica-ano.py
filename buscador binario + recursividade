def buscaBinaria_recursiva(lista, elemento, primeira_metade = 0, segunda_metade = None):
''' basicamente retrata a mesma ideia da função busca binária; no entanto, o adicionamento da base e chamada recursiva deixa o algoritmo mais sofisticado, chmando ela própria
para a resoluação de um conjunto de problemas n menores dentro de un conjunto maior x '''

    if segunda_metade is None:
        segunda_metade = len(lista)-1
    if segunda_metade < primeira_metade:
        return -1
    else:
        meio = (primeira_metade + segunda_metade)//2
    if elemento < lista[meio]:
        return buscaBinaria_recursiva(lista, elemento, primeira_metade,meio-1)
    if elemento > lista[meio]:
        return buscaBinaria_recursiva(lista, elemento, meio+1, segunda_metade)
    else:
        return meio

a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
import pytest
@pytest.mark.parametrize('entrada, elemento, saida', [
    (a, 10, 0),
    (a, 20, 1), 
    (a, 30, 2),
    (a, 40, 3),
    (a, 50, 4),
    (a, 60, 5),
    (a, 70, 6),
    (a, 80, 7),
    (a, 90, 8),
    (a, 100, 9)
])
def testar_buscaBinaria_recursiva(entrada, elemento, saida):
    assert buscaBinaria_recursiva(entrada, elemento) == saida
    
'''
obs: módulo pytest para testar o script de forma mais automatizada.
'''
