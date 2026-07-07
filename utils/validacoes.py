"""
Arquivo criado automaticamente.
"""

import re


class Validacoes:

    @staticmethod
    def validar_email(email):

        padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        return re.match(padrao, email) is not None

    @staticmethod
    def validar_cpf(cpf):

        cpf = cpf.replace(".", "").replace("-", "")

        return len(cpf) == 11 and cpf.isdigit()

    @staticmethod
    def validar_preco(preco):

        return preco >= 0