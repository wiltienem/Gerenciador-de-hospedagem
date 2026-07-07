import streamlit as st
from componentes.card_hospedagem import CardHospedagem

class Hospedagens:

    def __init__(self, sistema):
        self.sistema = sistema

    def mostrar(self):

        st.title("🏠 Hospedagens")

        df = self.sistema.get_hospedagens()

        st.sidebar.header("Filtros")

        bairro = st.sidebar.selectbox(
            "Bairro",
            ["Todos"] + sorted(df["bairro"].unique().tolist())
        )

        tipo = st.sidebar.selectbox(
            "Tipo",
            ["Todos"] + sorted(df["tipo"].unique().tolist())
        )

        busca = st.text_input(
            "🔍 Buscar hospedagem"
        )

        resultado = df.copy()

        if bairro != "Todos":
            resultado = resultado[
                resultado["bairro"] == bairro
            ]

        if tipo != "Todos":
            resultado = resultado[
                resultado["tipo"] == tipo
            ]

        if busca:

            resultado = resultado[
                resultado["nome"].str.contains(
                    busca,
                    case=False
                )
            ]

        st.write(f"**{len(resultado)} hospedagens encontradas**")

        for _, h in resultado.iterrows():
         CardHospedagem.mostrar(h)

         st.divider()