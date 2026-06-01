# Importa o módulo para geração de dados aleatórios
import random
# Importa o módulo que contém grupos de caracteres pré-definidos (letras, números, etc.)
import string

def gerar_senha(comprimento, usar_minusculas, usar_maiusculas, usar_numeros, usar_especiais):
    """
    Função que monta o banco de caracteres permitidos com base nas escolhas
    do usuário e sorteia os caracteres até atingir o comprimento desejado.
    """
    # Inicializa uma string vazia que guardará todos os caracteres possíveis para a senha
    caracteres_permitidos = ""

    # Se o usuário escolheu minúsculas, adiciona 'abcdefghijklmnopqrstuvwxyz'
    if usar_minusculas:
        caracteres_permitidos += string.ascii_lowercase  
        
    # Se escolheu maiúsculas, adiciona 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if usar_maiusculas:
        caracteres_permitidos += string.ascii_uppercase    #        
        
    # Se escolheu números, adiciona '0123456789'
    if usar_numeros: 
        caracteres_permitidos += string.digits    
        
    # Se escolheu especiais, adiciona pontuações e símbolos (ex: !"#$%&'()*+,-./...)
    if usar_especiais:
        caracteres_permitidos += string.punctuation

    # Validação: se a string continuar vazia, significa que o usuário respondeu 'não' para tudo
    if not caracteres_permitidos:
        return "Erro: Nenhum tipo de caractere selecionado."

    # Inicializa uma lista vazia para armazenar cada caractere sorteado
    senha_final = []
    
    # Loop que vai rodar a quantidade de vezes equivalente ao tamanho da senha pedido
    for _ in range(comprimento):
        # Sorteia um único caractere aleatório de dentro do nosso grupo de caracteres permitidos
        caractere_sorteado = random.choice(caracteres_permitidos)
        # Adiciona o caractere sorteado ao final da lista
        senha_final.append(caractere_sorteado)

    # Junta todos os elementos da lista em uma única string e a retorna
    return "".join(senha_final)

# --- Interface do Usuário no Terminal ---
print("--- Gerador de Senhas Aleatórias ---")

# Solicita o tamanho da senha e converte o texto digitado para um número inteiro (int)
tamanho = int(input("Digite o comprimento desejado da senha: "))

# As linhas abaixo fazem a pergunta, convertem a resposta para minúsculo (.lower())
# e checam se é igual a 's'. O resultado será True (verdadeiro) ou False (falso).
incluir_minusculas = input("Incluir letra minusculas? (s/n): ").lower() == 's'
incluir_maiusculas = input("Incluir letras MAIÚSCULAS? (s/n): ").lower() == 's'
incluir_numeros = input("Incluir números? (s/n): ").lower() == 's'
incluir_especiais = input("Incluir caracteres especiais? (s/n): ").lower() == 's'

# Chama a função enviando todas as preferências coletadas e armazena o retorno na variável 'resultado'
resultado = gerar_senha(tamanho, incluir_minusculas, incluir_maiusculas, incluir_numeros, incluir_especiais)

# Exibe o resultado final na tela
print("\nSua senha gerada é:")
print(resultado)