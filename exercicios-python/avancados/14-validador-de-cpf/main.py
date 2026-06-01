def validar_cpf(cpf): 
    # Mantém apenas os números da string, removendo pontos, traços e espaços
    cpf = ''.join(filter(str.isdigit, cpf)) 
  
    # Um CPF deve ter exatamente 11 dígitos.
    # Além disso, CPFs com todos os números iguais (ex: 111.111.111-11) 
    # passam no cálculo matemático, mas são considerados inválidos pela Receita Federal.
    if len(cpf) != 11 or len(set(cpf)) == 1: 
        return False 
  
    # --- Validação do primeiro dígito verificador ---
    soma = 0 
    # Multiplica os primeiros 9 dígitos por pesos decrescentes de 10 a 2
    for i in range(9): 
        soma += int(cpf[i]) * (10 - i) 
    
    # O resto da divisão por 11 determina o dígito
    resto = soma % 11 
    # Se o resto for menor que 2, o dígito deve ser 0; caso contrário, é 11 menos o resto
    digito1 = 0 if resto < 2 else 11 - resto 
  
    # Se o primeiro dígito calculado for diferente do que está no CPF, é inválido
    if digito1 != int(cpf[9]): 
        return False 
  
    # --- Validação do segundo dígito verificador ---
    soma = 0 
    # Multiplica os primeiros 10 dígitos (incluindo o que acabamos de validar) 
    # por pesos decrescentes de 11 a 2
    for i in range(10): 
        soma += int(cpf[i]) * (11 - i) 
    
    resto = soma % 11 
    digito2 = 0 if resto < 2 else 11 - resto 
  
    # Se o segundo dígito calculado não bater, o CPF é inválido
    if digito2 != int(cpf[10]): 
        return False 
  
    # Se passou por todos os testes acima, o CPF é matematicamente consistente
    return True 
  
# --- Exemplo de uso ---
cpf_teste = input("Digite um CPF para validar: ") 

# Chama a função e exibe o resultado para o usuário
if validar_cpf(cpf_teste): 
    print(f"O CPF {cpf_teste} é VÁLIDO.") 
else: 
    print(f"O CPF {cpf_teste} é INVÁLIDO.")