import pandas as pd


class LeitorCSV:

    @staticmethod
    def carregar(caminho):

        try:

            return pd.read_csv(caminho)

        except FileNotFoundError:

            print(f"Arquivo não encontrado: {caminho}")

            return pd.DataFrame()

        except Exception as erro:

            print(erro)

            return pd.DataFrame()