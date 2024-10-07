from model.TerrenoConverter import TerrenoConverter

class TerrenoController:
    def __init__(self):
        self._terreno_converter = TerrenoConverter()

    def validar_dimensoes(self):
        if self._terreno_converter.largura is None or self._terreno_converter.comprimento is None:
            raise ValueError("Ambas as dimensões (largura e comprimento) devem ser fornecidas.")

    def calcular_area(self):
        self.validar_dimensoes()
        return self._terreno_converter.calcular_area()

    def calcular_perimetro(self):
        self.validar_dimensoes()
        return self._terreno_converter.calcular_perimetro()

    # Getters e Setters
    @property
    def terreno_converter(self):
        return self._terreno_converter

    @terreno_converter.setter
    def terreno_converter(self, valor):
        self._terreno_converter = valor
