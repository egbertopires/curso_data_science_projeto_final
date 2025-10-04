# Importando o pandas
import pandas as pd

########################################################

# Caminho do conjunto de dados em formato CSV
caminhoDosDados = r"C:\Users\egber\projetosPython\projeto_final_youth_space\arquivos\MICRODADOS_ENEM_2019.csv"

########################################################

# Colunas que devem ser excluídas do dataframe
# Motivo: consideradas sem relevância para a análise
retirarColunas = [
    "NU_INSCRICAO", "NU_ANO", "CO_MUNICIPIO_ESC", "CO_UF_ESC",
    "CO_MUNICIPIO_PROVA", "NO_MUNICIPIO_ESC", "SG_UF_ESC", "CO_UF_PROVA",
    "CO_PROVA_CN", "CO_PROVA_CH", "TP_SIT_FUNC_ESC",
    "CO_PROVA_LC", "CO_PROVA_MT", "TX_RESPOSTAS_CN", "TX_RESPOSTAS_CH",
    "TX_RESPOSTAS_LC", "TX_RESPOSTAS_MT", "TX_GABARITO_CN", "TX_GABARITO_CH",
    "TX_GABARITO_LC", "TX_GABARITO_MT"
]

########################################################

# Colunas que devem ter valores ausentes substituídos por zero
# Interpretação: o participante não informou o dado ou a nota é zero
colunas_substituir_por_zero = [
    "TP_ENSINO", "TP_DEPENDENCIA_ADM_ESC", "TP_LOCALIZACAO_ESC", "NU_NOTA_CN",
    "NU_NOTA_CH", "NU_NOTA_LC", "NU_NOTA_MT", "TP_STATUS_REDACAO",
    "NU_NOTA_COMP1", "NU_NOTA_COMP2", "NU_NOTA_COMP3", "NU_NOTA_COMP4",
    "NU_NOTA_COMP5", "NU_NOTA_REDACAO"
]

########################################################

# Colunas a serem excluídas para o conjunto de classificação
# Motivo: consideradas sem relevância para a análise
excluirClassificacao = [
    "NO_MUNICIPIO_PROVA", "SG_UF_PROVA", "TP_PRESENCA_CN", "TP_PRESENCA_CH", "TP_PRESENCA_LC",
    "TP_PRESENCA_MT", "NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_LC", "NU_NOTA_MT",
    "TP_STATUS_REDACAO", "NU_NOTA_COMP1", "NU_NOTA_COMP2", "NU_NOTA_COMP3", "NU_NOTA_COMP4",
    "NU_NOTA_COMP5", "NU_NOTA_REDACAO", "MEDIA"
]

########################################################

# Colunas a serem excluídas para o conjunto de regressão
# Motivo: consideradas sem relevância para a análise
excluirRegressao = [
    "NO_MUNICIPIO_PROVA", "SG_UF_PROVA", "TP_PRESENCA_CN", "TP_PRESENCA_CH", "TP_PRESENCA_LC",
    "TP_PRESENCA_MT", "NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_LC", "NU_NOTA_MT",
    "TP_STATUS_REDACAO", "NU_NOTA_COMP1", "NU_NOTA_COMP2", "NU_NOTA_COMP3", "NU_NOTA_COMP4",
    "NU_NOTA_COMP5", "NU_NOTA_REDACAO", "SITUACAO_PRESENCA"
]

########################################################

# Dicionário para substituir códigos do Q6 por faixas salariais
faixaSalarial = {
    "A": "Nenhuma",
    "B": "Até 998",
    "C": "998–1.497",
    "D": "1.497–1.996",
    "E": "1.996–2.495",
    "F": "2.495–2.994",
    "G": "2.994–3.992",
    "H": "3.992–4.990",
    "I": "4.990–5.988",
    "J": "5.988–6.986",
    "K": "6.986–7.984",
    "L": "7.984–8.982",
    "M": "8.982–9.980",
    "N": "9.980–11.976",
    "O": "11.976–14.970",
    "P": "14.970–19.960",
    "Q": "Mais de 19.960"
}

########################################################

# Leitura do dataframe tratado (pré-processado para análise)
tratados_DF = pd.read_csv(r"arquivos/tratado_enem_2019")

#######################################################

# Leitura do dataframe para regressão
regressao_DF = pd.read_csv(r"arquivos/regressao_enem_2019")

# ########################################################

# Leitura do dataframe para classificação
classificacao_DF = pd.read_csv(r"arquivos/classificacao_enem_2019")

# ########################################################

# Leitura do dataframe para classificação ausentes
classificacao_ausentes_DF = pd.read_csv(r"arquivos/ausentes_DF_normalizado.csv")

# ########################################################

# Criando uma iteração para a criação de instâncias LabelEnconder

# Criando uma lista com os nomes de todas as colunas
listandoColunasTratadas = regressao_DF.columns.to_list()

textoUm = ''
textoDois = ''

# Iterando para verificar quais colunas são qualitativas
indiceRegressao = 0
for nomeColuna in listandoColunasTratadas:
    if regressao_DF[nomeColuna].dtype == "object":
        textoUm += f'LabelEncoder_{nomeColuna} = LabelEncoder()\n'
        textoDois += f'quantitativo_regressao[:,{indiceRegressao}] = LabelEncoder_{nomeColuna}.fit_transform(quantitativo_regressao[:,{indiceRegressao}])\n'
    indiceRegressao += 1

laberRegressao = f'{textoUm}\n{textoDois}'

# Criando um arquivo de texto com os dados da iteração
with open("arquivos/laberRegressao.txt", "w", encoding="utf-8") as f:
    f.write(str(laberRegressao))

#######################################################

# Leitura do dataframe para criação do mapa de calor
normalizado_regressao_DF = pd.read_csv(r"C:\Users\egber\projetosPython\projeto_final_youth_space\arquivos\regressao_DF_normalizado.csv")

#######################################################
# Criando uma iteração para a criação de instâncias LabelEnconder

# Criando uma lista com os nomes de todas as colunas
listandoColunasTratadas = classificacao_DF.columns.to_list()

textoUm = ''
textoDois = ''

# Iterando para verificar quais colunas são qualitativas
indiceClassificacao = 0
for nomeColuna in listandoColunasTratadas:
    if classificacao_DF[nomeColuna].dtype == "object":
        textoUm += f'LabelEncoder_{nomeColuna} = LabelEncoder()\n'
        textoDois += f'quantitativo_classificacao[:,{indiceClassificacao}] = LabelEncoder_{nomeColuna}.fit_transform(quantitativo_classificacao[:,{indiceClassificacao}])\n'
    indiceClassificacao += 1

laberClassificacao = f'{textoUm}\n{textoDois}'

# Criando um arquivo de texto com os dados da iteração
with open("arquivos/laberClassificacao.txt", "w", encoding="utf-8") as f:
    f.write(str(laberClassificacao))