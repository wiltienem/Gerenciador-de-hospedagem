import streamlit as st


class CardHospedagem:

    @staticmethod
    def mostrar(h):

        with st.container():

            c1, c2 = st.columns([1,3])

            with c1:

                st.image(
                    "https://images.unsplash.com/photo-1564013799919-ab600027ffc6?w=800",
                    use_container_width=True
                )

            with c2:

                st.subheader(h["nome"])
                st.write(f"📍 {h['bairro']}")
                st.write(f"🏠 {h['tipo']}")
                st.write(f"⭐ {h['avaliacao']}")
                st.write(f"👥 {h['hospedes_max']} hóspedes")
                st.success(f"R$ {h['preco']:.2f} / noite")

            st.divider()