from classes.pessoa import Pessoa


class Hospede(Pessoa):
    """
    Representa um hóspede do sistema.
    """

    def __init__(
        self,
        nome,
        cpf,
        email,
        telefone
    ):

        super().__init__(nome, cpf, email)

        self._telefone = telefone

    @property
    def telefone(self):

        return self._telefone

    @telefone.setter
    def telefone(self, telefone):

        self._telefone = telefone

    def __str__(self):

        return (
            super().__str__()
            + f"\nTelefone: {self.telefone}"
        )