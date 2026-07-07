from abc import ABC, abstractmethod


class GraficoBase(ABC):
    """
    Classe abstrata que servirá de base para todos os gráficos.
    """

    def __init__(self, dataframe):

        self._df = dataframe


    @abstractmethod
    def gerar(self):
        """
        Método obrigatório que cada gráfico deverá implementar.
        """
        pass