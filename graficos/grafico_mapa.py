import plotly.express as px


class GraficoMapa:

    @staticmethod
    def criar(df):

        fig = px.scatter_mapbox(
            df,
            lat="latitude",
            lon="longitude",
            hover_name="nome",
            hover_data={
                "bairro": True,
                "preco": True,
                "latitude": False,
                "longitude": False
            },
            zoom=10,
            height=600
        )

        fig.update_layout(
            mapbox_style="open-street-map",
            margin={"r": 0, "t": 40, "l": 0, "b": 0},
            title="Mapa das Hospedagens"
        )

        return fig