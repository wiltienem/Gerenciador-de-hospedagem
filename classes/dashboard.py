import streamlit as st

from paginas.inicio import Inicio
from paginas.hospedagens import Hospedagens
from paginas.hospedes import Hospedes
from paginas.reservas import Reservas
from paginas.pagamentos import Pagamentos
from paginas.avaliacoes import Avaliacoes
from paginas.dashboard import DashboardPagina
from paginas.relatorios import Relatorios


class Dashboard:

    def __init__(self, sistema):
        self.sistema = sistema

    def iniciar(self):

        st.set_page_config(
            page_title="Gerenciador de Hospedagem",
            page_icon="🏨",
            layout="wide",
            initial_sidebar_state="expanded"
        )

        st.sidebar.title("🏨 Gerenciador de Hospedagem")
        st.sidebar.markdown("---")
        st.sidebar.success("Sistema de Gerenciamento")
        st.sidebar.markdown("---")

        pagina = st.sidebar.radio(
            "Menu",
            [
                "🏠 Início",
                "🏡 Hospedagens",
                "👤 Hóspedes",
                "📅 Reservas",
                "💳 Pagamentos",
                "⭐ Avaliações",
                "📊 Dashboard",
                "📈 Relatórios"
            ]
        )

        if pagina == "🏠 Início":
            Inicio(self.sistema).mostrar()

        elif pagina == "🏡 Hospedagens":
            Hospedagens(self.sistema).mostrar()

        elif pagina == "👤 Hóspedes":
            Hospedes(self.sistema).mostrar()

        elif pagina == "📅 Reservas":
            Reservas(self.sistema).mostrar()

        elif pagina == "💳 Pagamentos":
            Pagamentos(self.sistema).mostrar()

        elif pagina == "⭐ Avaliações":
            Avaliacoes(self.sistema).mostrar()

        elif pagina == "📊 Dashboard":
            DashboardPagina(self.sistema).mostrar()

        elif pagina == "📈 Relatórios":
            Relatorios(self.sistema).mostrar()