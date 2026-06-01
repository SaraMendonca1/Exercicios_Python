#Trazendo a caixa de ferramentas do Pandas e dando o apelido de 'pd'
import pandas as pd

#Lendo o arquivo CSV do meu computador e guardando nessa variável 'df' )
df = pd.read_csv('dados-clientes.csv')

#Calculando a média de duas colunas ao mesmo tempo pra economizar linha de código
media_idade, media_renda = df[['Idade', 'Renda']].mean()

# Pegando a coluna 'Cidade', contando qual aparece mais e extraindo só o nome dela (.idxmax())
cidade_top = df['Cidade'].value_counts().idxmax()

# Fazendo um filtro rápido: quero apenas as linhas onde a renda for maior que 5 mil
clientes_filtrados = df.query("Renda > 5000")

# Mostrando os resultados na tela (o :.0f tira as casas decimais da idade, e o :.2f deixa a renda com cara de dinheiro)
print(f"Média de Idade: {media_idade:.0f} anos")
print(f"Média de Renda: R$ {media_renda:.2f}")
print(f"Cidade com mais clientes: {cidade_top}")
print(f"\nClientes com renda > 5000:\n{clientes_filtrados}")