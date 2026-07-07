import streamlit as st


class Inicio:

    def __init__(self, sistema):
        self.sistema = sistema

    def mostrar(self):

        hospedagens = self.sistema.get_hospedagens()
        hospedes = self.sistema.get_hospedes()
        reservas = self.sistema.get_reservas()
        pagamentos = self.sistema.get_pagamentos()

        receita = 0
        if len(pagamentos) > 0:
            receita = pagamentos["valor"].sum()

        st.markdown(
            """
            <h1 style='text-align:center;color:#2563EB;'>
                🏨 Gerenciador de Hospedagem
            </h1>

            <h4 style='text-align:center;color:gray;'>
                Sistema Inteligente de Gerenciamento de Hospedagens
            </h4>
            """,
            unsafe_allow_html=True
        )

        st.markdown("---")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "🏠 Hospedagens",
            len(hospedagens)
        )

        c2.metric(
            "👤 Hóspedes",
            len(hospedes)
        )

        c3.metric(
            "📅 Reservas",
            len(reservas)
        )

        c4.metric(
            "💰 Receita",
            f"R$ {receita:,.2f}"
        )

        st.markdown("---")

        c1, c2 = st.columns([2, 1])

        with c1:

            st.subheader("Bem-vindo ao Gerenciador de Hospedagem")

            st.write("""
Nosso sistema foi desenvolvido para facilitar o gerenciamento de hospedagens.

### Funcionalidades

- 🏠 Cadastro de hospedagens
- 👤 Controle de hóspedes
- 📅 Reservas
- 💳 Pagamentos
- ⭐ Avaliações
- 📊 Dashboard
- 📈 Relatórios
            """)

        with c2:

            st.info(
                """
### Projeto

🎓 Programação Orientada a Objetos

🏫 Sistema de Hospedagem

📍 Florianópolis

Versão 1.0
"""
            )

        st.markdown("---")

        st.subheader("Resumo Financeiro")

        c1, c2, c3 = st.columns(3)

        c1.success(
            f"Preço médio\n\nR$ {hospedagens['preco'].mean():.2f}"
        )

        c2.warning(
            f"Maior diária\n\nR$ {hospedagens['preco'].max():.2f}"
        )

        c3.info(
            f"Menor diária\n\nR$ {hospedagens['preco'].min():.2f}"
        )