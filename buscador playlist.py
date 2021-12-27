while True:
    class Musica():
        def __init__(self,titulo, compositor, cantor, ano):
            self.titulo = titulo
            self.compositor = compositor
            self.cantor = cantor
            self.ano = ano
    class Buscador():
        def procurar_playlist(self, playlist, procuracao):
            lista = []
            for instancia in range(len(playlist)):
                # se colocar print(musica), aparecerá: 0, 1 , 2 -> pq são 3 instâncias na lista playlist
                # print(playlist[instancia].ano)
                # posso colocar playlist[instancia]. e qualquer outro valor atribuido a self no construtor
                if playlist[instancia].titulo == procuracao:
                    lista.append(playlist[instancia].cantor)
                    lista.append(playlist[instancia].ano)
                if playlist[instancia].cantor == procuracao or playlist[instancia].compositor == procuracaoC:
                    lista.append(playlist[instancia].titulo)
                if playlist[instancia].ano == procuracao:
                    lista.append(playlist[instancia].titulo)
            if len(lista) > 0:
                print(f"'{procuracao}' tem o seguinte resultado de busca: {lista}")
            else:
                print(f"'{procuracao}' não resultou em nenhuma busca encontrada.")

        def populacionar_playlist(self,digitado):
            playlist = [
                        Musica("Ponta de Areia", "Milton Nascimento", "Milton Nascimento", 1975),
                        Musica("Podres Poderes", "Caetano Veloso", "Caetano Veloso", "1984"),
                        Musica("Baby", "Gal Costa", "Caetano Veloso", "1969"),
                        Musica("Where Is My Mind", "Pixies", "Pixies", "1988"),
                        Musica("Without You", "Mariah Carey", "Mariah Carey", "1993"),
                        Musica("Garota Radical", "Cine", "Banda Cine", "2009"),
                        Musica("As Cores", "Cine", "Banda Cine", "2010"),
                        Musica("Um Lance, Não Um Romance", "Cine", "Banda Cine", "2010"),
                        Musica("Prometa", "Cine", "Banda Cine", "2010"),
                        Musica("Levo Comigo", "Restart", "Restart", "2009"),
                        Musica("Menina Estranha", "Restart", "Restart", "2009"),
                        Musica("Pra Você Lembrar", "Restart", "Restart", "2008"),
                        Musica("Snuff", "Corey Taylor", "Corey Taylor", "2018"),
                        ]
            # chamar a função 'procurar_playlist' determinado elemento
            procurar = self.procurar_playlist(playlist, digitado)
    objeto = Buscador()
    digitado = input('Digite o que deseja procurar: ')
    objeto.populacionar_playlist(digitado)
