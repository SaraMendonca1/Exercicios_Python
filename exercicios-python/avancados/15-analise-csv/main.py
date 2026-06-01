# Importa o módulo nativo 'csv', que facilita a leitura e escrita de arquivos com valores separados por vírgula
import csv 
  
def analisar_vendas(nome_arquivo): 
    # Inicializa os acumuladores do relatório: o faturamento total e um dicionário para a contagem de produtos
    total_vendas = 0 
    produtos_vendidos = {} 
  
    # Bloco 'try' inicia o tratamento de erros. Se algo der errado aqui dentro, o Python vai para as exceções no final
    try: 
        # Abre o arquivo CSV em modo leitura ('r') com codificação UTF-8 para evitar problemas com acentos
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_csv: 
            # O DictReader transforma cada linha do CSV em um dicionário, usando a primeira linha (cabeçalho) como chaves
            leitor = csv.DictReader(arquivo_csv) 
            
            # Percorre o arquivo CSV linha por linha
            for linha in leitor: 
                # Extrai os dados da linha usando o nome das colunas definido no cabeçalho
                produto = linha['produto'] 
                quantidade = int(linha['quantidade']) # Converte o texto da quantidade para número inteiro
                preco = float(linha['preco'])         # Converte o texto do preço para número decimal
  
                # Calcula o subtotal (quantidade * preço) e soma ao faturamento total
                total_vendas += quantidade * preco 
                
                # Atualiza a quantidade acumulada do produto no dicionário.
                # O .get(produto, 0) retorna a quantidade atual ou 0 caso o produto ainda não tenha sido registrado.
                produtos_vendidos[produto] = produtos_vendidos.get(produto, 0) + quantidade 
  
        # Após fechar o arquivo, verifica se o dicionário não está vazio (ou seja, se processou alguma venda)
        if produtos_vendidos: 
            # Descobre qual produto teve a maior quantidade vendida. 
            # O 'key=produtos_vendidos.get' faz o Python comparar os valores (quantidades) e não as chaves (nomes)
            produto_mais_vendido = max(produtos_vendidos, key=produtos_vendidos.get) 
            
            # Exibe o relatório de análise formatado no terminal
            print(f"\n--- Análise de Vendas ---") 
            print(f"Total de vendas: R$ {total_vendas:.2f}") # Exibe o faturamento com 2 casas decimais
            print(f"Produto mais vendido: {produto_mais_vendido} ({produtos_vendidos[produto_mais_vendido]} unidades)") 
        else: 
            print("Nenhum dado de vendas encontrado.") 
  
    # --- Tratamento de Erros (Exceções) ---
    
    # Caso o arquivo 'vendas.csv' não exista no diretório atual
    except FileNotFoundError: 
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.") 
    
    # Caso o arquivo CSV não possua as colunas 'produto', 'quantidade' ou 'preco' exatamente como escritas no código
    except KeyError as e: 
        print(f"Erro: Coluna '{e}' não encontrada no arquivo CSV. Verifique o cabeçalho.") 
    
    # Caso o arquivo contenha letras onde deveriam estar números (ex: quantidade igual a "cinco")
    except ValueError as e: 
        print(f"Erro de conversão de dados: {e}. Verifique os valores numéricos no CSV.") 
    
    # Captura qualquer outro erro inesperado que não foi previsto acima
    except Exception as e: 
        print(f"Ocorreu um erro inesperado: {e}")

  
# Chamada da função passando o nome do arquivo que será analisado
analisar_vendas('vendas.csv')