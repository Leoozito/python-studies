class Cliente:
    
    def __init__(self, nome):
        self.__nome = nome
    # .title() deixa a primeira letra da palavra maiúscula
    # o @property se trata de uma propriedade, ou seja, que você indica que essa função pode ser digitada e chamada sem parenteses.
    @property
    def nome(self):
        print("chamando @property nome()")
        return self.__nome.title()
    # da para alterar os atributos através desta propriedade
    @nome.setter
    def nome(self, nome):
        print("chamando setter nome()")
        self.__nome = nome
        