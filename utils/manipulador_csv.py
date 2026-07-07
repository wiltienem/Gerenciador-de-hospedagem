import pandas as pd


class ManipuladorCSV:

    @staticmethod
    def salvar(df, caminho):
        df.to_csv(caminho, index=False)

    @staticmethod
    def adicionar(df, novo):
        return pd.concat([df, novo], ignore_index=True)

    @staticmethod
    def excluir(df, indice):
        return df.drop(indice).reset_index(drop=True)

    @staticmethod
    def atualizar(df, indice, coluna, valor):
        df.loc[indice, coluna] = valor
        return df