# Importando as bibliotecas necessárias para a Análise Exploratória de Dados
import matplotlib.pyplot as plt
import seaborn as sns
from variaveis import tratados_DF, regressao_DF, faixaSalarial, normalizado_regressao_DF

########################################################

# Filtrando apenas os alunos presentes para criar um novo dataframe
alunosPresentes = tratados_DF[tratados_DF['SITUACAO_PRESENCA'] == "PRESENTE"]

########################################################
# Criando gráfico de barras para mostrar a proporção de alunos
# por situação de presença (Presente, Faltante, Eliminado/Parcial)

# Contagem das categorias da variável SITUACAO_PRESENCA
contagemGráficoColunas = tratados_DF['SITUACAO_PRESENCA'].value_counts()

# Removendo o nome da série (evita legenda automática)
contagemGráficoColunas.name = None

# Criando instância para plotar o gráfico de colunas verticais
plt.figure(figsize=(6,4))
ax = contagemGráficoColunas.plot(kind="bar", legend=False)

# Definindo título do gráfico
plt.title("DISTRIBUIÇÃO DOS ALUNOS POR SITUAÇÃO DE PRESENÇA")

# Removendo o rótulo do eixo X
plt.xlabel('')

# Mantendo as categorias do eixo X na horizontal
plt.xticks(rotation=0)

# Inserindo valores absolutos acima das barras
for i, v in enumerate(contagemGráficoColunas):
    ax.text(i, v + 0.1 , str(v), ha='center', fontweight='bold')

########################################################
# Criando histogramas para analisar a distribuição das notas
# Comparando as notas de Redação e Matemática

# Definindo tamanho da figura para os dois histogramas lado a lado
plt.figure(figsize=(12,5))

# Histograma das notas de Redação
plt.subplot(1,2,1)
n, bins, patches = plt.hist(alunosPresentes["NU_NOTA_REDACAO"], bins=5, color='green', edgecolor='black')
plt.title("DISTRIBUIÇÃO DAS NOTAS DE REDAÇÃO")
plt.xlabel("")  # Mantendo rótulo vazio
plt.ylabel("")  # Mantendo rótulo vazio

# Adicionando os valores acima das barras do histograma de Redação
for i in range(len(patches)):
    plt.text(patches[i].get_x() + patches[i].get_width()/2, patches[i].get_height() + 0.5,
             str(int(patches[i].get_height())), ha='center', fontweight='bold')

# Histograma das notas de Matemática
plt.subplot(1,2,2)
n, bins, patches = plt.hist(alunosPresentes["NU_NOTA_MT"], bins=5, color='blue', edgecolor='black')
plt.title("DISTRIBUIÇÃO DAS NOTAS DE MATEMÁTICA")
plt.xlabel("")  # Mantendo rótulo vazio
plt.ylabel("")  # Mantendo rótulo vazio

# Adicionando os valores acima das barras do histograma de Matemática
for i in range(len(patches)):
    plt.text(patches[i].get_x() + patches[i].get_width()/2, patches[i].get_height() + 0.5,
             str(int(patches[i].get_height())), ha='center', fontweight='bold')

# Ajustando espaçamento entre os gráficos
plt.tight_layout()

########################################################
# Boxplot para analisar a variação da média por sexo
plt.figure(figsize=(6,4))
sns.boxplot(x="TP_SEXO", y="MEDIA", data=tratados_DF, showmeans=True,
            meanprops={"marker":"o", "markerfacecolor":"red", "markeredgecolor":"black"})
plt.title("DESEMPENHO POR SEXO")

# Definindo limites e intervalos do eixo Y
max_val = tratados_DF['MEDIA'].max()
min_val = tratados_DF['MEDIA'].min()
plt.ylim(min_val - 10, max_val + 10)
plt.yticks(range(int(min_val), int(max_val)+25, 25))

########################################################
# Boxplot para analisar a variação da média por tipo de instituição
plt.figure(figsize=(6,4))
sns.boxplot(x="TP_DEPENDENCIA_ADM_ESC", y="MEDIA", data=alunosPresentes, showmeans=True,
            meanprops={"marker":"o", "markerfacecolor":"red", "markeredgecolor":"black"})
plt.title("DESEMPENHO POR TIPO DE INSTITUIÇÃO")

# Definindo limites e intervalos do eixo Y
max_val = alunosPresentes['MEDIA'].max()
min_val = alunosPresentes['MEDIA'].min()
plt.ylim(min_val - 10, max_val + 10)
plt.yticks(range(int(min_val), int(max_val)+25, 25))

########################################################
# Substituindo códigos da coluna Q006 por faixas salariais usando o mapeamento definido em faixaSalarial
alunosPresentes["Faixa_Salarial"] = alunosPresentes["Q006"].map(faixaSalarial)

# Agrupando por faixa salarial e calculando a média das notas para cada faixa
dados_plot = alunosPresentes.groupby("Faixa_Salarial")["MEDIA"].mean().sort_values(ascending=False).reset_index()

# Plotando gráfico horizontal das médias por faixa salarial
plt.figure(figsize=(10,8))
ax = sns.barplot(y="Faixa_Salarial", x="MEDIA", data=dados_plot, ci=None, palette="viridis", orient="h")

# Adicionando valores da média ao final de cada barra
for i, v in enumerate(dados_plot["MEDIA"]):
    ax.text(v + 0.05, i, f"{v:.2f}", va="center")

plt.title("DESEMPENHO POR FAIXA SALARIAL")
plt.xlabel(" ")
plt.ylabel(" ")

# Exibindo o gráfico
plt.show()

########################################################
# Calculando a correlação entre a média das notas e a faixa etária dos alunos
correlacao = alunosPresentes['MEDIA'].corr(alunosPresentes['TP_FAIXA_ETARIA'])
print(correlacao)

########################################################
# Analisando quais preditores (features) têm correlação com a média das notas usando um mapa de calor

# Calcula a correlação da coluna MEDIA com todas as outras variáveis do dataframe normalizado
correlacao_regressao = normalizado_regressao_DF.corr()["MEDIA"].drop("MEDIA")

# Ordenando os valores de correlação em ordem decrescente
correlacao_ordenada = correlacao_regressao.sort_values(ascending=False)

# Gerando arquivo CSV com as correlações ordenadas
correlacao_ordenada.to_frame().to_csv("correlacao_desempenho.csv", index=True)

# Criando mapa de calor vertical para melhor visualização das correlações
plt.figure(figsize=(4, 10))
sns.heatmap(correlacao_regressao.to_frame(), annot=True, cmap="coolwarm", center=0, linewidths=0.5)
plt.title("CORRELAÇÃO DOS PREVISORES COM O DESEMPENHO")
plt.show()
