CONTADOR DE VOGAIS EM PYTHON
Este é um script simples em Python que solicita uma palavra ao usuário e realiza a contagem de todas as vogais presentes, incluindo caracteres com acentuação (acentos agudos, circunflexos, tis e graves).

COMO FUNCIONA
O programa percorre cada letra da string fornecida e verifica se ela pertence a um conjunto predefinido de vogais da língua portuguesa.

1. Entrada: O usuário digita uma palavra ou frase.

2. Processamento: O texto é convertido para letras minúsculas (.lower()) para garantir que letras maiúsculas também sejam contadas.

3. Verificação: Um laço for itera sobre a string, comparando cada caractere com a lista: aeiouáéíóúâêîôûãõàèìòù.

4. Saída: Exibe o total acumulado no console.

TECNOLOGIAS UTILIZADAS
• Python 3

• Lógica de iteração e manipulação de strings.

EXEMPLO DE USO

palavra = input("Digite uma palavra: ").lower()
contador = 0

for letra in palavra:
    if letra in "aeiouáéíóúâêîôûãõàèìòù":
        contador += 1

print(f"Quantidade de vogais em {palavra}: {contador}")

Resultado esperado no terminal:

Digite uma palavra: Programação

Quantidade de vogais em programação: 5

COMO EXECUTAR
1. Certifique-se de ter o Python instalado em sua máquina.

2. Salve o código em um arquivo chamado main.py.

3. Abra o terminal ou prompt de comando.

4. Execute o comando:

python main.py