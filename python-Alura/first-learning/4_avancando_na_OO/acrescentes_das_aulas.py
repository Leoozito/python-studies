# Tem um meio diferente de tornar um atributo privado para quem for olhar o código...
# Como fica ruim e meio errado chamar uma classe e usar seu atributo privado desase jeito: "self.nome = _NomeClasse__nomeAtributo",
# O CERTO: é deixar a variavel privada com só 1 underline, para quem for ler o código , veja q vc está com intenção de proteger aquela variavel

# POLIMORFISMO : É quando não importa a classe sendo usada, contanto que esta classe herde de uma superclasse específica.

# só podemos usar um objeto no FOR se: objeto ser iterable.

# temos também o parametro list que é um built-in, ou seja, que ja vem embutido no python3
# temos a função hasattr() que consegue ir em um objeto definido e ajuda a saber se tem um atributo especifico nesse objeto
    # detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas
    
# Tipos de Herança - Interface X Reuso
# Interface = É quando queremos absorver a ideia de polimorfismo,
# Reuso = Se tiver pensando em reutilizar o código e remover duplicação

# Forma de reuso - Composição X Extensão
# Extensão = a forma de herança é chamada de extensão, ou seja , eu pego uma classe em si e faço praticamente uma extensão, só que no caso a herança tem muito acoplamento, ou seja, se você pega praticamente o código inteiro da super classe, suas outras classes dependem dessa super classe, e se é ocorrido mudança na super classe talvez inflija no programa.

# Composição = Ao invés de partir com a régra do "É UM", pode partir da regra do "TEM UM", partindo pela logica, se a classe É UMa coisa, gera duvida primeiro do que é essa coisa para depois entender a classe, ja se a classe TEM UMa coisa, apenas entendendo o que a classe ja é suficiente.

# Mas LEMBRANDO , n é errado fazer herança, apenas tendo em mente que, tem que absorver o polimorfismo ou tendo reuso

# Jeito mais pythonico -> Usando os built-in's do python em metodo que são esses:

# Inicialização = __init__
# Representação = __str__ , __repr__
# Container, sequencia = __contains__ ,  __iter__, __len__, __getitem__
# Númericos= __add__, __sub__, __mul__, __mod__

# O que é instancia: pergunta basica
# É basicamente uma variavel recebendo uma classe, essa variavel se chama instancia.

# Temos o metodo MRO ->

# Ensinado neste modulo (principais que podem ser pesquisados a qualquer momento):
# 01. Definição de métodos assessores
# 02. Generalização/especialização
# 04. Herança de um tipo built-in (nativo)
# 06. Herança múltipla