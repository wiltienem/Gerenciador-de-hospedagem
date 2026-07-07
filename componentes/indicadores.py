import streamlit as st


class Indicadores:

    @staticmethod
    def mostrar(sistema):

        hospedagens = sistema.get_hospedagens()
        hospedes = sistema.get_hospedes()
        reservas = sistema.get_reservas()
        pagamentos = sistema.get_pagamentos()

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.metric(
                "🏠 Hospedagens",
                len(hospedagens)
            )

        with c2:
            st.metric(
                "👤 Hóspedes",
                len(hospedes)
            )

        with c3:
            st.metric(
                "📅 Reservas",
                len(reservas)
            )

        with c4:

            if len(pagamentos) > 0:
                total = pagamentos["valor"].sum()
            else:
                total = 0

            st.metric(
                "💰 Receita",
                f"R$ {total:,.2f}"
            )