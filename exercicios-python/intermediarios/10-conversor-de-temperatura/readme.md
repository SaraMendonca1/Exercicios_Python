CONVERSOR DE TEMPERATURA

Este é um programa simples em Python que permite converter temperaturas entre as escalas Celsius e Fahrenheit. O sistema funciona em modo interativo via terminal, oferecendo um menu para o usuário escolher o tipo de conversão desejada.

FUNCIONALIDADES
• Conversão de Celsius para Fahrenheit
• Conversão de Fahrenheit para Celsius
• Menu interativo contínuo
• Validação básica de opção do usuário

COMO FUNCIONA
O programa utiliza um loop `while True` para manter a execução contínua até que o usuário escolha a opção de saída.

1. Exibe o menu de opções
2. Recebe a escolha do usuário
3. Executa a conversão correspondente
4. Repete o processo até o usuário selecionar sair

FÓRMULAS UTILIZADAS
• Celsius para Fahrenheit:

  F = (C × 9/5) + 32

• Fahrenheit para Celsius:

  C = (F - 32) × 5/9

COMO EXECUTAR
1. Certifique-se de ter o Python instalado
2. Salve o código em um arquivo, por exemplo, main.py.
3. Execute no terminal:

   python main.py

EXEMPLO DE USO
----- Conversor de temperatura -----
1 - Celsius para Fahrenheit
2 - Fahrenheit para Celsius
0 - Sair

Escolha uma opção: 1
Informe a temperatura em Celsius: 25
25.0°C = 77.00°F

OBSERVAÇÕES
• O programa espera que o usuário digite valores numéricos válidos para temperatura
• Caso seja digitada uma opção inválida no menu, uma mensagem de erro será exibida