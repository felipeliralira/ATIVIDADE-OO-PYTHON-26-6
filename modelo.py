#Filmes e séries tem as seguintes características:

#Filme: Nome, ano, duração
#Séries: Nome, ano, temporadas

class Filmes:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__curtir = 0

    @property
    def valor_curtir(self):
        return self.__curtir
    
    @property
    def nome(self):
        return self.__nome

    def curtida(self):
        self.curtir += 1

class Series:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__curtir = 0
    
    @property
    def valor_curtir(self):
        return self.__curtir
    
    @property
    def nome(self):
        return self.__nome
    
    def curtida(self):
        self.curtir += 1

avatar = Filmes("Avatar", 2009, 177)
print(f"Filme: {avatar.nome} - Ano: {avatar.ano} - Duração: {avatar.duracao} - Curtidas: {avatar.curtida}")

serie1 = Series("Hearbreak High", 2022, 3)
serie1.curtida()
print(f"Nome: {serie1.nome} - Ano: {serie1.ano} - temporadas: {serie1.temporadas} - Curtidas: {serie1.curtida}")



