import pandas as pd

df = pd.read_csv('dados-clientes.csv')

media_idade, media_renda = df[['Idade', 'Renda']].mean()

cidade_top = df['Cidade'].value_counts().idxmax()

clientes_filtrados = df.query("Renda > 5000")

print(f"Média de Idade: {media_idade:.0f} anos")
print(f"Média de Renda: R$ {media_renda:.2f}")
print(f"Cidade com mais clientes: {cidade_top}")
print(f"\nClientes com renda > 5000:\n{clientes_filtrados}")