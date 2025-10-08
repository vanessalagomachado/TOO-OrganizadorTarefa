from datetime import datetime

class Agendamento:
    def __init__(self, data_inicio: datetime, data_final: datetime, atividades: str, nome: str, local: str):
        self.data_inicio = data_inicio
        self.data_final = data_final
        self.atividades = atividades
        self.nome = nome
        self.local = local

    # Getter and Setter for data_inicio
    @property
    def data_inicio(self) -> datetime:
        return self.__data_inicio

    @data_inicio.setter
    def data_inicio(self, data_inicio: datetime):
        self.__data_inicio = data_inicio

    # Getter and Setter for data_final
    @property
    def data_final(self) -> datetime:
        return self.__data_final

    @data_final.setter
    def data_final(self, data_final: datetime):
        self.__data_final = data_final

    # Getter and Setter for atividades
    @property
    def atividades(self):
        return self.__atividades

    @atividades.setter
    def atividades(self, atividades: str):
        self.__atividades = atividades.strip()

    # Getter and Setter for nome
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome.strip().title()

    # Getter and Setter for local
    @property
    def local(self):
        return self.__local

    @local.setter
    def local(self, local: str):
        self.__local = local.strip()
        
    # Método especial __str__
    def __str__(self):
        inicio = self.data_inicio.strftime('%d-%m-%Y %H:%M') if isinstance(self.data_inicio, datetime) else ""
        fim = self.data_final.strftime('%d-%m-%Y %H:%M') if isinstance(self.data_final, datetime) else ""
        return f"Agendamento: {self.nome} ({inicio} -> {fim})"
        
    # Método exibir_dados
    def exibir_dados(self):
        inicio = self.data_inicio.strftime('%d-%m-%Y %H:%M') if isinstance(self.data_inicio, datetime) else ""
        fim = self.data_final.strftime('%d-%m-%Y %H:%M') if isinstance(self.data_final, datetime) else ""
        atividades = f"Atividades: {self.atividades}\n" if self.atividades else ""
        local = f"Local: {self.local}\n" if self.local else ""

        return (
            f"--- Agendamento ---\n"
            f"Nome: {self.nome}\n"
            f"{atividades}"
            f"{local}"
            f"Início: {inicio}\n"
            f"Término: {fim}\n"
        )