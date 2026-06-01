GERADOR DE TABUADAS MATEMÁTICAS
Este projeto consiste em um script Python que gera tabuadas completas para as quatro operações aritméticas básicas (soma, subtração, multiplicação e divisão), utilizando uma lógica de correspondência inversa para facilitar o aprendizado.

FUNCIONALIDADES
• Soma: Exibe a adição do número escolhido aos valores de 1 a 10.

• Subtração: Utiliza a lógica inversa da soma para apresentar resultados inteiros e positivos.

• Multiplicação: Exibe o produto do número escolhido pelos valores de 1 a 10.

• Divisão: Utiliza a lógica inversa da multiplicação para garantir divisões exatas e quocientes inteiros.

• Tratamento de Exceções: Bloqueia a entrada de dados inválidos (letras ou símbolos) através de um bloco try-except.

TECNOLOGIAS UTILIZADAS
• Python 3

• Estruturas de repetição (for loops).

• Formatação de strings (f-strings) com controle de espaçamento e alinhamento de colunas.

COMO EXECUTAR
1. Certifique-se de ter o Python instalado.

2. Salve o código em um arquivo main.py.

3. Execute no terminal:

python main.py

DETALHES DA LÓGICA APLICADA
Diferente de uma tabuada simples, este código aplica conceitos de operações inversas para melhorar a clareza visual:

• Na Subtração: Em vez de subtrair valores de 1 a 10 do número base, o programa calcula o minuendo de forma que o resultado seja sempre o índice do laço.

• Na Divisão: O programa define o dividendo como o produto de num * i, garantindo que o divisor (num) resulte sempre em um quociente exato.

EXEMPLO DE SAÍDA
Digite um número inteiro: 5
Tabuada de 5

SOMA
5 +  1 = 6.00
5 +  2 = 7.00
...
------------------------------
SUBTRAÇÃO
 6 - 5 = 1.00
 7 - 5 = 2.00
...
------------------------------
DIVISÃO
 5 / 5 =  1
10 / 5 =  2
...