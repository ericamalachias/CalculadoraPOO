import tkinter as tk
from tkinter import messagebox
from operacoes import Soma, Subtracao, Multiplicacao, Divisao


class CalculadoraApp:
    def __init__(self, calculadora):
        self.calculadora = calculadora

        self.janela = tk.Tk()
        self.janela.title("Calculadora POO")
        self.janela.geometry("350x450")

        tk.Label(self.janela, text="Primeiro número:").pack(pady=3)
        self.entrada1 = tk.Entry(self.janela)
        self.entrada1.pack(pady=3)

        tk.Label(self.janela, text="Segundo número:").pack(pady=3)
        self.entrada2 = tk.Entry(self.janela)
        self.entrada2.pack(pady=3)

        frame_botoes = tk.Frame(self.janela)
        frame_botoes.pack(pady=10)

        tk.Button(frame_botoes, text="Somar (+)", width=13, command=self.somar).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(frame_botoes, text="Subtrair (-)", width=13, command=self.subtrair).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(frame_botoes, text="Multiplicar (*)", width=13, command=self.multiplicar).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(frame_botoes, text="Dividir (/)", width=13, command=self.dividir).grid(row=1, column=1, padx=5, pady=5)

        self.label_resultado = tk.Label(self.janela, text="Resultado: ", font=("Arial", 12, "bold"))
        self.label_resultado.pack(pady=8)

        tk.Button(self.janela, text="Limpar Campos", command=self.limpar_campos).pack(pady=3)

        tk.Label(self.janela, text="Histórico:").pack(pady=5)
        self.lista_historico = tk.Listbox(self.janela, width=40, height=7)
        self.lista_historico.pack(pady=3)

        tk.Button(self.janela, text="Limpar Histórico", command=self.limpar_historico).pack(pady=5)

    def pegar_numeros(self):
        try:
            num1 = float(self.entrada1.get())
            num2 = float(self.entrada2.get())
            return num1, num2
        except ValueError:
            raise ValueError("Digite apenas números válidos.")

    def fazer_conta(self, operacao, simbolo):
        resultado = self.calculadora.calcular(operacao, simbolo)
        self.label_resultado.config(text=f"Resultado: {resultado}")
        self.atualizar_historico()

    def somar(self):
        try:
            n1, n2 = self.pegar_numeros()
            self.fazer_conta(Soma(n1, n2), "+")
        except ValueError as erro:
            messagebox.showerror("Erro", str(erro))

    def subtrair(self):
        try:
            n1, n2 = self.pegar_numeros()
            self.fazer_conta(Subtracao(n1, n2), "-")
        except ValueError as erro:
            messagebox.showerror("Erro", str(erro))

    def multiplicar(self):
        try:
            n1, n2 = self.pegar_numeros()
            self.fazer_conta(Multiplicacao(n1, n2), "*")
        except ValueError as erro:
            messagebox.showerror("Erro", str(erro))

    def dividir(self):
        try:
            n1, n2 = self.pegar_numeros()
            self.fazer_conta(Divisao(n1, n2), "/")
        except ValueError as erro:
            messagebox.showerror("Erro", str(erro))

    def atualizar_historico(self):
        self.lista_historico.delete(0, tk.END)
        for item in self.calculadora.historico.listar():
            self.lista_historico.insert(tk.END, item)

    def limpar_campos(self):
        self.entrada1.delete(0, tk.END)
        self.entrada2.delete(0, tk.END)
        self.label_resultado.config(text="Resultado: ")

    def limpar_historico(self):
        self.calculadora.historico.limpar()
        self.atualizar_historico()

    def executar(self):
        self.janela.mainloop()