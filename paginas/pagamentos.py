import streamlit as st
import pandas as pd
import os
from datetime import date


class Pagamentos:

    def __init__(self, sistema):
        self.sistema = sistema

    def mostrar(self):

        st.title("💳 Pagamentos")

        pagamentos = self.sistema.get_pagamentos()
        reservas = self.sistema.get_reservas()

        aba1, aba2 = st.tabs(
            ["📋 Pagamentos", "➕ Novo Pagamento"]
        )

        # ==========================
        # LISTA
        # ==========================

        with aba1:

            st.dataframe(
                pagamentos,
                use_container_width=True,
                hide_index=True
            )

        # ==========================
        # NOVO PAGAMENTO
        # ==========================

        with aba2:

            reserva = st.selectbox(
                "Reserva",
                reservas["id"]
            )

            valor = reservas.loc[
                reservas["id"] == reserva,
                "valor_total"
            ].values[0]

            st.info(f"Valor da Reserva: R$ {valor:.2f}")

            metodo = st.selectbox(
                "Forma de Pagamento",
                [
                    "Pix",
                    "Cartão de Crédito",
                    "Cartão de Débito",
                    "Boleto"
                ]
            )

            data_pagamento = st.date_input(
                "Data do Pagamento",
                value=date.today()
            )

            if st.button("Registrar Pagamento"):

                novo = pd.DataFrame({

                    "id": [len(pagamentos) + 1],

                    "id_reserva": [reserva],

                    "valor": [valor],

                    "metodo": [metodo],

                    "data_pagamento": [data_pagamento]

                })

                pagamentos = pd.concat(
                    [pagamentos, novo],
                    ignore_index=True
                )

                pagamentos.to_csv(
                    os.path.join(
                        "dados",
                        "pagamentos.csv"
                    ),
                    index=False
                )

                st.success(
                    "Pagamento registrado com sucesso!"
                )

                st.rerun()