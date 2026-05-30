# Entrada de dados do usuário:
nome= (input("Informe seu nome: "))
# O "input(...)" mostra a mensagem entre parênteses e espera o usuário digitar algo. O que for digitado é retornado como um texto e armazenado na variável "nome".
print(f"Olá, {nome}! Bem vindo(a) ao mundo Python!")
# O "print(...)" exibe a mensagem entre parênteses na tela. O "f" antes da string indica que é uma f-string, permitindo a inclusão de variáveis dentro da string usando chaves {}. Aqui, o valor da variável "nome" será inserido na mensagem exibida ao usuário. Ou seja, se o usuário digitar "Sara", a mensagem exibida será "Olá, Sara! Bem vindo(a) ao mundo Python!"