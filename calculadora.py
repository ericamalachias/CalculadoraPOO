from historico import Historico

class Calculadora:
    def __init__(self):
        self.historico = Historico()

    def calcular(self, operacao, simbolo):
        resultado = operacao.executar()
        texto = f"{operacao.primeiro} {simbolo} {operacao.segundo} = {resultado}"
        self.historico.adicionar(texto)
        return resultado