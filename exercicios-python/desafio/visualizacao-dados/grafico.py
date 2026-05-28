import pandas as pd
import matplotlib.pyplot as plt

#solicitando que a biblioteca panda leia o arquivo CSV// ignora espaços iniciais incluido nos dados
df = pd.read_csv('dados-cliente.csv', skipinitialspace=True)

#configurando design da tabela
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

#configurando os dados da cidade no gráfico esquerdo
contagem_cidades = df['Cidade'].value_counts() 
contagem_cidades.plot(kind='bar', ax=ax1, color='skyblue', edgecolor='black')

ax1.set_title('Distribuição de Clientes por Cidade', fontweight='bold')
ax1.set_xlabel('Cidade')
ax1.set_ylabel('Quantidade de Clientes')
ax1.tick_params(axis='x', rotation=0) #impedindo que o grafico incline o texto caso ele for muito grande

#configurando histograma de idades 
df['Idade'].plot(kind='hist', bins=5, ax=ax2, color='lightgreen', edgecolor='black')

ax2.set_title('Distribuição de Idades', fontweight='bold')
ax2.set_xlabel('Idade')
ax2.set_ylabel('Frequência')

# 3. Ajustando o layout paranão ficar sobreposto e exibindo a janela
plt.tight_layout()
plt.show()