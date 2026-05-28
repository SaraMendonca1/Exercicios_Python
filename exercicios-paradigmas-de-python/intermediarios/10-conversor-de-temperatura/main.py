while True: # O while True faz com que o programa seja executado até que o break seja encontrado no código, permitindo que o usuário escolha opções repetidamente até decidir sair do programa.
    print("-"*5, "Conversor de temperatura", "-"*5) # Exibe o título do programa, cercado por linhas de traços para destacar o título.
    print("1 - Celsius para Fahrenheit") 
    print("2 - Fahrenheit para Celsius")
    print("0 - Sair")
# Exibe um menu de opções para o usuário, listando as conversões disponíveis (Celsius para Fahrenheit e Fahrenheit para Celsius) e a opção para sair do programa (0).
    opcao= input("Escolha uma opção: ").strip() # O programa solicita que o usuário escolha uma opção e armazena a entrada na variável "opcao", removendo quaisquer espaços em branco extras com o método strip().

    if opcao == "0": # Se a opção escolhida for 0, o programa exibe uma mensagem de encerramento e sai do loop, terminando a execução.
        print("Fim do programa") # Exibe a mensagem "Fim do programa" para indicar que o programa está sendo encerrado.
        break # O comando break é utilizado para sair do loop while, encerrando a execução do programa.

    elif opcao == "1": # Se a opção escolhida for 1, o programa solicita a temperatura em Celsius.
        c = float(input("Informe a temperatura em Celsius: ")) # O programa solicita que o usuário informe a temperatura em Celsius e armazena a entrada na variável "c", convertendo-a para um número de ponto flutuante.
        resultado = (c * 9/5) + 32 # O programa realiza a conversão da temperatura de Celsius para Fahrenheit usando a fórmula adequada.
        print(f"{c}°C = {resultado:.2f}°F") # O programa exibe o resultado da conversão em um formato específico, com duas casas decimais.

    elif opcao == "2": # Se a opção escolhida for 2, o programa solicita a temperatura em Fahrenheit.
        f = float(input("Informe a temperatura em Fahrenheit: ")) # O programa solicita que o usuário informe a temperatura em Fahrenheit e armazena a entrada na variável "f", convertendo-a para um número de ponto flutuante.
        resultado = (f - 32) * 5/9 # O programa realiza a conversão da temperatura de Fahrenheit para Celsius usando a fórmula adequada.
        print(f"{f}°F = {resultado:.2f}°C") # O programa exibe o resultado da conversão em um formato específico, com duas casas decimais.

    else: # Se a opção escolhida pelo usuário não for 0, 1 ou 2, o programa entra no bloco else, indicando que a opção é inválida.
        print("ERRO! Digite uma opção válida!") # Se a opção escolhida pelo usuário não for válida (diferente de 0, 1 ou 2), o programa exibe uma mensagem de erro solicitando que o usuário digite uma opção válida. O programa então continua a execução, permitindo que o usuário escolha uma nova opção.

        