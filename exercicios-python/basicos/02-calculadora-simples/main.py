while True: # # O while True faz com que o programa seja executado até que o break seja encontrado no código, permitindo que o usuário escolha opções repetidamente até decidir sair do programa. 
    print("-"*5, "CALCULADORA SIMPLES", "-"*5) # Exibe o título da calculadora no programa, cercado por linhas de traços para destacar o título.
    print("1 - Somar") 
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Sair")
# O programa exibe um menu de opções para o usuário, listando as operações disponíveis (somar, subtrair, multiplicar, dividir) e a opção para sair do programa (0).
    opcao= input("Digite a opção desejada: ") # O programa solicita que o usuário digite a opção desejada e armazena a entrada na variável "opcao".
    if opcao == '0': 
        print("Fim do programa") # Se a opção escolhida for 0, o programa exibe a mensagem "Fim do programa" para indicar que o programa está sendo encerrado.
        break # O comando break é utilizado para sair do loop while, encerrando a execução do programa.
    if opcao in ['1','2','3','4']: #Se a opção escolhida for válida (1,2,3 ou 4), o programa solicitará os números para realizar a operação. 
        try:
            num1=float(input("Digite 1º número: ")) # Pede o primeiro número e o converte para float.
            num2=float(input("Digite 2º número: ")) # Pede o segundo número e o converte para float. 
            match int(opcao): # O programa utiliza a estrutura de controle match-case para determinar qual operação realizar com base na opção escolhida pelo usuário.
                case 1: # Se a opção for 1, o programa realiza a soma dos dois números e exibe o resultado.
                    print(f"Resultado: {num1} + {num2} = {num1+num2}")
                case 2: # Se a opção for 2, o programa realiza a subtração dos dois números e exibe o resultado.
                    print(f"Resultado: {num1} - {num2} = {num1-num2}")
                case 3: # Se a opção for 3, o programa realiza a multiplicação dos dois números e exibe o resultado.
                    print(f"Resultado: {num1} * {num2} = {num1*num2}")
                case 4: # Se a opção for 4, o programa verifica se o segundo número é zero para evitar a divisão por zero. Se for zero, exibe uma mensagem de erro; caso contrário, realiza a divisão e exibe o resultado.
                    if num2==0: 
                        print("Não é permitida a divisão por zero")
                    else:
                        print(f"Resultado: {num1} / {num2} = {num1/num2}")
        
        except ValueError: # Se o usuário inserir um valor que não pode ser convertido para float, o programa captura a exceção ValueError e exibe uma mensagem de erro, solicitando que o usuário tente novamente.
            print("Erro! Tente novamente") # O programa continua a execução, permitindo que o usuário escolha uma nova opção ou insira novos números para realizar as operações.
    else: 
        print("Digite apenas as opções válidas") # Se a opção escolhida pelo usuário não for válida (diferente de 0, 1, 2, 3 ou 4), o programa exibe uma mensagem de erro solicitando que o usuário digite apenas as opções válidas. O programa então continua a execução, permitindo que o usuário escolha uma nova opção.
