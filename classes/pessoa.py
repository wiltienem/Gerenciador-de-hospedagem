from abc import ABC


class Pessoa(ABC):
    """
    Classe base para representar uma pessoa.
    """

    def __init__(self, nome: str, cpf: str, email: str):

        self._nome = nome
        self._cpf = cpf
        self._email = email

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @property
    def email(self):
        return self._email

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @email.setter
    def email(self, novo_email):
        self._email = novo_email

    def __str__(self):

        return (
            f"Nome: {self.nome}\n"
            f"CPF: {self.cpf}\n"
            f"E-mail: {self.email}"
        )