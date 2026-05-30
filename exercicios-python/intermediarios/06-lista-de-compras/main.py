compras= [] # O programa inicia criando uma lista vazia chamada "compras", que será utilizada para armazenar os itens da lista de compras do usuário.
while True: # O programa entra em um loop infinito utilizando a estrutura while True, o que significa que o programa continuará executando até que seja explicitamente interrompido por um break.
    print("-"*5, "COMPRAS", "-"*5) # O programa exibe um título "COMPRAS" cercado por uma linha de caracteres "-" para destacar a seção de compras.
    print("1 - Adicionar itens") # O programa exibe a opção "1 - Adicionar itens" para informar ao usuário que ele pode escolher essa opção.
    print("2 - Exibir lista") # O programa exibe a opção "2 - Exibir lista" para informar ao usuário que ele pode escolher essa opção.
    print("3 - Excluir item") # O programa exibe a opção "3 - Excluir item" para informar ao usuário que ele pode escolher essa opção.
    print("0 - Sair") # O programa exibe a opção "0 - Sair" para informar ao usuário que ele pode escolher essa opção.

    opcao= input("Digite a opção desejada:") # O programa solicita que o usuário digite a opção desejada e armazena a entrada na variável "opcao". A função input() é utilizada para capturar a entrada do usuário como uma string, permitindo que o programa processe a escolha do usuário.
    if opcao=="0": # O programa verifica se a opção digitada pelo usuário é "0", o que indica que o usuário deseja sair do programa. Se a condição for verdadeira, o programa executa o código dentro do bloco if.
        print("Fim do programa!") # Se a condição if for verdadeira, o programa exibe a mensagem "Fim do programa!".  
        break # O comando break é utilizado para sair do loop while, encerrando a execução do programa.

    if opcao in ["1","2","3"]: # O programa verifica se a opção digitada pelo usuário é uma das opções válidas ("1", "2" ou "3"). Se a condição for verdadeira, o programa executa o código dentro do bloco if.
        try: # O programa é envolvido em um bloco try-except para lidar com possíveis erros de entrada, como o usuário digitar um valor que não seja um número inteiro.
            match int(opcao): # O programa utiliza a estrutura match-case para comparar a opção digitada pelo usuário (convertida para um número inteiro) com os casos definidos. A função int() é utilizada para converter a entrada do usuário em um número inteiro.
                case 1: # Se a opção digitada pelo usuário for "1", o programa executa o código dentro do bloco case 1.
                    item=input("Insira o nome do item: ") # O programa solicita que o usuário insira o nome do item a ser adicionado à lista de compras e armazena a entrada na variável "item". A função input() é utilizada para capturar a entrada do usuário como uma string, permitindo que o programa processe o nome do item.
                    compras.append(item) # O programa adiciona o item digitado pelo usuário à lista de compras utilizando o método append(). O método append() é utilizado para adicionar um elemento ao final da lista, permitindo que o programa mantenha um registro dos itens adicionados à lista de compras.
                    print(f"{item} adicionado a lista") # O programa exibe uma mensagem confirmando que o item foi adicionado à lista de compras, utilizando f-strings para formatar a saída e incluir o nome do item adicionado.
                case 2: # Se a opção digitada pelo usuário for "2", o programa executa o código dentro do bloco case 2.
                    if len(compras)==0: # O programa verifica se a lista de compras está vazia utilizando a função len() para obter o número de elementos na lista. Se o resultado for igual a 0, significa que a lista está vazia, e o programa executa o código dentro do bloco if.
                        print("Lista de compras vazia.") # Se a condição if for verdadeira, o programa exibe a mensagem "Lista de compras vazia." para informar ao usuário que não há itens na lista de compras.
                    else: # Se a condição if for falsa, ou seja, se a lista de compras não estiver vazia, o programa executa o código dentro do bloco else.
                        print("--- LISTA DE COMPRAS ---") # O programa exibe o título "--- LISTA DE COMPRAS ---" para indicar que a próxima seção exibirá os itens da lista de compras. 
                        for i, item in enumerate(compras, 1): # O programa utiliza um loop for para iterar sobre os itens da lista de compras, utilizando a função enumerate() para obter tanto o índice (i) quanto o valor do item. O segundo argumento da função enumerate() é 1, o que significa que a contagem dos índices começará em 1 em vez de 0, proporcionando a enumeração dos itens adicionados.
                            print(f"{i}. {item}") # O programa exibe cada item da lista de compras em um formato específico. A expressão f"{i}. {item}" utiliza f-strings para formatar a saída, exibindo o índice do item (i) seguido pelo nome do item (item).
                        print("-"*25) # O programa exibe uma linha de 25 caracteres "-" para separar visualmente a lista de compras exibida.
                case 3: # Se a opção digitada pelo usuário for "3", o programa executa o código dentro do bloco case 3.
                    excluir=input("Digite o nome do item a ser excluído: ") # O programa solicita que o usuário digite o nome do item a ser excluído da lista de compras e armazena a entrada na variável "excluir". A função input() é utilizada para capturar a entrada do usuário como uma string, permitindo que o programa processe o nome do item a ser excluído.
                    if excluir in compras: # O programa verifica se o item digitado pelo usuário para exclusão está presente na lista de compras utilizando o operador in. Se a condição for verdadeira, significa que o item está na lista, e o programa executa o código dentro do bloco if.
                        compras.remove(excluir) # O programa remove o item digitado pelo usuário da lista de compras utilizando o método remove(). 
                        print(f"{excluir} excluído da lista!") # O programa exibe uma mensagem confirmando que o item foi excluído da lista de compras, utilizando f-strings para formatar a saída e incluir o nome do item excluído.
                    else: # Se a condição if for falsa, ou seja, se o item digitado pelo usuário para exclusão não estiver presente na lista de compras, o programa executa o código dentro do bloco else.
                        print(f"{excluir} não encontrado na lista") # O programa exibe uma mensagem informando que o item digitado pelo usuário para exclusão não foi encontrado na lista de compras, utilizando f-strings para formatar a saída e incluir o nome do item que não foi encontrado.

        except ValueError: # Se o usuário digitar um valor que não possa ser convertido para um número inteiro, como uma string ou um número decimal, o programa irá gerar uma exceção do tipo ValueError. O bloco except captura essa exceção e executa o código dentro dele.
            print("Erro! Tente novamente") # Se uma exceção do tipo ValueError for capturada, o programa exibe a mensagem "Erro! Tente novamente" para informar ao usuário que a entrada foi inválida e que ele deve tentar novamente digitando uma opção válida.
    else: # Se a condição if for falsa, ou seja, se a opção digitada pelo usuário não for "0", "1", "2" ou "3", o programa executa o código dentro do bloco else.
        print("Digite apenas as opções válidas") # O programa exibe a mensagem "Digite apenas as opções válidas" para informar ao usuário que a opção digitada não é válida e que ele deve digitar uma opção válida para continuar utilizando o programa.


