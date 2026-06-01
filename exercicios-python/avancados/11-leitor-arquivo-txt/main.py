def ler_arquivo(caminho_arquivo): 
    """
    Função para ler e exibir o conteúdo de um arquivo de texto.
    """
    try: 
        # Abre o arquivo para leitura ('r') garantindo o fechamento automático com 'with'
        # O encoding 'utf-8' é usado para suportar caracteres especiais e acentos
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read() # Lê todo o conteúdo do arquivo para a variável
            print("--- Conteúdo do Arquivo ---")
            print(conteudo)
            print("---------------------------")
        
    except FileNotFoundError:
        # Caso o arquivo não exista no diretório especificado
        print(f"Erro: O arquivo {caminho_arquivo} não foi encontrado")
    except Exception as e:
        # Captura qualquer outro erro inesperado (ex: falta de permissão)
        print(f"Ocorreu um erro inesperado: {e}")

# Ponto de entrada do script: garante que o código só rode se executado diretamente
if __name__ == "__main__":
    # Solicita ao usuário o nome ou caminho do arquivo
    nome_do_arquivo = input("Digite o nome do arquivo (ex: dados.txt): ")
    # Chama a função passando o nome fornecido
    ler_arquivo(nome_do_arquivo)