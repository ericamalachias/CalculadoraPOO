from abc import ABC, abstractmethod


class Operacao(ABC):
    def __init__(self, primeiro, segundo):
        self.primeiro = float(primeiro)
        self.segundo = float(segundo)

    @abstractmethod
    def executar(self):
        pass


class Soma(Operacao):
    def executar(self):
        return self.primeiro + self.segundo


class Subtracao(Operacao):
    def executar(self):
        return self.primeiro - self.segundo


class Multiplicacao(Operacao):
    def executar(self):
        return self.primeiro * self.segundo


class Divisao(Operacao):
    def executar(self):
        if self.segundo == 0:
            raise ValueError("Não é possível dividir por zero.")
        return self.primeiro / self.segundo