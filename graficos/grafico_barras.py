import plotly.express as px


class GraficoBarras:

    @staticmethod
    def criar(df):

        bairros = (
            df.groupby("bairro")
            .size()
            .reset_index(name="Quantidade")
        )

        fig = px.bar(

            bairros,

            x="bairro",

            y="Quantidade",

            title="Hospedagens por Bairro"

        )

        return fig