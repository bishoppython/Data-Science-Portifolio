# Problema de Negocio
# Você foi contratado como Cientista de Dados da empresa e o meu objetivo foi
# construir uma Máquina Preditiva para prever o Preço de Venda dos carros da empresa.
# Esse processo de previsão vai automatizar e otimizar a definição dos preços
# dos carros que serão vendidos pelo App Instacarro.
# Site: https://www.instacarro.com/

# Importação dos Pacotes :
import pandas as pd     # importação do pacote pandas de manipulação de dados
import numpy as np      # pacote de funções matemáticas
import seaborn as sns   # Gráficos
import warnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt  # pacote de visualização de dados
import openpyxl


df = pd.read_excel('preco-carros.xlsx')
# df # ao utilizar jupyter ou Colab (notebooks)
#print(df) #Exclusivo para Local Machine

# Importando o Pacote Dataprep.eda para Criação de Relatório Personalizado
from dataprep.eda import create_report

# CRIA RELATORIO COM TITULO
report = create_report(df, title='Meu Relatório')

# ao utilizar jupyter ou Colab (notebooks)
# create_report(df)
# create_report

# MOSTRA RELATORIO NO NAVEGADOR (WINDOWS, LINUX)
# para salvá-lo utilize p .save(filename='nome do arquivo', to='~/local do arquivo')
#report.show_browser()

# VERIFICA AS VARIAVEIS (COLUNA-CAMPOS-FEATURES)
colunas = df.columns
print(colunas)
# ao utilizar jupyter ou Colab (notebooks)
# df.columns

# ESCOLHE AS VARIAVEIS E SALVA NO DATASET:
dataset = df[['ano', 'preco_venda', 'preco_atu', 'kms_rodado', 'combustivel', 'tipo_vendendor', 'transmissao', 'proprietario']]

# VISUALIZAR O DATASET:
# ao utilizar jupyter ou Colab (notebooks)
# dataset.head()

# PARA LOCAL MACHINES
M_dataset = dataset.head()
print(M_dataset)

# CRIAÇÃO DE UM CAMPO COM O ANO CORRENTE:
dataset['ano_atu'] = 2022

# CRIAR A NOVA COLUNA - IDADE DO CARRO
dataset['idade'] = dataset['ano_atu']-dataset['ano']

# VISUALIZAR O DATASET:
# ao utilizar jupyter ou Colab (notebooks)
# dataset.head()

# :: PARA LOCAL MACHINES ::
M_dataset = dataset.head()
print(M_dataset)

# ELIMINAR (DROPAR) AS COLUNAS DESNECESSÁRIAS:
# :: PARA LOCAL MACHINES ::
M_dataset = dataset.drop(['ano', 'ano_atu'], axis =1, inplace = True)

M_dataset = dataset.head()
print(M_dataset)
# ao utilizar jupyter ou Colab (notebooks)
# dataset.drop(['ano', 'ano_atu'],axis =1, inplace = True)

# :: TRANSFORMAR CAMPOS TEXTUAIS EM NUMÉRICOS ::
M_dataset = pd.get_dummies(dataset, drop_first = True)

M_dataset = dataset.head()
print(M_dataset)
# ao utilizar jupyter ou Colab (notebooks)
# dataset = pd.get_dummies(dataset, drop_first = True)

# SEPARAÇÃO DAS VARIÁVEIS EXPLICATIVAS E O TARGET (VARIÁVEL QUE QUEREMO PREVER):
''''
X = M_dataset.iloc[:,1:]
y = M_dataset.iloc[:,0]

# SEPARAÇÃO DAS AMOSTRAS PARA TREINAMENTO E TESTE DA MÁQUINA PREDITIVA - TRAIN TEST SPLIT:
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)'''