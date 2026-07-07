from classes.hospede import Hospede
from classes.hospedagem import Hospedagem


class Avaliacao:
    """
    Avaliação feita por um hóspede.
    """

    def __init__(
        self,
        codigo: int,
        hospede: Hospede,
        hospedagem: Hospedagem,
        nota: int,
        comentario: str
    ):

        self._codigo = codigo
        self._hospede = hospede
        self._hospedagem = hospedagem
        self._nota = nota
        self._comentario = comentario

    @property
    def nota(self):
        return self._nota

    @property
    def comentario(self):
        return self._comentario
    
    @property
    def hospede(self):
        return self._hospede

    @property
    def hospedagem(self):
        return self._hospedagem

    def __str__(self):

        return (
            f"{self.hospede.nome} avaliou "
            f"{self.hospedagem.nome} "
            f"com nota {self.nota}"
        )