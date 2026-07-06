class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._curtidas = 0

    @property
    def curtidas(self):
        return self._curtidas

    @property
    def nome(self):
        return self._nome
    
    @property
    def curtir(self):
        self._curtidas += 1

class Filmes(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

class Series(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

# Criando os objetos
avatar = Filmes("Avatar", 2009, 177)
avatar.curtir() # Dá 1 curtida

serie1 = Series("Heartbreak High", 2022, 3)
serie1.curtir() # Dá 1 curtida

# Exibindo os resultados
print(f"Filme: {avatar.nome} - Ano: {avatar.ano} - Duração: {avatar.duracao} min - Curtidas: {avatar.curtidas}")
print(f"Série: {serie1.nome} - Ano: {serie1.ano} - Temporadas: {serie1.temporadas} - Curtidas: {serie1.curtidas}")
