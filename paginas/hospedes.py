from utils.manipulador_csv import ManipuladorCSV
import streamlit as st
import pandas as pd
import os


class Hospedes:

    def __init__(self, sistema):
        self.sistema = sistema

    def mostrar(self):

        st.title("👤 Hóspedes")

        df = self.sistema.get_hospedes()

        aba1, aba2 = st.tabs(["📋 Lista de Hóspedes", "➕ Cadastrar"])

        # ==========================
        # LISTA
        # ==========================

        with aba1:

            st.subheader("Hóspedes Cadastrados")

            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True
            )

        st.divider()

        st.subheader("🗑️ Excluir Hóspede")

        if len(df) > 0:

            hospede_excluir = st.selectbox(
                "Selecione o hóspede",
                df["nome"],
                key="excluir_hospede"
            )

            if st.button("Excluir Hóspede"):

                df = df[df["nome"] != hospede_excluir]

                df.to_csv(
                    "dados/hospedes.csv",
                    index=False
                )

                st.success("Hóspede excluído com sucesso!")

                st.rerun()

            st.divider()

            st.divider()

            st.subheader("Pesquisar")

            pesquisa = st.text_input("Nome do hóspede")

            if pesquisa:

                resultado = df[
                    df["nome"].str.contains(
                        pesquisa,
                        case=False
                    )
                ]

                st.dataframe(
                    resultado,
                    use_container_width=True
                )
                st.divider()

            st.subheader("Excluir Hóspede")

            if len(df) > 0:

                excluir = st.selectbox(

                    "Selecione",

                    df["nome"]

                )

                if st.button("Excluir"):

                    indice = df[
                        df["nome"] == excluir
                    ].index[0]

                    df = ManipuladorCSV.excluir(
                        df,
                        indice
                    )

                    ManipuladorCSV.salvar(
                        df,
                        "dados/hospedes.csv"
                    )

                    st.success("Hóspede removido!")

                    st.rerun()

        # ==========================
        # CADASTRO
        # ==========================

        with aba2:

            st.subheader("Novo Hóspede")

            nome = st.text_input("Nome")

            cpf = st.text_input("CPF")

            email = st.text_input("E-mail")

            telefone = st.text_input("Telefone")

            if st.button("Cadastrar"):

                if (
                    nome == ""
                    or cpf == ""
                    or email == ""
                    or telefone == ""
                ):

                    st.error("Preencha todos os campos.")

                else:

                    novo = pd.DataFrame({

                        "id": [len(df) + 1],

                        "nome": [nome],

                        "cpf": [cpf],

                        "email": [email],

                        "telefone": [telefone]

                    })

                    df = pd.concat(
                        [df, novo],
                        ignore_index=True
                    )

                    caminho = os.path.join(
                        "dados",
                        "hospedes.csv"
                    )

                    ManipuladorCSV.salvar(df, caminho)

                    st.success("Hóspede cadastrado com sucesso!")

                    st.rerun()