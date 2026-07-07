import streamlit as st
import pandas as pd
import os
from datetime import date


class Reservas:

    def __init__(self, sistema):
        self.sistema = sistema

    def mostrar(self):

        st.title("📅 Reservas")

        reservas = self.sistema.get_reservas()
        hospedes = self.sistema.get_hospedes()
        hospedagens = self.sistema.get_hospedagens()

        aba1, aba2 = st.tabs(
            ["📋 Reservas", "➕ Nova Reserva"]
        )

        # ==========================
        # LISTA
        # ==========================

        with aba1:

            st.dataframe(
                reservas,
                use_container_width=True,
                hide_index=True
            )

        # ==========================
        # NOVA RESERVA
        # ==========================

        with aba2:

            hospede = st.selectbox(
                "Hóspede",
                hospedes["nome"]
            )

            hospedagem = st.selectbox(
                "Hospedagem",
                hospedagens["nome"]
            )

            checkin = st.date_input(
                "Check-in",
                value=date.today()
            )

            checkout = st.date_input(
                "Check-out",
                value=date.today()
            )

            diaria = hospedagens.loc[
                hospedagens["nome"] == hospedagem,
                "preco"
            ].values[0]

            dias = (checkout - checkin).days

            if dias <= 0:
                dias = 1

            total = diaria * dias

            st.success(
                f"Valor Total: R$ {total:.2f}"
            )

            if st.button("Salvar Reserva"):

                id_hospede = hospedes.loc[
                    hospedes["nome"] == hospede,
                    "id"
                ].values[0]

                id_hospedagem = hospedagens.loc[
                    hospedagens["nome"] == hospedagem,
                    "id"
                ].values[0]

                nova = pd.DataFrame({

                    "id": [len(reservas) + 1],

                    "id_hospede": [id_hospede],

                    "id_hospedagem": [id_hospedagem],

                    "checkin": [checkin],

                    "checkout": [checkout],

                    "valor_total": [total],

                    "status": ["Confirmada"]

                })

                reservas = pd.concat(
                    [reservas, nova],
                    ignore_index=True
                )

                reservas.to_csv(
                    os.path.join(
                        "dados",
                        "reservas.csv"
                    ),
                    index=False
                )

                st.success(
                    "Reserva cadastrada!"
                )

                st.rerun()