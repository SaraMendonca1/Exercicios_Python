GERENCIADOR DE LISTA DE CONTATOS
Este é um script Python simples para gerenciar uma lista de contatos via terminal. O projeto permite cadastrar, visualizar e excluir contatos, utilizando conceitos básicos de listas, dicionários e estruturas de repetição.

FUNCIONALIDADES
O programa oferece um menu interativo com as seguintes opções:

• Adicionar novo contato: Permite inserir o nome, telefone e e-mail de uma pessoa.

• Exibir lista de contatos: Lista todos os contatos salvos no momento.

• Excluir contato: Remove um contato da lista buscando pelo nome exato.

• Sair: Encerra a execução do programa.

TECNOLOGIAS UTILIZADAS
•Python 3.10+

COMO EXECUTAR
1. Certifique-se de ter o Python instalado em sua máquina.

2. Copie o código para um arquivo chamado, por exemplo, main.py.

3. Abra o terminal ou prompt de comando na pasta onde o arquivo foi salvo.

4. Execute o comando:

python main.py

EXEMPLO DE USO
Ao iniciar o programa, você verá o seguinte menu:

----- CONTATOS -----
1 - Adicionar novo contato
2 - Exibir lista de contatos
3 - Excluir contato
0 - Sair
Digite a opção desejada:


REGRAS DE NEGÓCIO
Os dados são armazenados em uma lista de dicionários na memória RAM (os dados serão perdidos ao fechar o programa).

A exclusão é feita comparando o nome digitado com o nome cadastrado (case-sensitive).