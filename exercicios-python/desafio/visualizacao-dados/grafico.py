import pandas as pd
import matplotlib.pyplot as plt

# 1. Carregando os dados e limpando os espaços ocultos do CSV
df = pd.read_csv('dados-cliente.csv', skipinitialspace=True)

# 2. Técnica Avançada: Criando uma "tela" (fig) e dois espaços para gráficos (ax1, ax2)
# figsize=(12, 5) define a largura e altura da janela em polegadas
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# --- GRÁFICO 1: Barras (Clientes por Cidade) no espaço ax1 ---
contagem_cidades = df['Cidade'].value_counts() 
# Usamos os próprios recursos do Pandas plotar dentro do eixo ax1
contagem_cidades.plot(kind='bar', ax=ax1, color='skyblue', edgecolor='black')

ax1.set_title('Distribuição de Clientes por Cidade', fontweight='bold')
ax1.set_xlabel('Cidade')
ax1.set_ylabel('Quantidade de Clientes')
ax1.tick_params(axis='x', rotation=0) # Deixa os nomes das cidades na horizontal

# --- GRÁFICO 2: Histograma (Distribuição de Idades) no espaço ax2 ---
# bins=5 define em quantos "blocos" de idade o gráfico será dividido
df['Idade'].plot(kind='hist', bins=5, ax=ax2, color='lightgreen', edgecolor='black')

ax2.set_title('Distribuição de Idades', fontweight='bold')
ax2.set_xlabel('Idade')
ax2.set_ylabel('Frequência')

# 3. Ajustando o layout para nada ficar sobreposto e exibindo a janela
plt.tight_layout()
plt.show()