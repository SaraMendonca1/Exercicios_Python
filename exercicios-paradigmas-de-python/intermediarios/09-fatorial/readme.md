CÁLCULO DE FATORIAL
Este programa em Python calcula o fatorial de um número inteiro informado pelo usuário. O cálculo é realizado por meio de uma função recursiva.

O fatorial de um número n (representado por n!) é o produto de todos os inteiros positivos de 1 até n. Por definição:

• 0! = 1
• 1! = 1

FUNCIONAMENTO DO CÓDIGO
Função fatorial(n)
A função utiliza recursividade para calcular o fatorial:

• Se n for igual a 0 ou 1, retorna 1.
• Caso contrário, retorna n * fatorial(n - 1).

Entrada de Dados
O usuário deve digitar um número inteiro quando solicitado.

Saída
O programa exibe o valor do fatorial do número informado.

EXEMPLO DE USO
Entrada:
Digite um número: 5

Saída:
O fatorial de 5 é 120

REQUISITOS
• Python 3 instalado

OBSERVAÇÕES
• O programa não trata entradas inválidas (como letras ou números negativos).
• Para evitar erros ou resultados inesperados, utilize apenas números inteiros não negativos.

POSSÍVEIS MELHORIAS
• Adicionar validação de entrada
• Tratar números negativos
• Implementar versão iterativa para comparação com a recursiva