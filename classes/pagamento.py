from datetime import date

from classes.reserva import Reserva


class Pagamento:
    """
    Representa um pagamento de uma reserva.
    """

    def __init__(
        self,
        codigo: int,
        reserva: Reserva,
        valor: float,
        metodo: str,
        data_pagamento: date
    ):

        self._codigo = codigo
        self._reserva = reserva
        self._valor = valor
        self._metodo = metodo
        self._data_pagamento = data_pagamento

    @property
    def codigo(self):
        return self._codigo

    @property
    def reserva(self):
        return self._reserva

    @property
    def valor(self):
        return self._valor

    @property
    def metodo(self):
        return self._metodo

    @property
    def data_pagamento(self):
        return self._data_pagamento

    def __str__(self):

        return (
            f"Pagamento {self.codigo}\n"
            f"Reserva: {self.reserva.codigo}\n"
            f"Valor: R$ {self.valor:.2f}\n"
            f"Método: {self.metodo}"
        )