from classes.leitor_csv import LeitorCSV


class Sistema:

    def __init__(self):

        self._listings = LeitorCSV.carregar("dados/listings.csv")

        self._hospedes = LeitorCSV.carregar("dados/hospedes.csv")

        self._reservas = LeitorCSV.carregar("dados/reservas.csv")

        self._pagamentos = LeitorCSV.carregar("dados/pagamentos.csv")

        self._avaliacoes = LeitorCSV.carregar("dados/avaliacoes.csv")

    def get_hospedagens(self):

        return self._listings

    def get_hospedes(self):

        return self._hospedes

    def get_reservas(self):

        return self._reservas

    def get_pagamentos(self):

        return self._pagamentos

    def get_avaliacoes(self):

        return self._avaliacoes
    
    def atualizar_hospedes(self):

        self._hospedes = LeitorCSV.carregar(
        "dados/hospedes.csv"
    )
        
    def atualizar_reservas(self):

        self._reservas = LeitorCSV.carregar(
        "dados/reservas.csv"
    )
        
    def atualizar_pagamentos(self):

        self._pagamentos = LeitorCSV.carregar(
        "dados/pagamentos.csv"
    )