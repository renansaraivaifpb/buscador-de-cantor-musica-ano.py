def buscaBinaria_recursiva(lista, elemento, primeira_metade = 0, segunda_metade = None):
''' basicamente retrata a mesma ideia da função busca binária; no entanto, o adicionamento da base e chamada recursiva deixa o algoritmo mais sofisticado, chmando ela própria
para a resoluação de um conjunto de problemas n menores dentro de un conjunto maior x '''

    if segunda_metade is None:
        segunda_metade = len(lista)-1
    if segunda_metade < primeira_metade:
        return -1 # busca não encontrada dentro de um conjunto (lista) ordenado.
    else:
        # execute isso até o momento que as duas verificações abaixo seja falsa e retorne meio.
        meio = (primeira_metade + segunda_metade)//2
    if elemento < lista[meio]:
        return buscaBinaria_recursiva(lista, elemento, primeira_metade,meio-1)
        # caso o elemento esteja na primeira metade, então chamar a função contendo os parâmetros
        # obs: o parametro meio-1, serve para atribuir um valor para segunda metade de tal forma que seja o antecessor do meio
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
    (a, 100, 9),
    (a, 0, -1),
    (a, 75, -1),
    (a, -10, -1)
])
def testar_buscaBinaria_recursiva(entrada, elemento, saida):
    assert buscaBinaria_recursiva(entrada, elemento) == saida
    
'''
obs: módulo pytest para testar o script de forma mais automatizada.
'''
