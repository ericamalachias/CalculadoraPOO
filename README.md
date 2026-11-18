# Calculadora Desktop com POO

Aplicação de calculadora simples com interface gráfica desenvolvida em Python utilizando Tkinter e os conceitos de Programação Orientada a Objetos (POO).

## Funcionalidades
- Realizar operações básicas: soma, subtração, multiplicação e divisão.
- Exibir o resultado na tela.
- Limpar os campos de entrada e o resultado.
- Registrar as contas feitas em um histórico.
- Limpar o histórico de operações.
- Exibir mensagens de erro para entradas inválidas (letras ou campos vazios) e divisão por zero.

## Estrutura do Projeto
- `main.py`: arquivo principal que inicia a aplicação.
- `operacoes.py`: define a classe abstrata `Operacao` e as classes `Soma`, `Subtracao`, `Multiplicacao` e `Divisao`.
- `historico.py`: define a classe `Historico`, responsável por guardar, listar e limpar os registros.
- `calculadora.py`: define a classe `Calculadora`, que executa a operação e salva o resultado no histórico.
- `interface.py`: define a classe `CalculadoraApp`, que cria a janela e os botões com Tkinter.

## Conceitos de POO Aplicados
- **Abstração:** a classe `Operacao` serve de modelo e obriga todas as operações a terem o método `executar()`.
- **Herança:** `Soma`, `Subtracao`, `Multiplicacao` e `Divisao` herdam atributos da classe `Operacao`.
- **Polimorfismo:** a `Calculadora` executa qualquer operação chamando `operacao.executar()`, sem precisar de vários `if`.
- **Encapsulamento:** a lista interna de registros do `Historico` é acessada apenas pelos métodos da própria classe.
- **Composição:** a `Calculadora` possui um objeto `Historico` para registrar os cálculos.

## Como Executar o Projeto

### Pelo código-fonte (Python)
1. Abra o terminal na pasta onde estão os arquivos `.py`.
2. Execute o comando:
```bash
python main.py
