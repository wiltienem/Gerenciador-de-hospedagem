import streamlit as st
from componentes.indicadores import Indicadores
from graficos.grafico_barras import GraficoBarras
from graficos.grafico_boxplot import GraficoBoxPlot
from graficos.grafico_linhas import GraficoLinhas
from graficos.grafico_pizza import GraficoPizza
from graficos.grafico_mapa import GraficoMapa


class DashboardPagina:

    def __init__(self, sistema):

        self.sistema = sistema

    def mostrar(self):

        st.title("📊 Dashboard")

        Indicadores.mostrar(self.sistema)

        df = self.sistema.get_hospedagens()

        c1, c2 = st.columns(2)

        with c1:

            st.plotly_chart(

                GraficoBarras.criar(df),

                use_container_width=True

            )

            st.plotly_chart(

                GraficoLinhas.criar(df),

                use_container_width=True

            )

        with c2:

            st.plotly_chart(

                GraficoPizza.criar(df),

                use_container_width=True

            )

            st.plotly_chart(

                GraficoBoxPlot.criar(df),

                use_container_width=True

            )

            st.subheader("🗺️ Localização das Hospedagens")

            st.plotly_chart(
                GraficoMapa.criar(df),
                use_container_width=True
            )