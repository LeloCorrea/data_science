'''
Desafio: Previsão do valor do imóvel.
Objetivo: Prever o valor de imóveis de uma determinada cidade através de uma tecnologia.



Esses comandos na verdade não são exclusivos do colaboratory, os mesmos comandos funcionam no Jupyter notebook local, no vscode, no Pycharm.

# 1 - Importando os módulos para (Leitura de um arquivo xlsx):
import pandas as pd
import numpy as np

# 2 - Lendo os arquivos excel:
#df = pd.read_excel(' caminho do arquivo excel ', index_col=None, header=None)

# 3 - Visualizando os dados:
# df.head()
'''
# ---

# Semana de Ciência de Dados
# Minerando Dados

# Conhecendo a base de dados
#Importando como bibliotecas básicas:
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

#Carregando a base de dados:

#Carrega a dataset de boston
from sklearn.datasets import load_boston
boston = load_boston()

#Descrição do dataset
print (boston.DESCR)

#cria um dataframe pandas
data = pd.DataFrame(boston.data, columns=boston.feature_names)

#Imprime as 5 primeiras linhas do dataset
data.head()

#Escreve o arquivo para o disco
data.to_csv('data.csv')

'''
Conhecendo as colunas da base de dados:

CRIM: Taxa de criminalidade per capita por região.

ZN: Proporção de terrenos residenciais divididos por lotes com mais de 25.000 pés quadrados.

INDUS: Essa é a proporção de hectares de negócios não comerciais na região.

CHAS: Variável fictícia  Charles River (=1 se o trecho limita o rio; 0 caso contrário).

NOX: concentração de óxido nítrico (partes por 10 milhões)

RM: Número médio de quartos entre as casas do bairro

Age: proporção de unidades ocupadas pelos proprietários construídas antes de 1940

DIS: distâncias ponderadas para cinco centros de emprego em Boston

RAD: Índice de acessibilidade às rodovias radiais

IMPOSTO: taxa do imposto sobre a propriedade de valor total por US $ 10.000

B: 1000 (Bk - 0,63) ², onde Bk é a proporção de pessoas de descendência afro-americana por regiao

PTRATIO: Bairros com maior proporção de alunos para professores (maior valor de 'PTRATIO')

LSTAT: porcentagem de status mais baixo da população

MEDV: valor médio de casas ocupadas pelos proprietários em US $ 1000
'''

#Adicionando a coluna que será nossa variável alvo

#Adiciona a variavel MEDV
data['MEDV'] = boston.target

#Imprime as 5 primeiras linhas do dataframe
data.head()

data.describe()

#Análise e exploração dos dados.

#Nesta etapa nosso objetivo é conhecer os dados que estamos trabalhando.

#Podemos utilizar a ferramenta PANDAS PROFILING para esta etapa:

# instalando o pandas profiling
#!pip install https://github.com/pandas-profiling/pandas-profiling/archive/master.zip

#import o ProfileReport
from pandas_profiling import ProfileReport

#Executando o profile
profile = ProfileReport(data, title='Relatório - Pandas Profiling', html={'style':{'full_width':True}})

profile

'''
Observações

O coeficiente de correlação varia de -1 a 1. Se valor é próximo de 1, isto significa que existe uma forte correlação positiva entre as variáveis. Quando esse número é próximo de -1, as variáveis tem uma forte correlação negativa.

A relatório que executamos acima nos mostra que a nossa variável alvo (MEDV) é fortemente correlacionada com as variáveis LSTAT e RM

RAD e TAX são fortemente correlacionadas, podemos remove-las do nosso modelo para evitar a multi-colinearidade.

O mesmo acontece com as colunas DIS and AGE a qual tem a correlação de -0.75

A coluna ZN possui 73% de valores zero.
'''

#Salvando o relatório no disco:
profile.to_file(output_file="Relatorio01.html")