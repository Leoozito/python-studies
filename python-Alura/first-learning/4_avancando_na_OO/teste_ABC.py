from abc import ABC # abstract base classes -> classes abstratas que são as bases do que será implementado ou seja: antes de nós mesmo criarmos uma classe que dependa de outra, podemos ver se ja n existe no python uma BASE para essas classes dependentes.
from collections.abc import MutableSequence # -> contém diversas classes prontas para serem herdadas.
from numbers import Complex

class Playlist(MutableSequence):
    pass