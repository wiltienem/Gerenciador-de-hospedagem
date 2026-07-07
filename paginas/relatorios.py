import streamlit as st
import pandas as pd


class Relatorios:

    def __init__(self, sistema):
        self.sistema = sistema

    def mostrar(self):

        st.title("📈 Relatórios")

        opcao = st.selectbox(

            "Selecione o relatório",

            [

                "Hospedagens",

                "Hóspedes",

                "Reservas",

                "Pagamentos",

                "Avaliações"

            ]

        )

        if opcao == "Hospedagens":
            df = self.sistema.get_hospedagens()

        elif opcao == "Hóspedes":
            df = self.sistema.get_hospedes()

        elif opcao == "Reservas":
            df = self.sistema.get_reservas()

        elif opcao == "Pagamentos":
            df = self.sistema.get_pagamentos()

        else:
            df = self.sistema.get_avaliacoes()

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        csv = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="📥 Baixar relatório CSV",
            data=csv,
            file_name=f"{opcao.lower()}.csv",
            mime="text/csv"
        )