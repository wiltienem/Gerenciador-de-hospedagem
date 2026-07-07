import plotly.express as px


class GraficoPizza:

    @staticmethod
    def criar(df):

        tipos = (
            df.groupby("tipo")
            .size()
            .reset_index(name="Quantidade")
        )

        fig = px.pie(

            tipos,

            values="Quantidade",

            names="tipo",

            title="Tipos de Hospedagem"

        )

        return fig