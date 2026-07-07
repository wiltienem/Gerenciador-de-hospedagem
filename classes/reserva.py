from datetime import date

from classes.hospede import Hospede
from classes.hospedagem import Hospedagem


class Reserva:
    """
    Representa uma reserva realizada por um hóspede.
    """

    def __init__(
        self,
        codigo: int,
        hospede: Hospede,
        hospedagem: Hospedagem,
        checkin: date,
        checkout: date,
        valor_total: float,
        status: str = "Confirmada"
    ):

        self._codigo = codigo
        self._hospede = hospede
        self._hospedagem = hospedagem
        self._checkin = checkin
        self._checkout = checkout
        self._valor_total = valor_total
        self._status = status

    @property
    def codigo(self):
        return self._codigo

    @property
    def hospede(self):
        return self._hospede

    @property
    def hospedagem(self):
        return self._hospedagem

    @property
    def checkin(self):
        return self._checkin

    @property
    def checkout(self):
        return self._checkout

    @property
    def valor_total(self):
        return self._valor_total

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, novo_status):
        self._status = novo_status

    def __str__(self):

        return (
            f"Reserva {self.codigo}\n"
            f"Hóspede: {self.hospede.nome}\n"
            f"Hospedagem: {self.hospedagem.nome}\n"
            f"Check-in: {self.checkin}\n"
            f"Check-out: {self.checkout}\n"
            f"Valor: R$ {self.valor_total:.2f}\n"
            f"Status: {self.status}"
        )