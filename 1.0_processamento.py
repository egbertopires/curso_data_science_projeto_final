# PROJETO FINAL - YOUTHSPACE
# CURSO: CIÊNCIA DE DADOS

########################################################

# Importando as bibliotecas pandas e numpy
import pandas as pd
import numpy as np

# Importando do módulo variáveis:
# caminhoDosDados, retirarColunas, colunas_substituir_por_zero,
# excluirClassificacao e excluirRegressao
from variaveis import (caminhoDosDados, retirarColunas, colunas_substituir_por_zero,
                       excluirClassificacao, excluirRegressao)

# Criação do dataframe enemDF.
# Parâmetros utilizados para ler o conjunto de dados:
# encoding='latin1', sep=";"
enemDF = pd.read_csv(caminhoDosDados, encoding='latin1', sep=";")

# Eliminando colunas desnecessárias (lista definida no módulo variáveis)
enemDF = enemDF.drop(retirarColunas, axis=1)

# Substituindo valores ausentes por zero
# (colunas definidas no módulo variáveis)
enemDF[colunas_substituir_por_zero] = enemDF[colunas_substituir_por_zero].fillna(0)

# Criando as colunas SITUACAO_PRESENCA e MEDIA
# SITUACAO_PRESENCA: classifica em AUSENTE, PRESENTE ou ELIMINADO/PRESENÇA PARCIAL
# MEDIA: calcula a média das quatro provas objetivas e da redação
enemDF["SITUACAO_PRESENCA"] = np.select(
    [enemDF.iloc[:, 14:(17+1)].sum(axis=1) == 0,
             enemDF.iloc[:, 14:(17+1)].sum(axis=1) == 4],
    ["AUSENTE",
             "PRESENTE"],
    default="ELIMINADO OU PRESENÇA PARCIAL"
)

# Criando a coluna MEDIA
# A lista criada com range facilita o agrupamento de colunas para o cálculo
enemDF["MEDIA"] = enemDF.iloc[:, list(range(18, (21+1))) + [29]].mean(axis=1)


# A partir deste ponto, o conjunto de dados está pronto para ser dividido
# e atender aos critérios do projeto.
# O dataframe enemDF servirá como base para criação de dashboards no Power BI
# e para geração de conjuntos destinados a classificação e regressão.

# Criando o dataset tratado_enem_2019_
# Contém a base original do ENEM 2019 pré-processada
# Ideal para reutilização em trabalhos futuros
enemDF.to_csv("tratado_enem_2019", index=False)

# Criando o conjunto de dados para classificação
# Excluindo colunas desnecessárias (lista definida no módulo variáveis)
classificacaoEnemDF = enemDF.loc[enemDF['SITUACAO_PRESENCA'] != 'ELIMINADO OU PRESENÇA PARCIAL'\
                                ].drop(excluirClassificacao, axis=1)

# Criando o conjunto de dados para regressão
# Excluindo colunas desnecessárias (lista definida no módulo variáveis)
regressaoEnemDF = enemDF.loc[enemDF['SITUACAO_PRESENCA'] == 'PRESENTE'\
                                ].drop(excluirRegressao, axis=1)

# Salvando os datasets em arquivos CSV
# Os arquivos gerados estão na pasta arquivos.

classificacaoEnemDF.to_csv("classificacao_enem_2019", index=False)
regressaoEnemDF.to_csv("regressao_enem_2019", index=False)
