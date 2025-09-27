# Importando as bibliotecas necessárias para a Análise Exploratória de Dados
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

########################################################
# Carregando os dados tratados do ENEM 2019
criarGraficos = pd.read_csv(r"arquivos/tratado_enem_2019")

########################################################
# Criando gráfico de barras para responder:
# Qual a proporção de alunos presentes, faltantes e eliminados ou com presença parcial?

# Contagem das categorias da variável SITUACAO_PRESENCA
contagemGráficoColunas = criarGraficos['SITUACAO_PRESENCA'].value_counts()

# Removendo o nome da série (retira a legenda automática do gráfico)
contagemGráficoColunas.name = None

# Criando instância para plotar o gráfico de colunas verticais
ax = contagemGráficoColunas.plot(kind="bar", legend=False)

# Definindo título do gráfico
plt.title("PROPORÇÃO DE ALUNOS")

# Removendo o rótulo do eixo X
plt.xlabel('')

# Mantendo as categorias do eixo X na horizontal
plt.xticks(rotation=0)

# Inserindo valores absolutos acima das barras
for i, v in enumerate(contagemGráficoColunas):
    ax.text(i, v + 0.1 , str(v), ha='center', fontweight='bold')

########################################################
# Criando histogramas para analisar a distribuição das notas
# Serão comparadas as notas de Redação e Matemática

# Filtrando apenas os alunos presentes
alunosPresentes = criarGraficos[criarGraficos['SITUACAO_PRESENCA'] == "PRESENTE"]

# Definindo o tamanho da figura para os dois histogramas lado a lado
plt.figure(figsize=(12,5))

# Histograma das notas de Redação
plt.subplot(1,2,1)
n, bins, patches = plt.hist(alunosPresentes["NU_NOTA_REDACAO"], bins=5, color='green', edgecolor='black')
plt.title("DISTRIBUIÇÃO DAS NOTAS DE REDAÇÃO")
plt.xlabel("")   # Mantendo rótulo vazio
plt.ylabel("")   # Mantendo rótulo vazio

# Adicionando os valores acima das barras
for i in range(len(patches)):
    plt.text(patches[i].get_x() + patches[i].get_width()/2, patches[i].get_height() + 0.5,
             str(int(patches[i].get_height())), ha='center', fontweight='bold')

# Histograma das notas de Matemática
plt.subplot(1,2,2)
n, bins, patches = plt.hist(alunosPresentes["NU_NOTA_MT"], bins=5, color='blue', edgecolor='black')
plt.title("DISTRIBUIÇÃO DAS NOTAS DE MATEMÁTICA")
plt.xlabel("")   # Mantendo rótulo vazio
plt.ylabel("")   # Mantendo rótulo vazio

# Adicionando os valores acima das barras
for i in range(len(patches)):
    plt.text(patches[i].get_x() + patches[i].get_width()/2, patches[i].get_height() + 0.5,
             str(int(patches[i].get_height())), ha='center', fontweight='bold')

# Ajustando espaçamento entre os gráficos
plt.tight_layout()

########################################################
# Gráfico utilizado para explicar a variação da média por sexo:
# Boxplot
sns.boxplot(x="TP_SEXO", y="MEDIA", data=criarGraficos, showmeans=True,
            meanprops={"marker":"o", "markerfacecolor":"red", "markeredgecolor":"black"})
plt.title("DISTRIBUIÇÃO DAS NOTAS POR SEXO")
max_val = criarGraficos['MEDIA'].max()
min_val = criarGraficos['MEDIA'].min()
plt.ylim(min_val - 10, max_val + 10)
plt.yticks(range(int(min_val), int(max_val)+25, 25))
# Exibindo os gráficos
plt.show()