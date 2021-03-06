#Machine Learning e Deploy

{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "anaconda-cloud": {},
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.6.5"
    },
    "colab": {
      "name": "aula03.ipynb",
      "provenance": [],
      "collapsed_sections": []
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "GFJ4EVNomx-9",
        "colab_type": "text"
      },
      "source": [
        "## **Semana de Data Science**\n",
        "\n",
        "- Minerando Dados"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "4vhNe3CadOcI",
        "colab_type": "text"
      },
      "source": [
        "### Conhecendo a base de dados"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "UIKcG9cuf73S",
        "colab_type": "text"
      },
      "source": [
        "Monta o drive"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Pra_pLjfAW3d",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "LpI7iiKFVv85",
        "colab_type": "text"
      },
      "source": [
        "Importando as bibliotecas básicas"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "KrCFI6wjVy8r",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import pandas as pd\n",
        "import seaborn as sns\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "pN6MI_aOdLkK",
        "colab_type": "text"
      },
      "source": [
        "Carregando a Base de Dados"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "fH08VuIvDYqC",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# carrega o dataset de london\n",
        "from sklearn.datasets import load_boston\n",
        "boston = load_boston()"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "vdncFGtm9EZe",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# descrição do dataset\n",
        "print (boston.DESCR)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "e1d1cfElD_aD",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# cria um dataframe pandas\n",
        "data = pd.DataFrame(boston.data, columns=boston.feature_names)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "2DqDhU9Gdkme",
        "colab_type": "text"
      },
      "source": [
        "Adicionando a coluna que será nossa variável alvo"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "WaGqRi0vElWS",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# adiciona a variável MEDV\n",
        "data['MEDV'] = boston.target"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "caKPkl_SFil0",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# filtra os top 16 maiores registro da coluna MEDV\n",
        "top16 = data.nlargest(16, 'MEDV').index"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "cicsUFf4OELZ",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# remove os valores listados em top16\n",
        "data.drop(top16, inplace=True)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "X2mMG-H_xfCU",
        "colab_type": "text"
      },
      "source": [
        "**Definindo um Baseline**\n",
        "\n",
        "- `Uma baseline é importante para ter marcos no projeto`.\n",
        "- `Permite uma explicação fácil para todos os envolvidos`.\n",
        "- `É algo que sempre tentaremos ganhar na medida do possível`."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "q-k-jC68Tmra",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# converte os dados\n",
        "data.RM = data.RM.astype(int)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "cA9VCNRnUOPi",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "data.info()"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "K_-mp-6WtUee",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# estatística descritiva da coluna numero de quartos\n",
        "data.RM.describe()"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "HIknobGdtUQR",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# definindo a regra para categorizar os dados\n",
        "categorias = []"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "faL-8m1onPP2",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# alimenta a lista categorias\n",
        "for i in data.RM.iteritems():\n",
        "  valor = (i[1])\n",
        "  if valor <= 4:\n",
        "    categorias.append('Pequeno')\n",
        "  elif valor < 7:\n",
        "    categorias.append('Medio')\n",
        "  else:\n",
        "    categorias.append('Grande')"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "-nEk0wXeNFWE",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# cria a coluna categorias\n",
        "data['categorias'] = categorias"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "i-iVO76sR-am",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# imprime a contagem de categorias\n",
        "data.categorias.value_counts()"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Gxa6OrD8Ht-0",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# agrupa as categorias e calcula as médias\n",
        "medias_categorias = data.groupby(by='categorias')['MEDV'].mean()"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "zYMhxnzDIM2X",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# visualizando a variável medias_categorias\n",
        "medias_categorias"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "wJHkQXozHcYN",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# criando o dicionario com chaves medio, grande e pequeno e seus valores\n",
        "dic_baseline = {'Grande': medias_categorias[0], 'Medio': medias_categorias[1], 'Pequeno': medias_categorias[2]}"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "AMrYkM_T7eqS",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# imprime dicionario\n",
        "dic_baseline"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "7lfDPAmL8kjX",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# cria a função retorna baseline\n",
        "def retorna_baseline(num_quartos):\n",
        "  if num_quartos <= 4:\n",
        "    return dic_baseline.get('Pequeno')\n",
        "  elif num_quartos < 7:\n",
        "    return dic_baseline.get('Medio')\n",
        "  else:\n",
        "    return dic_baseline.get('Grande')"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "um5I8oQ2Arhe",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# chama a função retorna baseline\n",
        "retorna_baseline(7)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "785EhcLuCoqw",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "for i in data.RM.iteritems():\n",
        "  n_quartos = i[1]\n",
        "  print('Número de quartos é: {} , Valor médio: {}'.format(n_quartos,retorna_baseline(n_quartos)))"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "7Is3KDjcXzBG",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# imprime as 5 primeiras linhas do dataframe\n",
        "data.head()"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "SaYmsVtotcF_",
        "colab_type": "text"
      },
      "source": [
        "### Trabalhando com a baseline"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "SXXetS7AHiXz",
        "colab_type": "text"
      },
      "source": [
        "Preparando os dados"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Ai2si0SMFKVX",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# remove as colunas colineares, variavel alvo e a coluna categorias\n",
        "X = data.drop(['RAD','TAX','MEDV','DIS','AGE','ZN','categorias'], axis=1)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "vxOb-hwYFFJx",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# variável 'y' é nossa variável alvo\n",
        "y = data['MEDV']"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "EhagncsDLyk-",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# Dados na variável X\n",
        "X.head()"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "W3He9wgaL5W7",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# Variável alvo\n",
        "y.head()"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "B0I1geDbH2cV",
        "colab_type": "text"
      },
      "source": [
        "Separando os conjuntos de treino e teste"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "13W2Fe2PfoK2",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# carrega o método train_test_split\n",
        "from sklearn.model_selection import train_test_split"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "FaFtnr62AJ74",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# divide os dados entre o conjunto de treino e teste, 80% e 20% respectivamente.\n",
        "# define qualquer valor para o parâmetro random_state.\n",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=5)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "BiUsFzXQAJ38",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# imprime a quantidade de linhas dos conjuntos\n",
        "print ('X_train: numero de linhas e colunas: {}'.format(X_train.shape))\n",
        "print ('X_test: numero de linhas e colunas: {}'.format(X_test.shape))\n",
        "print ('y_train: numero de linhas e colunas: {}'.format(y_train.shape))\n",
        "print ('y_test: numero de linhas e colunas: {}'.format(y_test.shape))"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Wu94wESmFQqy",
        "colab_type": "text"
      },
      "source": [
        "Modelo de baseline"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "FI97hd4HFPtR",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# imprimindo as 5 primeiras linhas dos dados de teste\n",
        "X_test.head()"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "vRGvzY2jFbvD",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# definindo uma lista de predicoes\n",
        "predicoes = []"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xZ09WeQcGdL0",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# para cada elemento do teste alimenta a lista predicoes\n",
        "for i in X_test.RM.iteritems():\n",
        "  n_quartos = i[1]\n",
        "  predicoes.append(retorna_baseline(n_quartos))"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Zn-1qKZYF16H",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# imprime as 10 primeiras linhas da lista de predicoes\n",
        "predicoes[:10]"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "CM3QVVQ-Ug5L",
        "colab_type": "text"
      },
      "source": [
        "Atribuindo resultados a um dataframe\n",
        "\n",
        "-   `Manteremos um log ao longo do projeto`\n",
        "-   `Permite a evolução dado o baseline`\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "dMr0oUucnuy-",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# cria um dataframe vazio\n",
        "df_results = pd.DataFrame()"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "9T5FnjHnUDTA",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# adiciona a coluna valor_real\n",
        "df_results['valor_real'] = y_test.values"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "seteWjL0UDL3",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# cria a coluna valor_predito_baseline com as predicoes\n",
        "df_results['valor_predito_baseline'] = predicoes"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "6e34IoHyUC77",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# imprimindo as 10 primeiras linhas do df_results\n",
        "df_results.head(10)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "HNRa3fuzVX_6",
        "colab_type": "text"
      },
      "source": [
        "Plota o valor real e o baseline"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "wcrc2krAVJCN",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import plotly.graph_objects as go\n",
        "\n",
        "# Create traces\n",
        "fig = go.Figure()\n",
        "\n",
        "# Linha com os dados de teste\n",
        "fig.add_trace(go.Scatter(x=df_results.index,\n",
        "                         y=df_results.valor_real,\n",
        "                         mode='lines+markers',\n",
        "                         name='Valor Real'))\n",
        "\n",
        "# Linha com os dados preditos\n",
        "fig.add_trace(go.Scatter(x=df_results.index,\n",
        "                         y=df_results.valor_predito_baseline,\n",
        "                         mode='lines+markers',\n",
        "                         name='Valor Predito Baseline'))\n",
        "# Plota a figura\n",
        "fig.show()"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "IUt81GVWGHLb",
        "colab_type": "text"
      },
      "source": [
        "Avaliação do modelo baseline"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ACJFie9JF7iq",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# calcula a métrica rmse\n",
        "from sklearn.metrics import mean_squared_error\n",
        "from math import sqrt"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "6UO0iZm44Gl_",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "rmse = (np.sqrt(mean_squared_error(y_test, predicoes)))"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "aFThM7L9GDA6",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# imprime a performance do modelo\n",
        "print ('Performance do modelo baseline:')\n",
        "print('\\nRMSE é: {} '.format(rmse))"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "6jL-gszHYgZY",
        "colab_type": "text"
      },
      "source": [
        "### Machine Learning"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "8rokdiRpzTry",
        "colab_type": "text"
      },
      "source": [
        "#### Regressão Linear"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "nEbWBlL3Ir9M",
        "colab_type": "text"
      },
      "source": [
        "- `Devido a correlação entre algumas features podemos usar uma regressão linear.`\n",
        "- `Modelo simples e eficiente.`\n",
        "- `Solução rápida e robusta.`"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xy7zx_pJIw6e",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# carrega o pacote LinearRegression\n",
        "from sklearn.linear_model import LinearRegression"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "fRgZ6NHUfvzM",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# cria o objeto do tipo LinearRegression\n",
        "lin_model = LinearRegression()"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "EP4-r-x9fyMF",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# treina o algoritmo de regressão linear\n",
        "lin_model.fit(X_train, y_train)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "XwIaD1k1NVzg",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# avaliação do modelo nos dados de teste\n",
        "y_pred = lin_model.predict(X_test)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Wx7arH2JoHGU",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# calcula a métrica rmse\n",
        "rmse = (np.sqrt(mean_squared_error(y_test, y_pred)))"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "zi54cRQwNcPm",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# imprime a performance do modelo\n",
        "print ('Performance do modelo avaliado com os dados de teste:')\n",
        "print('\\nRMSE é: {} '.format(rmse))"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Fc4Cy6ehSRz7",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# atribui os resultados no dataframe df_results\n",
        "df_results['valor_predito_reg_linear'] = lin_model.predict(X_test)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "vY6sddMASRrj",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "df_results.head(10)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qojh6XHzSDHZ",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import plotly.graph_objects as go\n",
        "\n",
        "# Create traces\n",
        "fig = go.Figure()\n",
        "\n",
        "# Linha com os dados de teste\n",
        "fig.add_trace(go.Scatter(x=df_results.index,\n",
        "                         y=df_results.valor_real,\n",
        "                         mode='lines+markers',\n",
        "                         name='Valor Real'))\n",
        "\n",
        "# Linha com os dados de baseline\n",
        "fig.add_trace(go.Scatter(x=df_results.index,\n",
        "                         y=df_results.valor_predito_baseline,\n",
        "                         mode='lines+markers',\n",
        "                         name='Baseline'))\n",
        "\n",
        "# Linha com os dados preditos pela regressão linear\n",
        "fig.add_trace(go.Scatter(x=df_results.index,\n",
        "                         y=df_results.valor_predito_reg_linear,\n",
        "                         mode='lines',\n",
        "                         line = dict(color = '#FEBFB3'),\n",
        "                         name='Valor Predito Regressão Linear'))\n",
        "\n",
        "# Plota a figura\n",
        "fig.show()"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "yhHrta_etlaE",
        "colab_type": "text"
      },
      "source": [
        "##### Arvore de decisão\n",
        "\n",
        "*   `Algoritmo de aprendizado supervisionado`\n",
        "*   `Explicabilidade do Modelo`\n",
        "*   `Simples`\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "s6AMt-S1tklE",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# importa o pacote DecisionTreeRegressor\n",
        "from sklearn.tree import DecisionTreeRegressor"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "9GWqPqMatkiv",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# cria um objeto do tipo DecisionTreeRegressor\n",
        "regressor = DecisionTreeRegressor()"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "aesYvbgetkgX",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# treina o algoritmo\n",
        "regressor.fit(X_train, y_train)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "WHDUHZgHyztm",
        "colab_type": "text"
      },
      "source": [
        "Avaliando o modelo de Árvore de Decisão"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3rnUwS6Vtkdw",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# fazendo as previsões\n",
        "y_pred = regressor.predict(X_test)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "WPIrhQh_Lt4i",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# Adicionando o valor do modelo no dataframe df_results\n",
        "df_results['valor_predito_arvore'] = y_pred"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "z3bMNJK0LASe",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# visualiza o dataframe df_results\n",
        "df_results.head(10)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "PV-RAtLPN12A",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import plotly.graph_objects as go\n",
        "\n",
        "# cria uma figura\n",
        "fig = go.Figure()\n",
        "\n",
        "# Linha com os dados de teste\n",
        "fig.add_trace(go.Scatter(x=df_results.index,\n",
        "                         y=df_results.valor_real,\n",
        "                         mode='lines+markers',\n",
        "                         name='Valor Real'))\n",
        "\n",
        "# Linha com os dados de teste\n",
        "fig.add_trace(go.Scatter(x=df_results.index,\n",
        "                         y=df_results.valor_predito_baseline,\n",
        "                         mode='lines+markers',\n",
        "                         name='Valor Predito Baseline'))\n",
        "\n",
        "\n",
        "# Linha com os dados de teste\n",
        "fig.add_trace(go.Scatter(x=df_results.index,\n",
        "                         y=df_results.valor_predito_reg_linear,\n",
        "                         mode='lines+markers',\n",
        "                         name='Valor Predito Reg Liner'))\n",
        "\n",
        "# Linha com os dados preditos\n",
        "fig.add_trace(go.Scatter(x=df_results.index,\n",
        "                         y=df_results.valor_predito_arvore,\n",
        "                         mode='lines+markers',\n",
        "                         name='Valor Predito Arvore'))\n",
        "# Plota a figura\n",
        "fig.show()"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "exqvETJrM0BB",
        "colab_type": "text"
      },
      "source": [
        "Avaliação do Modelo"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "VpR1FT389JN_",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# calcula a métrica rmse\n",
        "rmse = (np.sqrt(mean_squared_error(y_test, y_pred)))"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "cEBz7JpJyYcm",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# imprime a performance do modelo\n",
        "print ('Performance do modelo avaliado com os dados de teste:')\n",
        "print('\\nRMSE é: {} '.format(rmse))"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "IPf53dk8cQ4A",
        "colab_type": "text"
      },
      "source": [
        "#### Random Forest\n",
        "\n",
        "- `Método Ensemble`\n",
        "- `Mais robustez para os modelos`"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "dXpfe5pfWcxs",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# Importa o método RandomForestRegressor\n",
        "from sklearn.ensemble import RandomForestRegressor"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "G-TcDYH6WcqX",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# cria o objeto rf_regressor\n",
        "rf_regressor = RandomForestRegressor()"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "PXwdpDXdWcm5",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# treina o algoritmo\n",
        "rf_regressor.fit(X_train, y_train)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "YJp4BOStc5bS",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# avaliação do modelo nos dados de teste\n",
        "y_pred = rf_regressor.predict(X_test)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "2jH8pO-PdD3I",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# adiciona os resultados no dataframe df_results\n",
        "df_results['valor_predito_random_forest'] = rf_regressor.predict(X_test)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "WLxMyfruc5UO",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# calcula a métrica rmse\n",
        "rmse = (np.sqrt(mean_squared_error(y_test, y_pred)))"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "V7Yt6UAxc5MQ",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# imprime a performance do modelo\n",
        "print ('Performance do modelo avaliado com os dados de teste:')\n",
        "print('\\nRMSE é: {} '.format(rmse))"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xKy2c8eidpdW",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# plota os resultados dos modelos e o valor real.\n",
        "import plotly.graph_objects as go\n",
        "\n",
        "# Create traces\n",
        "fig = go.Figure()\n",
        "\n",
        "# Linha com os dados de teste\n",
        "fig.add_trace(go.Scatter(x=df_results.index,\n",
        "                         y=df_results.valor_real,\n",
        "                         mode='markers',\n",
        "                         name='Valor Real'))\n",
        "\n",
        "# Linha com os dados da baseline\n",
        "fig.add_trace(go.Scatter(x=df_results.index,\n",
        "                         y=df_results.valor_predito_baseline,\n",
        "                         mode='lines+markers',\n",
        "                         line = dict(color = '#FF00FF'),\n",
        "                         name='Valor da Baseline'))\n",
        "\n",
        "# Linha com os dados preditos pela arvore\n",
        "fig.add_trace(go.Scatter(x=df_results.index,\n",
        "                         y=df_results.valor_predito_arvore,\n",
        "                         mode='lines',\n",
        "                         line = dict(color = '#B2FF66'),\n",
        "                         name='Valor Predito Árvore'))\n",
        "\n",
        "# Linha com os dados preditos pela regressão linear\n",
        "fig.add_trace(go.Scatter(x=df_results.index,\n",
        "                         y=df_results.valor_predito_reg_linear,\n",
        "                         mode='lines',\n",
        "                         line = dict(color = '#17BECF'),\n",
        "                         name='Valor Predito Regressão Linear'))\n",
        "\n",
        "\n",
        "# Linha com os dados preditos pela Random Forest\n",
        "fig.add_trace(go.Scatter(x=df_results.index,\n",
        "                         y=df_results.valor_predito_random_forest,\n",
        "                         mode='lines',\n",
        "                         line = dict(color = '#7F7F7F'),\n",
        "                         name='Valor Predito Random Forest'))\n",
        "\n",
        "# Plota a figura\n",
        "fig.show()"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "udB7k-TMe9tj",
        "colab_type": "text"
      },
      "source": [
        "### Tunning do Algoritmo de Machine Learning"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "-ivExBIzzrmX",
        "colab_type": "text"
      },
      "source": [
        "**Parâmetros da Random Forest**\n",
        "\n",
        "- `O parâmetro n_estimators define a quantidade de árvores que serão usadas para criação dos modelos. Quanto maior o número de árvores, maior será o número de modelos no ensemble.`\n",
        "\n",
        "- `O parâmtro max_deph define a profundidade da árvore, quanto mais profunda a árvore, mais especializado nos dados de treino o nosso modelo estará.`\n",
        "\n",
        "- `O parâmetro max_features define a quantidade máxima de nós que serão usados para separar os níveis folha da árvore`"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Kt1_TcBfWn31",
        "colab_type": "text"
      },
      "source": [
        "Deploy da Aplicação"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "o_vwA3soYjYq",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "X['MEDV'] = y"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "x5-qVIdOZwdt",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "X.head()"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "vbPO7woOa7N0",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "X.to_csv('data.csv', index=False)"
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}