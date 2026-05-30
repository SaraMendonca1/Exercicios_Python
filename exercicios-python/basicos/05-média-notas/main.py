nota1= float(input("Digite 1ª nota: ")) # O programa solicita que o usuário digite a primeira nota e armazena a entrada na variável "nota1". A função float() é utilizada para converter a entrada do usuário em um número decimal, permitindo que o programa realize operações matemáticas com esse valor.
nota2= float(input("Digite 2ª nota: ")) # O programa solicita que o usuário digite a segunda nota e armazena a entrada na variável "nota2". A função float() é utilizada para converter a entrada do usuário em um número decimal, permitindo que o programa realize operações matemáticas com esse valor.
nota3= float(input("Digite 3ª nota: ")) # O programa solicita que o usuário digite a terceira nota e armazena a entrada na variável "nota3". A função float() é utilizada para converter a entrada do usuário em um número decimal, permitindo que o programa realize operações matemáticas com esse valor.

media= (nota1+nota2+nota3)/3 # O programa calcula a média das três notas somando as variáveis "nota1", "nota2" e "nota3", e dividindo o resultado por 3. O resultado é armazenado na variável "media".
print(f"Média: {media:.2f}") # O programa exibe a média calculada em um formato específico. A expressão f"Média: {media:.2f}" utiliza f-strings para formatar a saída. A média é exibida com 2 casas decimais, proporcionando uma apresentação mais legível do resultado.

if media>=7: # O programa verifica se a média é maior ou igual a 7 utilizando o operador de comparação >=. Se a condição for verdadeira, significa que o aluno foi aprovado, e o programa executa o código dentro do bloco if.
    print("Aprovado(a)!") # Se a condição if for verdadeira, o programa exibe a mensagem "Aprovado(a)!" para indicar que o aluno foi aprovado. 
else:
    print("Reprovado(a)!") # Se a condição if for falsa, ou seja, se a média for menor que 7, o programa executa o código dentro do bloco else e exibe a mensagem "Reprovado(a)!" para indicar que o aluno foi reprovado.