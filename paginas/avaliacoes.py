import streamlit as st
import pandas as pd
import os


class Avaliacoes:

    def __init__(self, sistema):
        self.sistema = sistema

    def mostrar(self):

        st.title("⭐ Avaliações")

        avaliacoes = self.sistema.get_avaliacoes()
        hospedes = self.sistema.get_hospedes()
        hospedagens = self.sistema.get_hospedagens()

        aba1, aba2 = st.tabs(
            ["📋 Avaliações", "➕ Nova Avaliação"]
        )

        with aba1:

            st.dataframe(
                avaliacoes,
                use_container_width=True,
                hide_index=True
            )

        with aba2:

            hospede = st.selectbox(
                "Hóspede",
                hospedes["nome"]
            )

            hospedagem = st.selectbox(
                "Hospedagem",
                hospedagens["nome"]
            )

            nota = st.slider(
                "Nota",
                1,
                5,
                5
            )

            comentario = st.text_area(
                "Comentário"
            )

            if st.button("Salvar Avaliação"):

                id_hospede = hospedes.loc[
                    hospedes["nome"] == hospede,
                    "id"
                ].values[0]

                id_hospedagem = hospedagens.loc[
                    hospedagens["nome"] == hospedagem,
                    "id"
                ].values[0]

                nova = pd.DataFrame({

                    "id": [len(avaliacoes) + 1],

                    "id_hospede": [id_hospede],

                    "id_hospedagem": [id_hospedagem],

                    "nota": [nota],

                    "comentario": [comentario]

                })

                avaliacoes = pd.concat(
                    [avaliacoes, nova],
                    ignore_index=True
                )

                avaliacoes.to_csv(
                    os.path.join(
                        "dados",
                        "avaliacoes.csv"
                    ),
                    index=False
                )

                st.success(
                    "Avaliação salva com sucesso!"
                )

                st.rerun()