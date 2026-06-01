num= int(input("Digite um número: ")) # O programa solicita que o usuário digite um número inteiro e armazena a entrada na variável "num". A função int() é utilizada para converter a entrada do usuário em um número inteiro, permitindo que o programa realize operações matemáticas com esse valor.

if num%2==0: # O programa verifica se o número é par ou ímpar utilizando o operador de módulo (%), retornando o resto da divisão de "num" por 2. 
    print(f"O número{num} é par!") # Se o resultado da operação num%2 for igual a 0, significa que o número é par, e o programa exibe a mensagem indicando que o número é par.
else:
    print(f"O número {num} é ímpar!") # Se o resultado da operação num%2 for diferente de 0, significa que o número é ímpar, e o programa exibe a mensagem indicando que o número é ímpar.