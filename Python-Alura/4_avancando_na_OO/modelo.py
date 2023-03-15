# class Programa se torna um inicio sobre a parte de herança, para não ter que ficar repetindo código.
# O class Programa é a classe mãe da herança

class Programa:
    def __init__(self, nome, ano,):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0 

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    def dar_like(self):
        self._likes += 1
        
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f"Nome: {self._nome} - Ano: {self.ano} - {self.duracao} min - {self._likes} Likes" 

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        # o super(). é o que chama a classe mãe desejada
        super().__init__(nome, ano)
        self.duracao = duracao
    
    # o "__str__" ele é essencial para DEFINIR o objeto que irá retorna algo TEXTUAL de algum outro objeto das classes
    def __str__(self):
        return f"Nome do Filme: {self._nome} - Ano: {self.ano} - {self.duracao} min - {self._likes} Likes" 
        
class Serie(Programa): 
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
    
    def __str__(self):
        return f"Nome da Serie: {self._nome} - Ano: {self.ano} - {self.temporadas} temporadas - {self._likes} Likes" 
    
class Playlist:
    def __init__(self, nome, programas):    
        self.nome = nome
        self._programas = programas
        
    # o metodo __getitem__ é um metodo que define que é interavel
    def __getitem__(self, item):
        return self._programas[item]
    
    @property
    def listagem(self):
        return self._programas
    
    # built-in de tamanho 
    def __len__(self):
        return len(self._programas)
    
vingadores = Filme("vingadores - guerra infinita", 2018, 160)
# vingadores.dar_like()
tmep = Filme("todo mundo em pânico", 1999, 100)
# tmep.dar_like()
atlanta = Serie("atlanta", 2018, 2)
# atlanta.dar_like()
demolidor = Serie("Demolidor", 2016, 2)
# demolidor.dar_like()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'Tamanho da playlist: {len(playlist_fim_de_semana)}')
# aqui é usado o polimorfismo, ou seja, não importa se é filme ou serie, conseguimos imprimir os dois
for programa in playlist_fim_de_semana:
    print(programa)