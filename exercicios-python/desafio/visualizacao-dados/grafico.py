# Trazendo o Pandas (para ler a tabela) e o Matplotlib (para desenhar a tela)
import pandas as pd
import matplotlib.pyplot as plt

# Lendo o arquivo CSV e guardando na variável 'df'. O 'skipinitialspace' é para ignorar os espaços em branco soltos no arquivo e não dar erro
df = pd.read_csv('dados-cliente.csv', skipinitialspace=True)

# Preparando a aba do aplicativo. 
# plt.subplots(1, 2) corta a tela no meio: 1 linha com 2 colunas. 
# O 'ax1' ganha o controle do lado esquerdo e o 'ax2' do direito. O figsize é a largura x altura da janela inteira.
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))


#quadro da esquerda

# Fazendo a contagem de quantos clientes tem em cada cidade
contagem_cidades = df['Cidade'].value_counts() 

# Desenhando o gráfico de barras (kind='bar') no espaço da esquerda (ax=ax1), pintando de azul com a borda preta
contagem_cidades.plot(kind='bar', ax=ax1, color='skyblue', edgecolor='black')

# Colocando os nomes no título e nos eixos X (embaixo) e Y (do lado)
ax1.set_title('Distribuição de Clientes por Cidade', fontweight='bold')
ax1.set_xlabel('Cidade')
ax1.set_ylabel('Quantidade de Clientes')

# O rotation=0 obriga o nome das cidades a ficar reto na horizontal, impedindo que o gráfico incline o texto pra caber
ax1.tick_params(axis='x', rotation=0) 


#quadro da direita

# Criando o Histograma (kind='hist'). O 'bins=5' agrupa as idades cortando todo mundo em 5 "caixas" iguais. Vai lá pro lado direito (ax=ax2).
df['Idade'].plot(kind='hist', bins=5, ax=ax2, color='lightgreen', edgecolor='black')

# Etiquetando o gráfico da direita pra quem for ver entender o que é
ax2.set_title('Distribuição de Idades', fontweight='bold')
ax2.set_xlabel('Idade')
ax2.set_ylabel('Frequência')


# exibição

# O "tight_layout" arruma as margens sozinho pra um gráfico não ficar com texto sobreposto no outro
plt.tight_layout()

# pausa o script aqui, renderiza tudo e joga a janela visual na tela do computador
plt.show()