# Caminho do conjunto de dados em formato CSV
caminhoDosDados = r"C:\Users\egber\projetosPython\projeto_final_youth_space\arquivos\MICRODADOS_ENEM_2019.csv"

# Colunas que devem ser excluídas do dataframe
# Motivo: na análise, foram consideradas sem relevância para a tomada de decisão
retirarColunas = [
    "NU_INSCRICAO", "NU_ANO", "CO_MUNICIPIO_ESC", "CO_UF_ESC",
    "CO_MUNICIPIO_PROVA", "NO_MUNICIPIO_ESC", "SG_UF_ESC", "CO_UF_PROVA",
    "CO_PROVA_CN", "CO_PROVA_CH", "TP_SIT_FUNC_ESC",
    "CO_PROVA_LC", "CO_PROVA_MT", "TX_RESPOSTAS_CN", "TX_RESPOSTAS_CH",
    "TX_RESPOSTAS_LC", "TX_RESPOSTAS_MT", "TX_GABARITO_CN", "TX_GABARITO_CH",
    "TX_GABARITO_LC", "TX_GABARITO_MT"
]

# Colunas que devem ter valores ausentes substituídos por zero
# Interpretação: o participante não informou o dado ou sua nota foi zero
colunas_substituir_por_zero = [
    "TP_ENSINO", "TP_DEPENDENCIA_ADM_ESC", "TP_LOCALIZACAO_ESC", "NU_NOTA_CN",
    "NU_NOTA_CH", "NU_NOTA_LC", "NU_NOTA_MT", "TP_STATUS_REDACAO",
    "NU_NOTA_COMP1", "NU_NOTA_COMP2", "NU_NOTA_COMP3", "NU_NOTA_COMP4",
    "NU_NOTA_COMP5", "NU_NOTA_REDACAO"
]

# Colunas que devem ser excluídas no conjunto para classificação
# Motivo: na análise, foram consideradas sem relevância para a tomada de decisão
excluirClassificacao = [
    "NO_MUNICIPIO_PROVA", "SG_UF_PROVA", "TP_PRESENCA_CN", "TP_PRESENCA_CH", "TP_PRESENCA_LC",
    "TP_PRESENCA_MT", "NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_LC", "NU_NOTA_MT",
    "TP_STATUS_REDACAO", "NU_NOTA_COMP1", "NU_NOTA_COMP2", "NU_NOTA_COMP3", "NU_NOTA_COMP4",
    "NU_NOTA_COMP5", "NU_NOTA_REDACAO", "MEDIA"
]

# Colunas que devem ser excluídas no conjunto para regressão
# Motivo: na análise, foram consideradas sem relevância para a tomada de decisão
excluirRegressao = [
    "NO_MUNICIPIO_PROVA", "SG_UF_PROVA", "TP_PRESENCA_CN", "TP_PRESENCA_CH", "TP_PRESENCA_LC",
    "TP_PRESENCA_MT", "NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_LC", "NU_NOTA_MT",
    "TP_STATUS_REDACAO", "NU_NOTA_COMP1", "NU_NOTA_COMP2", "NU_NOTA_COMP3", "NU_NOTA_COMP4",
    "NU_NOTA_COMP5", "NU_NOTA_REDACAO", "SITUACAO_PRESENCA"
]
