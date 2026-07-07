import plotly.express as px


class GraficoBoxPlot:

    @staticmethod
    def criar(df):

        fig = px.box(
            df,
            y="preco",
            title="Distribuição dos Preços"
        )

        return fig