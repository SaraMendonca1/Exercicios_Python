# Importa o módulo nativo 'datetime' para trabalhar com manipulação de datas e horários
import datetime 
  
# Define uma função para registrar logs.
# Ela possui dois parâmetros opcionais (tipo e nome_arquivo) que já vêm com valores padrão.
def registrar_log(mensagem, tipo='INFO', nome_arquivo='app.log'): 
    
    # Obtém a data e hora atual do sistema e a formata como "Ano-Mês-Dia Hora:Minuto:Segundo"
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
    
    # Cria a string que será escrita no arquivo, organizando o timestamp, o tipo do log e a mensagem
    linha_log = f"[{timestamp}] [{tipo}] {mensagem}\n" 
    
    # Abre o arquivo especificado. O modo 'a' (append) garante que o texto será adicionado ao final do arquivo,
    # sem apagar o conteúdo existente. O 'with' garante que o arquivo seja fechado automaticamente após o uso.
    with open(nome_arquivo, 'a', encoding='utf-8') as f: 
        # Escreve a linha de log formatada dentro do arquivo
        f.write(linha_log) 
  
# --- Exemplo de uso da função ---

# Registra uma mensagem informativa padrão (usa o tipo 'INFO' definido no parâmetro)
registrar_log("Aplicação iniciada.", "INFO") 

# Registra um aviso/alerta no log
registrar_log("Variável 'x' não definida.", "WARNING") 

# Registra uma mensagem de erro crítico
registrar_log("Falha na conexão com o banco de dados.", "ERROR") 

# Exibe uma mensagem no console avisando o usuário que os logs foram salvos
print("Logs registrados em 'app.log'.")