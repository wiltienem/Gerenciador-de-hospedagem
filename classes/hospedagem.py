class Hospedagem:
    """
    Representa uma hospedagem disponível.
    """

    def __init__(
        self,
        codigo,
        nome,
        bairro,
        preco,
        tipo,
        avaliacao
    ):

        self._codigo = codigo
        self._nome = nome
        self._bairro = bairro
        self._preco = preco
        self._tipo = tipo
        self._avaliacao = avaliacao

    @property
    def codigo(self):
        return self._codigo

    @property
    def nome(self):
        return self._nome

    @property
    def bairro(self):
        return self._bairro

    @property
    def preco(self):
        return self._preco

    @property
    def tipo(self):
        return self._tipo

    @property
    def avaliacao(self):
        return self._avaliacao

    def __str__(self):

        return (
            f"{self.nome} - "
            f"{self.bairro} - "
            f"R$ {self.preco:.2f}"
        )