# Uma classe é uma especificação de um tipo, *definindo valores e comportamentos*.
# Atributos são o que o objeto tem!
# Funções nessa parte de orientar objetos, são tituladas como MÉTODOS

class ContaCorrente:
    # Python ao criar objetos, pode executar uma função automaticamente, dentro da nossa classe para definirmos os atributos. Para definir as coisas dentro da função se usa o self
    def __init__(self, numero, titulo, saldo, limite):
        print("Construindo objeto...{}".format(self))
        print("Meu limite {}".format(limite))
        # mandando o self ir para o objeto --> exemplo de atributos
        # o self == que encontra o dados do nosso objeto
        # o "__" no inicio da palavra faz com que ela se torne privada e não possa ser alterada
        self.__numero = numero
        self.__titulo = titulo
        self.__saldo = saldo
        self.__limite = limite 
        self.__codigo_banco = "001"
        
    # exemplo de método abaixo
    def extrato(self):
        print('Saldo {} do titular {}'.format(self.__saldo, self.__titulo))
        
    def deposita(self, valor):
        self.__saldo += valor
    
    # da para também deixar funções anonimas com "__", fazendo com que ela n possa ser chamada
    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel
    
    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))
        
    def transfere(self, valor, destino):
        # o self faz duas coisas, além de acessar um atributo, a partir do self eu posso chamar outro método
        print('Transferência feita, valor transferido: {}'.format(valor))
        self.saca(valor)
        destino.deposita(valor)
        
    @property    
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titulo
    
    @property
    def limite(self):
        return self.__limite
    
    # para mudar o limite
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
    
    # para fazer esse static method n pode ter self, ou seja só retornará um valor definido sempre que for chamado
    @staticmethod
    def codigos_bancos():
        return "001"
    