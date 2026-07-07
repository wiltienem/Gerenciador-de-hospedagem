import plotly.express as px


class GraficoLinhas:

    @staticmethod
    def criar(df):

        media = (
            df.groupby("bairro")["preco"]
            .mean()
            .reset_index()
        )

        fig = px.line(

            media,

            x="bairro",

            y="preco",

            markers=True,

            title="Preço Médio por Bairro"

        )

        return fig