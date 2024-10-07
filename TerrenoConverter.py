class TerrenoConverter:
    def __init__(self):
        self._largura = None
        self._comprimento = None

    # Método para calcular a área
    def calcular_area(self):
        if self._largura is not None and self._comprimento is not None:
            return self._largura * self._comprimento
        else:
            return None

    # Método para calcular o perímetro
    def calcular_perimetro(self):
        if self._largura is not None and self._comprimento is not None:
            return 2 * (self._largura + self._comprimento)
        else:
            return None

    # Getters e Setters para largura e comprimento
    @property
    def largura(self):
        return self._largura

    @largura.setter
    def largura(self, value):
        if value <= 0:
            raise ValueError("A largura deve ser maior que 0.")
        self._largura = value

    @property
    def comprimento(self):
        return self._comprimento

    @comprimento.setter
    def comprimento(self, value):
        if value <= 0:
            raise ValueError("O comprimento deve ser maior que 0.")
        self._comprimento = value
