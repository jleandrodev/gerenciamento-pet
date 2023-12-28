class ConsultaPet():
    def __init__(self, pet, motivo, peso_atual, medicamento_atual, exames, receita, data=""):
        self.__pet = pet
        self.__motivo = motivo
        self.__peso_atual = peso_atual
        self.__medicamento_atual = medicamento_atual
        self.__exames = exames
        self.__data = data
        self.__receita = receita

    @property
    def pet(self):
        return self.__pet
    @pet.setter
    def pet(self, pet):
        self.__pet = pet

    @property
    def motivo(self):
        return self.__motivo
    @motivo.setter
    def motivo(self, motivo):
        self.__motivo = motivo

    @property
    def peso_atual(self):
        return self.__peso_atual
    @peso_atual.setter
    def peso_atual(self, peso_atual):
        self.__peso_atual = peso_atual

    @property
    def medicamento_atual(self):
        return self.__medicamento_atual
    @medicamento_atual.setter
    def medicamento_atual(self, medicamento_atual):
        self.__medicamento_atual = medicamento_atual

    @property
    def exames(self):
        return self.__exames
    @exames.setter
    def exames(self, exames):
        self.__exames = exames
        
    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def receita(self):
        return self.__receita
    @receita.setter
    def receita(self, receita):
        self.__receita = receita

