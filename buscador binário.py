def busca_binaria(lista, buscavel):
''' verifica se o buscado está no meio, ou está inferior ou superior, e vá reduzindo pela metade até que se torne veridico a primeira condição; caso contrário, retorne -1 '''
    primeira_metade = 0
    segunda_metade = len(lista)-1
    while primeira_metade <= segunda_metade:
        meio = (primeira_metade+segunda_metade)//2
        if lista[meio] == buscavel:
            return meio
        else:
            if buscavel < lista[meio]:
                segunda_metade = meio - 1
            else: 
                primeira_metade = meio + 1
    return -1
print(busca_binaria([10,2, 3, 8, -10, 200, 17], 2))

'''
obs: este método se torna muito mais eficiente do que o buscador sexencial, pelo seguinte motivo: ele desconsidera determinada parte considerando a posição na lista. ou seja, ele 
trabalha apenas com verificações que foram reduzidas o campo de visão para determinada espefificação.
o // se torna bastante útil para caso o tamanho das listas forem imparares.
'''
